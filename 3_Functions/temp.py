def num(a):
    if a % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"


def cus_num(a):
    if a % 2 == 0:
        return "Even Number"
    return "Odd Number"



print(num(3))
print(cus_num(3))


envs = ('dev', 'test', 'prod')

 for elem in ('dev', 'test', 'prod'):
