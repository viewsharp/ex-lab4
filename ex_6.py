#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = sys.argv[1]

with open(path) as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    return list(field(arg, 'job-name'))


@print_result
def f2(arg):
    return filter(lambda line: line.lower().find('программист') != -1, arg)


@print_result
def f3(arg):
    return list(map(lambda line: line + ' с опытом Python', arg))


@print_result
def f4(arg):
    items = zip(arg, gen_random(100000, 200000, len(arg)))
    return ['{0}, зарплата {1} руб.'.format(item[0], item[1]) for item in items]


with timer():
    f4(f3(f2(f1(data))))
