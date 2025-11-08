# Lab10
# Student Name: JEONGHO KIM
# Student ID: 202337619

import sys

number = int(sys.argv[1])

for i in range(1, number + 1):
    if number % i == 0:

        print(i, end=" ")

print()
