# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

'''f = open('/Users/sybil/git/read_write/test.txt', 'r')
a = f.read()
print a

f.close()

print '* '*10


with open('/Users/sybil/git/read_write/test.txt', 'r') as f:
    print(f.read())

print '* '*10


with open('/Users/sybil/git/read_write/test2.txt', 'w') as f:
    f.write('中文'.encode('utf-8'))
'''








testpath = '/Users/sybil/git/read_write/test.txt'

test2path = '/Users/sybil/git/read_write/test2.txt'
def read_txt(path):
    f = open(path, 'r')
    a = f.read()
    return a
    f.close()

read_txt(testpath)

def write_txt(path,code):
    with open(path, 'w') as f:
        f.write(code.encode('utf-8'))

test = '我有一头小毛驴，lalalla'
write_txt(test2path, test)


if __name__ == '__main__':
    test_path = '/Users/sybil/git/read_write/test.txt'
    read_txt(testpath)


