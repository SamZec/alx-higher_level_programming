#!/usr/bin/python3
import hidden_4


def _hidden():
    for i in dir(hidden_4):
        if chr(95) not in i[0]:
            print("{}".format(i))


if __name__ == "__main__":
    _hidden()
