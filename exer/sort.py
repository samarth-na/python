import time
import random
import os


def clear_screen():
    os.system("clear")


numberOfArray = input("no of arrays = ")
numberOfArray = int(numberOfArray)
# while numberOfArray > 46:
#     numberOfArray = input("no of elemets must be below 47 = ")
#     numberOfArray = int(numberOfArray)


rangeOfNumber = input("range of number in array = ")
rangeOfNumber = int(rangeOfNumber)

# while rangeOfNumber > 190:
#     rangeOfNumber = input("range must be below 191 = ")
#     rangeOfNumber = int(rangeOfNumber)


stime = time.time()

list = [random.randint(1, rangeOfNumber) for _ in range(numberOfArray)]


def bubble_sort(list):
    length = len(list)
    for ifor in range(length):
        for jfor in range(0, length - ifor - 1):
            if list[jfor] > list[jfor + 1]:
                list[jfor], list[jfor + 1] = list[jfor + 1], list[jfor]

                time.sleep(0.005)
                clear_screen()
                for ifor in list:
                    print(ifor, "x" * ifor)
                # print(lst)


bubble_sort(list)

