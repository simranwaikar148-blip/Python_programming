#For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool. Display the total prime count for each number.

from multiprocessing import Pool
import math

def count_primes(n):
    count = 0

    for num in range(2, n + 1):
        prime = True

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                prime = False
                break

        if prime:
            count += 1

    return (n, count)

def main():
    numbers = [10000, 20000, 30000, 40000]

    with Pool() as p:
        result = p.map(count_primes, numbers)

    print("Prime Counts:")
    for n, cnt in result:
        print(f"Primes between 1 and {n} = {cnt}")

if __name__ == "__main__":
    main()