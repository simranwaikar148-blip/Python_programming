#Write a Python program using multiprocessing.Pool to calculate the sum of all odd numbers from 1 to N.

from multiprocessing import Pool
import os

def sum_odd(n):
    total = sum(i for i in range(1, n + 1, 2))
    return (os.getpid(), n, total)

def main():
    data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as p:
        result = p.map(sum_odd, data)

    for pid, num, total in result:
        print("Process ID :", pid)
        print("Input Number :", num)
        print("Sum of Odd Numbers :", total)
        print()

if __name__ == "__main__":
    main()