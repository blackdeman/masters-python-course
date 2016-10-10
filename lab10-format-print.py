

def format_print(obj, level=0):
    result = ""
    if isinstance(obj, list):
        result += "[\n"
        for subobj in obj:
            result += '\t' * (level + 1) + format_print(subobj, level + 1) + ",\n"
        result += '\t' * level + "]"
    elif isinstance(obj, dict):
        result += "{\n"
        for k, v in obj.iteritems():
            result += '\t' * (level + 1) + format_print(k, level + 1) + " : " + format_print(v, level + 1) + ",\n"
        result += '\t' * level + "}"
    else:
        result += str(obj)
    return result


tests = [1, [1, 2, 3, [4, 5]], [1, {'a': [1, 2], 'b': 'hi'}], {'x' : 5, 3 : "y"}]

for test in tests:
    print "Input : ", test, "\nOutput\n", format_print(test)
