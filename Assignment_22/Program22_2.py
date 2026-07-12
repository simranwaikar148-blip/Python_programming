#Write a program that calculates factorials of multiple numbers simultaneously using Pool.map(). Display Process ID, Input Number, and Factorial.

from multiprocessing import Pool
import math
import os

def factorial_data(n):
    return (os.getpid(), n, math.factorial(n))

def main():
    numbers = [10, 15, 20, 25]

    with Pool() as p:
        result = p.map(factorial_data, numbers)

    print("Process ID\tInput\tFactorial")
    for pid, num, fact in result:
        print(f"{pid}\t\t{num}\t{fact}")

if __name__ == "__main__":
    main()