# -*- coding: utf-8 -*-

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import txt


def test_txt_read():
    txt_path = '/Users/sybil/git/read_write/test.txt'
    out = txt.my_read(txt_path)
    print out


def test_txt_write():
    txt2_path = '/Users/sybil/git/read_write/test2.txt'
    txt_test = u'徐飞是个大坏蛋'
    txt.my_write(txt2_path, txt_test)


test_txt_read()
test_txt_write()
