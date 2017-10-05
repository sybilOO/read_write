# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import codecs
import csv
import os
xpath = os.path.dirname(os.path.abspath(__file__))
# csvfile = csv.reader(codecs.open('/Users/sybil/Downloads/hanbao_temp322.csv', 'rU', 'utf-8'))

def my_read(path):
    with open(path, 'rb') as f:  # 采用b的方式处理可以省去很多问题
        reader = csv.reader(f)
        for row in reader:
            print row[0]
            print row[1]
            print row[2]


def my_write(path, content):
    with open(path, 'wb') as f:  # 采用b的方式处理可以省去很多问题
        f.write(codecs.BOM_UTF8)
        writer = csv.writer(f)
        writer.writerow(['id', 'article', 'sentiments'])
        writer.writerows(content)

if __name__ == '__main__':
    test_path = os.path.join(xpath, 'test.csv')
    print my_read(test_path)

    test = [u'我有一条小毛驴', 'a124232', 'lalal']
    test2_path = os.path.join(xpath, 'test.csv')

    my_write(test2_path, test)

'''
import os
import csv

#xpath = os.path.dirname(os.path.abspath(__file__))
#test2_path = os.path.join(xpath, 'test.csv')
with open('/Users/sybil/github/read_write/csv/test.csv', 'wb') as f:  # 采用b的方式处理可以省去很多问题
    a = csv.writer(f)
    a.writerows([u'我有一条小毛驴', 'a124232', 'lalal'])
'''