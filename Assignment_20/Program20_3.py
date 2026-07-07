# Create EvenList and OddList threads.
# Display sum of even and odd elements.

import threading

def EvenList(lst):
    even = [i for i in lst if i % 2 == 0]
    print("Even Elements:", even)
    print("Sum of Even Elements:", sum(even))

def OddList(lst):
    odd = [i for i in lst if i % 2 != 0]
    print("Odd Elements:", odd)
    print("Sum of Odd Elements:", sum(odd))

def main():
    n = int(input("Enter number of elements: "))
    lst = []

    print("Enter elements:")
    for i in range(n):
        lst.append(int(input()))

    t1 = threading.Thread(target=EvenList, args=(lst,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(lst,), name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()