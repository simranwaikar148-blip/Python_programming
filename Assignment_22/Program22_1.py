#Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for every element in the list.

from multiprocessing import Pool

def sum_of_squares(n):
    return sum(i * i for i in range(1, n + 1))

def main():
    numbers = [1000000, 2000000, 3000000, 4000000]

    with Pool() as p:
        result = p.map(sum_of_squares, numbers)

    print("Sum of Squares:")
    for n, ans in zip(numbers, result):
        print(f"{n} -> {ans}")

if __name__ == "__main__":
    main()