# coding=utf-8

numbers = {0: 'no',
           1: 'one',
           2: 'two',
           3: 'three',
           4: 'four',
           5: 'five',
           6: 'six',
           7: 'seven',
           8: 'eight',
           9: 'nine',
           10: 'ten'}

first_line_format = '%s green bottles hanging on the wall,'
third_line_format = 'And if %s green bottle should accidentally fall,'
fourth_line_format = 'There’ll be %s green bottles hanging on the wall.'

start = 10
step = 1
for i in range(start, 0, -step):
    print first_line_format % numbers[i].title()
    print first_line_format % numbers[i].title()
    print third_line_format % numbers[step]
    print fourth_line_format % numbers[i - 1]
