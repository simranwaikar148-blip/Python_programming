# Create two threads EvenFactor and OddFactor.
# Display even factors, odd factors and their sums.

import threading

def EvenFactor(num):
    total = 0
    print("Even Factors:")
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:
            print(i, end=" ")
            total += i
    print("\nSum of Even Factors:", total)

def OddFactor(num):
    total = 0
    print("Odd Factors:")
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 != 0:
            print(i, end=" ")
            total += i
    print("\nSum of Odd Factors:", total)

def main():
    num = int(input("Enter a number: "))

    t1 = threading.Thread(target=EvenFactor, args=(num,), name="EvenFactor")
    t2 = threading.Thread(target=OddFactor, args=(num,), name="OddFactor")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()