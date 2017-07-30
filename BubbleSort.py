# Title: Bubble Sort
# Author: J. Mayeux - pyRN
# Date: 7-30-17

import random
import time

def bubblesort(list, amount):

    print('Unsorted', amount, 'item list--->', list, '\n')
    start = time.time()

    for x in range(0, len(list) - 1):   # This loop should break prior to final iteration, unless list in sorted in reverse first
        z = 0
        for y in range(0, (len(list) - 1) - x):  # Statement (len(sortlist)-1)-x) will decrease sort time each iteration
            if list[y] > list[y + 1]:
                list[y], list[y + 1] = list[y + 1], list[y]
                z += 1
        if z == 0:
            finish = time.time()
            print('Sorted', amount, 'item list--->', list, '\n')
            print('Sorting took', finish-start, 'seconds and ', x + 1, 'iterations')
            break

def main():
    list = []
    amount = random.randint(10, 1010)

    for i in range(0, amount):
        list.append(random.randint(0,1000))

    bubblesort(list, amount)

main()