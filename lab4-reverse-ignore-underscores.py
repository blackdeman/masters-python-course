# coding=utf-8

import re

# sample
# “_____The___Day_That_Never_Comes___”
# “_____Comes___Never_That_Day_The___”


def reverse_ignore_underscores(s):
    return re.sub('[a-zA-Z]+', '%s', s) % tuple(reversed([x for x in s.split('_') if x != '']))


def reverse_ignore_underscores_2(s):
    splitted = s.split('_')

    reversed_list = list(reversed([x for x in splitted if x != '']))
    indexes = [i for i in xrange(len(splitted)) if splitted[i] != '']

    for i in xrange(len(indexes)):
        splitted[indexes[i]] = reversed_list[i]

    return '_'.join(splitted)

tests = ['_____The___Day_That_Never_Comes___', 'Hello___World__', '____Hello_world', 'Hello' ]

for s in tests:
    print "--- Test ---"
    print s
    print reverse_ignore_underscores(s)


