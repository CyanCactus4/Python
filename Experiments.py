
from math import sqrt, ceil

par = input("Write a pozitive number: ")

try:
    par = int(par)
except ValueError:
    print("Non-correct value: string")
    exit()
finally:
    par = abs(par)
    print(f"Your number is {par}")

Dividors = [i for i in range(2, par//2+1) if par % i == 0]
Dividors.append(par)
Dividors.insert(0, 1)

print(f"All dividors of a number {par}:")
for i in Dividors: print(i, end =" ")
print()