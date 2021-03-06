import csv
import os
import sys
import re
import json
from glob import glob
from configparser import ConfigParser
from datetime import datetime
from argparse import ArgumentParser

# GLOBAL VARIABLES
# ================
ACCEPTABLE_CATEGORIES = ["BEER & CIDER", "CASHBACK", "CIGARETTES",
                         "CONFECTIONARY", "DAIRY", "GROCERY",
                         "LOTTERY", "NEWSPAPERS", "PAYZONE",
                         "PET FOOD", "SOFT DRINK", "SPIRIT",
                         "WASHING", "WINE"]

def validate_file(file_name):
    if os.path.isfile(file_name):
        return file_name
    raise FileNotFoundError(f"{file_name} Not found")


def get_args():
    parser = ArgumentParser(description='Process command line arguments')
    parser.add_argument('--config_file', dest='config_file', type=validate_file,
                        required=True,
                        help='Absolute path of the config file')
    args = parser.parse_args()
    return args


def get_config(config_file):
    config = ConfigParser()
    config.read(config_file)
    return config


def get_files(text_dir):
    try:
        files_list = glob(text_dir + '/*.txt')
        return files_list
    except Exception as exp:
        print(exp.__class__, exp)
        sys.exit(1)


def cleanup(dir_name):
    """

    :param dir_name:
    :return:
    Function to cleanup files in dir_name
    """
    print(f"Cleaning up {dir_name}")
    try:
        files_list = glob(dir_name + '/*.json')
        for file_name in files_list:
            print(f"Deleting {file_name}")
            os.remove(file_name)
    except Exception as exp:
        print(exp.__class__, exp)
        sys.exit(1)


def validate_date_string(date_str):
    try:
        datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S")
        return True
    except ValueError as ve:
        print(ve)
        return False


def validate_date_format(date_string):
    date_pattern = re.compile(r'\d+/\d+/\d+ \d+:\d+:\d+')
    if date_pattern.search(date_string):
        return True
    return False


def process_txt(text_file):
    print(f"Processing {text_file}")
    try:
        data_dict = {}
        date_str = ''
        # info: (observed pattern in text files
        # Categories are separated by ---- and total is separated by --
        req_format = re.compile(r'\-\-\-\-')
        total_format = re.compile(r'\-\-')
        with open(text_file, encoding='UTF-8') as file_obj:
            for line in file_obj.readlines():
                line_str = line.strip()
                if req_format.search(line):
                    category, sold_amount = line_str.split('----')
                    if category in ACCEPTABLE_CATEGORIES:
                        data_dict[category] = sold_amount
                    # print(line_str)
                elif total_format.search(line_str):
                    total, total_sale = line_str.split('--')
                    data_dict["TOTAL_SALES"] = total_sale
                elif validate_date_format(line_str):
                    date_str = line_str

        date_obj = datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S")
        return {date_obj: data_dict}
    except Exception as exp:
        print(exp.__class__, exp)
        sys.exit(1)


def refine_daily_report(datetime_obj, data):
    """
    :param datetime_obj (date object)
    :param data (dictionary of dictionary)
    :return:
    """
    dated_report = {}
    for elem in data:
        if datetime_obj.date() == elem.date():
            dated_report[elem] = data[elem]
    latest = max(dated_report)
    return {latest: dated_report[latest]}


def refine_data(data):
    """
    :param data (dictionary of dictionary)
    :return:
    """
    refined_data = {}
    for elem in data:
        daily_data = refine_daily_report(elem, data)
        datetimeobj = next(iter(daily_data))
        refined_data[datetimeobj] = daily_data[datetimeobj]
    return refined_data


def write_json(json_dir, file_name, data):
    try:
        json_abs_path = os.path.join(json_dir, file_name)
        with open(json_abs_path, "w", encoding='UTF-8') as file_obj:
            json.dump(data, file_obj, indent=4, ensure_ascii=False, sort_keys=data.keys())
    except Exception as exp:
        print(exp.__class__, exp)


def generate_csv_report(categories, json_data, start_date, end_date):
    csv_content = []
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()

    # Filter the report according to the date range given in config file.
    report_dates = []
    for date in sorted(json_data):
        date_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S").date()
        if start_date_obj <= date_obj <= end_date_obj:
            report_dates.append(date)

    report_dates_for_header = [date[0:10] for date in report_dates]
    header = ["CATEGORIES"] + report_dates_for_header
    csv_content.append(header)

    for category in categories:
        datewise_category_sales = []
        for date in report_dates:
            if category in json_data[date]:
                datewise_category_sales.append(json_data[date][category])
            else:
                datewise_category_sales.append('??0.00')
        row = [category] + datewise_category_sales
        csv_content.append(row)
    return csv_content


def write_report_csvfile(csv_content, csv_dir):
    try:
        csv_file_name = os.path.join(csv_dir, f'{datetime.now().strftime("%Y%m%d")}_generated_report.csv')
        with open(csv_file_name, 'w', newline='') as csv_obj:
            csv_writer = csv.writer(csv_obj)
            csv_writer.writerows(csv_content)
    except Exception as exp:
        print(exp.__class__, exp)
        sys.exit(1)


def main():
    args = get_args()
    config_file = args.config_file
    config_content = get_config(config_file)
    text_dir = config_content["DEFAULT"]["text_dir"].strip()
    csv_dir = config_content["DEFAULT"]["csv_dir"].strip()
    json_dir = config_content["DEFAULT"]["json_dir"].strip()
    start_date = config_content["DEFAULT"]["start_date"].strip()
    end_date = config_content["DEFAULT"]["end_date"].strip()

    # CLEANUP JSON DIR
    cleanup(json_dir)

    # GET LIST OF TEXT FILES
    text_files = get_files(text_dir)

    report = {}
    for text_file in text_files:
        daily_data = process_txt(text_file)
        date_obj = next(iter(daily_data))
        report[date_obj] = daily_data[date_obj]
    print()

    # refine json_data by removing duplicate reports generated in single date by
    # by considering only latest report for that day.
    refined_report = refine_data(report)

    json_data = {}
    for elem in refined_report:
        date_repr = elem.strftime("%Y-%m-%d %H:%M:%S")
        json_data[date_repr] = refined_report[elem]

    unique_categories = set()
    for elem in refined_report:
        for category in refined_report[elem]:
            unique_categories.add(category)

    # Write report to json file
    print("Writing contents to json file")
    write_json(json_dir, "report.json", json_data)

    # Convert unique_categories to list format
    unique_categories = list(sorted(unique_categories))
    # Move "TOTAL_SALES" to the last index.
    unique_categories.remove("TOTAL_SALES")
    unique_categories.append("TOTAL_SALES")

    # Prepare csv report content and write it to csv file.
    print("Preparing csv report content and write it to csv file.")
    csv_rows = generate_csv_report(unique_categories, json_data, start_date, end_date)
    write_report_csvfile(csv_rows, csv_dir)


if __name__ == '__main__':
    main()
