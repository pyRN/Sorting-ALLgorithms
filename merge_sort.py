# Title: merge_sort.py
# Author: J. Mayeux - pyRN
# Date: 10-3-17

import time


def split_array(array):
    if len(array) <= 1:
        return array
    midpoint = int(len(array)//2)
    left = split_array(array[:midpoint])
    right = split_array(array[midpoint:])
    return merge_sort(left, right)



def merge_sort(left, right):
    sorted_array = []
    i = 0
    j = 0


    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i = i+1
        else:
            sorted_array.append(right[j])
            j = j+1
    sorted_array += left[i:]
    sorted_array += right[j:]
    print(sorted_array)
    return sorted_array


def main():
    print('*' * 50)
    print('Merge Sort'.center(50))
    print('*' * 50, '\n')
    #print('Unsorted', amount, 'item array--->', array, '\n')
    array = [779, 167, 264, 237, 29, 578, 987, 729, 70, 744, 929, 553, 107, 244, 210, 118, 581, 404]
    start = time.time()

    split_array(array.copy())

    finish = time.time()

    #print('Sorted', amount, 'item array--->', array, '\n')
    print('Sorting took', finish - start, 'seconds', '\n')

main()


