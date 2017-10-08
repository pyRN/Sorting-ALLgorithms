# Title: bubble_sort.py
# Author: J. Mayeux - pyRN
# Date: 7-30-17

import time


def bubble_sort(array, amount):
    print('*' * 50)
    print('Bubble Sort'.center(50))
    print('*' * 50, '\n')
    print('Unsorted', amount, 'item array--->', array, '\n')
    start = time.time()

    for x in range(0, len(array) - 1):   # Loop should break prior to final iteration, unless sorted in reverse first
        z = 0
        for y in range(0, (len(array) - 1) - x):  # (len(sortarray)-1)-x) will decrease sort time each iteration
            if array[y] > array[y + 1]:
                array[y], array[y + 1] = array[y + 1], array[y]
                z += 1
        if z == 0:
            finish = time.time()
            print('Sorted', amount, 'item array--->', array, '\n')
            print('Sorting took', finish-start, 'seconds and ', x + 1, 'iterations', '\n')
            break
