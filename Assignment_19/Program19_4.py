#Write a program which contains filter(), map() and reduce(). Accept a list of numbers from the user. Filter even numbers. Find the square of each even number using map(). Return the addition of all squared numbers using reduce().



from functools import reduce

def main():
    n = int(input("Enter number of elements: "))
    lst = []

    print("Enter elements:")
    for i in range(n):
        lst.append(int(input()))

    filtered = list(filter(lambda x: x % 2 == 0, lst))
    mapped = list(map(lambda x: x ** 2, filtered))
    result = reduce(lambda x, y: x + y, mapped)

    print("Input List:", lst)
    print("List after filter:", filtered)
    print("List after map:", mapped)
    print("Output of reduce:", result)

if __name__ == "__main__":
    main()