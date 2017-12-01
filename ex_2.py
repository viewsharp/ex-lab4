#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)

# Реализация задания 2
if __name__ == '__main__':
    print('# Unique(data1)')
    results = list(Unique(data1))
    print(*results, sep=', ', end='\n\n')

    print('# Unique(data2)')
    results = list(Unique(data2))
    print(*results, sep=', ', end='\n\n')

    print('# Unique([‘a’, ‘A’, ‘b’, ‘B’])')
    results = list(Unique(['a', 'A', 'b', 'B']))
    print(*results, sep=', ', end='\n\n')

    print('# Unique([‘a’, ‘A’, ‘b’, ‘B’], ignore_case=True)')
    results = list(Unique(['a', 'A', 'b', 'B'], ignore_case=True))
    print(*results, sep=', ', end='\n\n')
