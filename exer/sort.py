import time
import random
import os


def clear_screen():
    os.system("clear")


n = input("no of arrays = ")
n = int(n)
while n > 46:
    n = input("no of elemets must be below 47 = ")
    n = int(n)

s = input("range of number in array = ")
s = int(s)
while s > 190:
    s = input("range must be below 191 = ")
    s = int(s)


stime = time.time()
list = [random.randint(1, s) for _ in range(n)]


def bubble_sort(list):
    length = len(list)
    for ifor in range(length):
        for jfor in range(0, length - ifor - 1):
            if list[jfor] > list[jfor + 1]:
                list[jfor], list[jfor + 1] = list[jfor + 1], list[jfor]

               # time.sleep(0.005)
                clear_screen()
                for ifor in list:
                    print(ifor, "x" * ifor)
                # print(lst)


bubble_sort(list)

clear_screen()
for i in list:
    print(i, "x" * i)
print(list)

etime = time.time()

print(stime)
print(etime - stime)
