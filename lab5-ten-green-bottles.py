# coding=utf-8


def get_plural_form(s, count):
    return s if count == 1 else s + 's'


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

first_line_format = '%s green %s hanging on the wall,'
third_line_format = 'And if %s green %s should accidentally fall,'
fourth_line_format = 'There’ll be %s green %s hanging on the wall.'

word = 'bottle'
start = 10
step = 1

for i in range(start, 0, -step):
    print first_line_format % (numbers[i].title(), get_plural_form(word, i))
    print first_line_format % (numbers[i].title(), get_plural_form(word, i))
    print third_line_format % (numbers[step], get_plural_form(word, step))
    print fourth_line_format % (numbers[i - 1], get_plural_form(word, i - 1))
