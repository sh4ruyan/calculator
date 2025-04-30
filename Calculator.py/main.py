import tkinter as tk
# for graphical interface
from tkinter import ttk
# for widgets

# Handle input

def display_menu():

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Fibonacci Sequence")
    print("6. Factorial")
    print("7. Close calculator")


def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return (int)(n1/n2)


def calc_fibonacci_seq(n):
    result = 0

    if n < 0:
        return "Error"

    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    result = calc_fibonacci_seq(n-1) + calc_fibonacci_seq(n-2)

    return result


def calc_factorial(n):
    result = 1
    if n == 0:
        return 1

    for i in range(1, n+1):
        result = result * i

    return result


def take_input(num_of_inputs):
    if num_of_inputs == "one":
        n1 = (int)(input("Please type your number: "))
        return n1
    else:
        n1 = (int)(input("Please type your first number: "))
        n2 = (int)(input("Please type your second number: "))
        return n1, n2


def print_closing_msg():
    print("Thank you for using my calculator! Hope you come back soon :)")


def main():
    print("Hello! Welcome to my very simple calculator :D \n")
    print("Here are some cool operations it can do! ")
    keep_calculating = True

    while keep_calculating:
        display_menu()
        choice_num = (int)(input("Please choose a number from the following options: "))

        if choice_num in [1, 2, 3, 4]:
            n1, n2 = take_input("two")
            match choice_num:
                case 1:
                    result = add(n1, n2)
                case 2:
                    result = subtract(n1, n2)
                case 3:
                    result = multiply(n1, n2)
                case 4:
                    result = divide(n1, n2)

        elif choice_num in [5, 6]:
            n = (take_input("one"))

            match choice_num:
                case 5:
                    result = calc_fibonacci_seq(n)

                case 6:
                    result = calc_factorial(n)

        elif choice_num == 7:
            print_closing_msg()
            exit(0)

        else:
            print("Error. Please choose one of the provided options")
            continue

        # Printing result

        print("Your result is", result, "\n")

        print("Would you like to keep using this amazing calculator?")
        answer = input("Type in yes or no: ")
        answer = answer.lower()
        if answer == "no":
            keep_calculating = False

    print_closing_msg()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
