import random
import selection_sort
import bubble_sort
import insertion_sort
import comb_sort
import merge_sort


def main():
    array = []
    amount = random.randint(10, 1010)

    for i in range(0, amount):
        array.append(random.randint(0, 1000))

    insertion_sort.insertion_sort(array.copy(), amount)
    bubble_sort.bubble_sort(array.copy(), amount)
    selection_sort.selection_sort(array.copy(), amount)
    comb_sort.comb_sort(array.copy(), amount)
    merge_sort.main(array.copy(), amount)

main()
