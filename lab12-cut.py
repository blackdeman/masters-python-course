"""
Print selected parts of lines from FILE to standard output.
"""
import csv


def cut(input_file, fields, separator):
    max_field = max(fields)

    with open(input_file, "r") as f:
        c = csv.reader(f, delimiter=separator, skipinitialspace=True)
        for line in c:
            if len(line) < max_field + 1:
                raise Exception("Line '{}' contains less columns than specified in FIELDS argument (max = {})"
                                .format(separator.join(line), max_field))
            print separator.join([line[i] for i in fields])


class ParseException(Exception):
    pass


def __parse_fields(fields):
    try:
        return [int(f) for f in fields.split(",")]
    except Exception:
        raise ParseException("Error while parsing FIELDS: '{}' is not a valid input string.".format(args.fields))


def __parse_separator(separator):
    if len(separator) > 1:
        raise ParseException("Separator should consist of only one character: '{}' is not valid".format(separator))
    return separator


if __name__ == "__main__":
    import argparse
    from argparse import RawTextHelpFormatter

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument('FILE',
                        help='file to read lines from')
    parser.add_argument('-f', '--fields', metavar='FIELDS',
                        help='select only columns described by FIELDS\n'
                             'FIELDS should be a string of ints greater or equals to 0, separated with comma\n'
                             'example: 0,3,1', required=True)
    parser.add_argument('-s', '--separator', metavar='SEP', default='\t',
                        help='use SEP instead of TAB for field separator')

    args = parser.parse_args()

    try:
        cut(args.FILE, __parse_fields(args.fields), __parse_separator(args.separator))
    except ParseException, e:
        print e
        parser.print_help()
    except Exception, e:
        print e
