# Create two threads to calculate the sum and product of elements in a list.

import threading

sum_result = 0
product_result = 1

def Sum(lst):
    global sum_result
    sum_result = sum(lst)

def Product(lst):
    global product_result
    product_result = 1
    for i in lst:
        product_result *= i

def main():
    global sum_result, product_result

    n = int(input("Enter number of elements: "))
    lst = []

    print("Enter elements:")
    for i in range(n):
        lst.append(int(input()))

    t1 = threading.Thread(target=Sum, args=(lst,))
    t2 = threading.Thread(target=Product, args=(lst,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of Elements:", sum_result)
    print("Product of Elements:", product_result)

if __name__ == "__main__":
    main()