#Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.Pool.

from multiprocessing import Pool
import math
import os

def factorial_number(n):
    fact = math.factorial(n)
    return (os.getpid(), n, fact)

def main():
    data = [10, 15, 20, 25]

    with Pool() as p:
        result = p.map(factorial_number, data)

    for pid, num, fact in result:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Factorial :", fact)
        print()

if __name__ == "__main__":
    main()