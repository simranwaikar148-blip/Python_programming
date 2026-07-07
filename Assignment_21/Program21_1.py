# Design a Python application that creates two threads named Prime and NonPrime to display prime and non-prime numbers.

import threading

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def Prime(lst):
    print("Prime Numbers:")
    for i in lst:
        if isPrime(i):
            print(i, end=" ")
    print()

def NonPrime(lst):
    print("Non-Prime Numbers:")
    for i in lst:
        if not isPrime(i):
            print(i, end=" ")
    print()

def main():
    n = int(input("Enter number of elements: "))
    lst = []

    print("Enter elements:")
    for i in range(n):
        lst.append(int(input()))

    t1 = threading.Thread(target=Prime, args=(lst,), name="Prime")
    t2 = threading.Thread(target=NonPrime, args=(lst,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()