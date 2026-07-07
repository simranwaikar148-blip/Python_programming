#Write a program which contains filter(), map() and reduce(). Accept a list of numbers from the user. Filter all prime numbers. Multiply each prime number by 2 using map(). Return the maximum number using reduce().

from functools import reduce

def isPrime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def main():
    n = int(input("Enter number of elements: "))
    lst = []

    print("Enter elements:")
    for i in range(n):
        lst.append(int(input()))

    filtered = list(filter(isPrime, lst))
    mapped = list(map(lambda x: x * 2, filtered))
    result = reduce(lambda x, y: x if x > y else y, mapped)

    print("Input List:", lst)
    print("List after filter:", filtered)
    print("List after map:", mapped)
    print("Output of reduce:", result)

if __name__ == "__main__":
    main()