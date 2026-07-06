#program to accept marks and display grade

def DisplayGrade(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First class")
    elif marks >= 50:
        print("Second class")
    else:
        print("Fail")

def main():
    marks = float(input("Enter marks: "))
    DisplayGrade(marks)

if __name__ == "__main__":
    main()