# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Oct 2021
# This program asks the user to input an integer for 
# a sum of terms up to the user's integer then shows result


def main():
    # this function loops all terms to the user inputted integer and
    # outputs a result for a comparison to the natural log of 2

    # loop variables
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
