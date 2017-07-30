#Bubble Sort

#Randomly Gen an list of numbers:
'''import random
for i in range(0,10):
    array.append(random.randint(0,100))
print(array)'''

array = [11, 87, 79, 54, 12, 5, 72, 25, 56, 28, 99, 5, 45]

def sort(array):
    for a in range(0, len(array)-1):
        if array[a] <= array[a+1] and (a+1) <= len(array):
            pass
        elif array[a] > array[a+1] and (a+1) <= len(array):
            array[a], array[a+1] = array[a+1], array[a]
            print(array)

while True:
    count = len(array)

    for a in range(0, len(array)-1):
        if array[a] <= array[a+1] and (a+1) <= len(array):
            count = count - 1
            if count == 0:
                exit()
            pass
        elif array[a] > array[a+1] and (a+1) <= len(array):
            sort(array)
