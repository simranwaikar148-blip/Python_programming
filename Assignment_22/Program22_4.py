#write a program that calculates 1^5 + 2^5 + 3^5 + ... + N^5 for multiple values of N simultanously using Pool. Measure thee total execution time .

from multiprocessing import Pool
import time

def sum_of_powers(n):
    return sum(i ** 5 for i in range(1, n + 1))

def main():
    numbers = [1000000, 2000000, 3000000, 4000000]

    start = time.time()

    with Pool() as p:
        result = p.map(sum_of_powers, numbers)

    end = time.time()

    print("Sum of Powers:")
    for n, ans in zip(numbers, result):
        print(f"{n} -> {ans}")

    print("Execution Time:", end - start, "seconds")

if __name__ == "__main__":
    main()