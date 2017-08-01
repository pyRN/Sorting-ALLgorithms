import random
import time


def insertion_sort(array, amount):
    print('#' * 30)
    print('Insertion Sort'.center(30))
    print('#' * 30)
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
    

def bubble_sort(array, amount):
    print('#' * 30)
    print('Bubble Sort'.center(30))
    print('#' * 30)
    print('Unsorted', amount, 'item array--->', array, '\n')
    start = time.time()

    for x in range(0, len(array) - 1):   # Loop should break prior to final iteration, unless sorted in reverse first
        z = 0
        for y in range(0, (len(array) - 1) - x):  # (len(array)-1)-x) will decrease sort time each iteration
            if array[y] > array[y + 1]:
                array[y], array[y + 1] = array[y + 1], array[y]
                z += 1
        if z == 0:
            finish = time.time()
            print('Sorted', amount, 'item array--->', array, '\n')
            print('Sorting took', finish-start, 'seconds and ', x + 1, 'iterations')
            break


def main():
    array = []
    amount = random.randint(10, 1010)

    for i in range(0, amount):
        array.append(random.randint(0, 1000))

    insertion_sort(array.copy(), amount)
    bubble_sort(array.copy(), amount)

main()
