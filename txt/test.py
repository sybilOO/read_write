# -*- coding: utf-8 -*-

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import txt
import os
#path = os.path.abspath(os.curdir)

path = os.path.dirname(os.path.abspath(__file__))

def test_txt_read():
    txt_path = os.path.join(path, 'test.txt')
    out = txt.my_read(txt_path)
    print out


def test_txt_write():
    txt2_path = os.path.join(path, 'test2.txt')
    txt_test = u'徐飞是dada个大坏蛋'
    txt.my_write(txt2_path, txt_test)


test_txt_read()
test_txt_write()

