# filter
my_list = [1, 2, 3, 4]


def check_odd(li):
    return li % 2 != 0


print(list(filter(check_odd, my_list)))
