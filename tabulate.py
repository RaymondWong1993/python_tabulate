# *-* coding: utf-8 -*-
import sys
import unicodedata
reload(sys)
sys.setdefaultencoding('utf8')

def inline_print(string, count):
    for i in range(0, count):
        sys.stdout.write(string)

def has_hz(text):
    result = False
    for ch in text:
        if isinstance(ch, unicode):
            if unicodedata.east_asian_width(ch) != 'Na':
                result = True
                break
        else:
            continue

    return result

def grid(header, table):
    length = getLength(header, table)

    inline_print('+', 1)
    for item in length:
        inline_print('-', item)
        inline_print('+', 1)

    print ''
    inline_print('|', 1)
    for i in range(0, len(header)):
        count = length[i]
        inline_print(header[i], 1)
        if has_hz(unicode(header[i], encoding='utf-8')):
            count = count - (len(unicode(header[i], encoding='utf-8')) * 2)
        else:
            count = count - len(header[i])
        inline_print(' ', count)
        inline_print('|', 1)
    
    print ''
    inline_print('+', 1)
    for item in length:
        inline_print('=', item)
        inline_print('+', 1)

    for i in range(0, len(table)):
        print ''
        inline_print('|', 1)
        for j in range(0, len(table[i])):
            count = length[j]
            inline_print(table[i][j], 1)
            if has_hz(unicode(table[i][j], encoding='utf-8')):
                count = count - (len(unicode(table[i][j], encoding='utf-8')) * 2)
            else:
                count = count - len(table[i][j])
            inline_print(' ', count)
            inline_print('|', 1)
        
        print ''
        inline_print('+', 1)
        for item in length:
            inline_print('-', item)
            inline_print('+', 1)
        
    print ''

def toUnicode(text):
    if isinstance(text, unicode):
        return text
    else:
        return unicode(text, encoding='utf-8')

def getLength(header, table):
    length = []
    for item in header:
        length.append(len(toUnicode(item)) * 2)

    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            if len(toUnicode(table[i][j])) * 2 > length[j]:
                length[j] = len(toUnicode(table[i][j])) * 2

    return length

if __name__ == '__main__':
    header = ['header1', 'header2', 'header3']
    table = [['cell11', 'cell12', 'cell13'], ['cell21','cell22','cell23'], ['cell31','cell32', 'cell33']]
    grid(header, table)
