# read and calculate math expression with no parentheses
import re


operators = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x / y,
             }


def split_exp(exp):
    if exp.startswith('-'):
        exp = 'neg' + exp[1:]

    # replace negtive mark
    exp = exp.replace(' ', '').replace('*-', '*neg').replace('+-', '+neg').replace('/-', '/neg').replace(
        '--', '+')
    arr = re.split(r'\s*([-+/*])\s*', exp)
    replace_neg = lambda x: x.replace('neg', '-')
    arr = list(map(replace_neg, arr))
    return arr


def cal_exp(expression):
    arr = split_exp(expression)
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y,
                 }
    i = 1
    while i < len(arr) - 1:
        if arr[i] in '*/':
            y = int(arr[i + 1])
            x = int(arr[i - 1])
            arr[i] = operators[arr[i]](x, y)
            arr.pop(i + 1)
            arr.pop(i - 1)
            continue
        else:
            i += 1
    i = 1
    while i < len(arr) - 1:
        if arr[i] in '+-':
            y = int(arr[i + 1])
            x = int(arr[i - 1])
            arr[i] = operators[arr[i]](x, y)
            arr.pop(i + 1)
            arr.pop(i - 1)
            continue
        else:
            i += 1

    return arr[0]


if __name__ == '__main__':
    expression1 = "3+4*2-5"
    expression2 = '-10 * 2/2 + 5 - 3 * -4--3'
    expression3 = "8 - 6 + 2 * 3"

    assert eval(expression1) == cal_exp(expression1)
    assert eval(expression2) == cal_exp(expression2)
    assert eval(expression3) == cal_exp(expression3)
    print('done')
