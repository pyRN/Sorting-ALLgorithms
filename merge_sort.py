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
    return sorted_array


def main(array, amount):
    print('*' * 50)
    print('Merge Sort'.center(50))
    print('*' * 50, '\n')
    start = time.time()

    split_array(array.copy())

    finish = time.time()
    print('Sorting of a ', amount, 'array took', finish - start, 'seconds', '\n')
    # Need to figure out how to print sorted array for this algorithm.


