import random
import SelectionSort
import BubbleSort
import InsertionSort




def main():
    array = []
    amount = random.randint(10, 1010)

    for i in range(0, amount):
        array.append(random.randint(0, 1000))

    InsertionSort.insertion_sort(array.copy(), amount)
    BubbleSort.bubble_sort(array.copy(), amount)
    SelectionSort.selection_sort(array.copy(), amount)

main()
