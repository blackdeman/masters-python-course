"""Print selected parts of lines from FILE to standard output.

Examples:
    Print 2 and 0 column of each line from file 'input.txt':
        $ cut.py -f 2,0 input.txt
    Print 0, 1 and 2 column of each line from file 'input.txt', using '%' as separator:
        $ cut.py -f 0,1,2 -s % input.txt
"""
import csv


def cut(input_file, fields, separator='\t'):
    """Print selected parts of lines from FILE to standard output.

    Args:
        input_file: path to file that should be processed
        fields: list of ints greater or equals to 0, that describes column numbers
                    and order in which columns should be presented in result line
        separator: specifies a separator to be used(instead of TAB) for splitting lines on parts

    Returns:
        string: string that contains columns in specified order

    Raises:
        ValueError: if line contains less columns than specified in fields argument
    """
    result = ""
    max_field = max(fields)

    with open(input_file, "r") as f:
        c = csv.reader(f, delimiter=separator, skipinitialspace=True)
        for line in c:
            if len(line) < max_field + 1:
                raise ValueError("Line '{}' contains less columns than specified in fields argument (max = {})"
                                 .format(separator.join(line), max_field))
            result += separator.join([line[i] for i in fields]) + '\n'
    return result


class ParseError(Exception):
    pass


def __parse_fields(fields):
    try:
        return [int(f) for f in fields.split(",")]
    except Exception:
        raise ParseError("Error while parsing FIELDS: '{}' is not a valid input string.".format(args.fields))


def __parse_separator(separator):
    if len(separator) > 1:
        raise ParseError("Separator should consist of only one character: '{}' is not valid".format(separator))
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
        print cut(args.FILE, __parse_fields(args.fields), __parse_separator(args.separator))
    except ParseError, e:
        print e
        parser.print_help()
    except Exception, e:
        print e
