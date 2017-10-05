# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf8')


def my_read(path):
    #   f = open(path, 'r')
    #   a = f.read()
    #  f.close()
    with open(path, 'r') as f:
        a = f.read()
        return a


def my_write(path, code):
    with open(path, 'w') as f:
        f.write(code.encode('utf-8'))


if __name__ == '__main__':
    test_path = '/Users/sybil/github/read_write/test.txt'
    print my_read(test_path)

    test = '我有一头小毛驴，lalalla'
    test2_path = '/Users/sybil/github/read_write/test2.txt'

    my_write(test2_path, test)
