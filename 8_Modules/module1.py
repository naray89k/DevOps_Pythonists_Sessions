# module1.py

print(f'---------------------- Running {__name__} -----------------')


def pprint_dict(header, d):
    """
    This is a function to pretty print dictionary
    :param header:
    :param d:
    :return:
    """
    print('\n\n -----------------------------------')
    print(f'------------- HEADER ------------------')
    for key, value in d.items():
        print(key, value)
    print(' -------------------------------\n\n')


pprint_dict('module1.globals', globals())

print(f'------------------------------ end of {__name__}')
