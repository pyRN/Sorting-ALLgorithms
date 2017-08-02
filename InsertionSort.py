# Title: Insertion
# Author: J. Mayeux - pyRN
# Date: 7-30-17

import time


def insertion_sort(array, amount):
    print('Unsorted', amount, 'item array--->', array, '\n')
    start = time.time()

    for x in range(0, amount):
        hold = []

        if x != 0 and array[x] <= array[x - 1]:
            hold.append(array.pop(x))  # Remove number at index and store in hold
            for y in range(x - 1, -1, -1):  # This will only cycle through indexes that have viewed

                if hold[0] <= array[y]:
                    if hold[0] >= array[y - 1] or y == 0:
                        array.insert(y, hold.pop())
                        break

    finish = time.time()
    print('Sorted', amount, 'item array--->', array, '\n')
    print('Sorting took', finish - start, 'seconds')
