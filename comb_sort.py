# Title: comb_sort.py
# Author: J. Mayeux - pyRN
# Date: 8/19/17

import time


def comb_sort(array, amount):
    print('*' * 50)
    print('Comb Sort'.center(50))
    print('*' * 50, '\n')
    print('Unsorted', amount, 'item array--->', array, '\n')
    start = time.time()

    divider = int(len(array) / 1.3)

    for a in range(0, len(array)):

        for b in range(0, len(array)):
            if (b + divider) > len(array) - 1:
                break

            if array[b] > array[b + int(divider)]:
                array[b], array[b + int(divider)] = array[int(divider) + b], array[b]

        divider = int(divider / 1.3)

        if divider < 1:
            for c in range(0, len(array) - 1):
                if array[c] > array[c + 1]:
                    array[c], array[c + 1] = array[c + 1], array[c]
            break

    finish = time.time()
    print('Sorted', amount, 'item array--->', array, '\n')
    print('Sorting took', finish - start, 'seconds', '\n')
