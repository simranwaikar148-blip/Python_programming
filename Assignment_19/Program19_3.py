#Write a program which contains filter(), map() and reduce(). Accept a list of numbers from the user. Filter numbers greater than or equal to 70 and less than or equal to 90. Increase each filtered number by 10 using map(). Return the product of all mapped numbers using reduce().

from functools import reduce

filtered = list(filter(lambda x: 70 <= x <= 90, list))
mapped = list(map(lambda x: x + 10,filtered))
result = reduce(lambda x, y: x * y,mapped)


def main():
    n = int(input("Enter number of elements: "))
    list = []

    print("Enter elements: ")
    for i in range(n):
        list.append(int(input()))

    print("Input List:",list)
    print("List after filter:",filtered)
    print("List after map:",mapped)
    print("Output of reduce:",result)
    



if __name__ == "__main__":
    main()