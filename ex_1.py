#!/usr/bin/env python3
from librip.gens import field, gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'},
    {},
    {'title': 'Ковер'},
    {'title': 'Ковер', 'price': 2000},
]

# Реализация задания 1
if __name__ == '__main__':
    print("# gen_field(goods, 'title')")
    results = list(field(goods, 'title'))
    print(*results, sep=', ', end='\n\n')

    print("# gen_field(goods, 'title', 'price')")
    results = list(field(goods, 'title', 'price'))
    print(*results, sep=', ', end='\n\n')

    print("# gen_field(goods, 'title', 'price', 'color')")
    results = list(field(goods, 'title', 'price', 'color'))
    print(*results, sep=', ', end='\n\n')

    print("# gen_random(1, 3, 5)")
    results = list(gen_random(1, 3, 5))
    print(*results, sep=', ', end='\n\n')
