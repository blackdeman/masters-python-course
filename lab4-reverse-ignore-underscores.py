# coding=utf-8

import re

# sample
# “_____The___Day_That_Never_Comes___”
# “_____Comes___Never_That_Day_The___”


def reverse_ignore_underscores(s):
    return re.sub('[a-zA-Z]+', '%s', s) % tuple(reversed([x for x in s.split('_') if x != '']))


print reverse_ignore_underscores('_____The___Day_That_Never_Comes___')

# s = '_____The___Day_That_Never_Comes___'
# print [x for x in s.split('_') if x != '']
# print s
# splitted = s.split('_')
# print splitted
# triples = [[i, splitted[i], -1] for i in xrange(len(splitted)) if splitted[i] != '']

# mapped = {i: splitted[i] for i in xrange(len(splitted))}
# print mapped

# print '_'.join(splitted)
