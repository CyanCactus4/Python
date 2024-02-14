from math import *
par = int(input("Введите положительно число:\t"))

assert(par >= 0)

line = f"Делители числа {par}:\n"
print(line)
for i in range(1, ceil(sqrt(par))+1):
    if par % i == 0:
        print(f"{i}\n")
print(f"{par}\n")
