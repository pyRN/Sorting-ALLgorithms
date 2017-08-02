# Title: Selection Sort
# Author: J. Mayeux - pyRN
# Date: 8-2-17

import time


def selection_sort(array, amount):
    print('Unsorted', amount, 'item array--->', array, '\n')
    start = time.time()

    for x in range(0, amount):
        low = x
        sort = x
        for y in range(sort, amount):
            if array[sort] <= array[y] <= array[low]:
                low = y
            sort = sort + 1
            if sort > amount:
                break
        array[x], array[low] = array[low], array[x]
    finish = time.time()
    print('Sorted', amount, 'item array--->', array, '\n')
    print('Sorting took', finish - start)
