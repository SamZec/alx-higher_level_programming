#!/usr/bin/python3
try:
    def safe_print_list_integers(my_list=[], x=0):
        count = 0
        for i in range(0, x):
            t = my_list[i]
            if not isinstance(t, int):
                continue
            print("{:d}".format(t), end='')
            count += 1
        print()
        return count
except Exception as e:
    pass
