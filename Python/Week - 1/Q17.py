##Create a list with 8 random integers between 1–100. Find and print:
##the biggest number, the smallest number (without using max() / min() functions – use loop and variables).

import random   
list = [random.randint(1, 100) for i in range(8)]
print(list)
j = list[0]
for i in list:
    if i > j:
        j = i
print("The biggest number is:", j)
k = list[0]
for i in list:
    if i < k:
        k = i   
print("The smallest number is:", k)


