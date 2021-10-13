# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Oct 2021
# This program asks the user to pick a number of integers
# and sums all of those integers


import math


def main():
    # this function loops a sum of inputted positive integers
    # and eliminates the negatives from the sum if the user enters
    # a negative integer

    # loop variable
    start_point = 1
    inverse_operation = -1
    sum = 0

    # input
    user_number = input("Enter in a positive integer: ")
    print("")

    # process & output
    try:

        user_number_int = int(user_number)

        for start_point in range(user_number_int):
            inverse_operation *= -1
            sum += inverse_operation * 1 / user_number_int
            user_number_int = user_number_int - 1

        if sum < 0:
            revised_sum = sum * -1
        else:
            revised_sum = sum * 1

        print("The natural logarithm of 2 is around 0.69314718056...")
        print("")
        print("The Log 2 with your amount of terms is: {0}".format(revised_sum))

    except Exception:
        print("That is an invalid integer.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
