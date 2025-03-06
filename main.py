"""
Main script for the string shift exercise.
"""

WELCOME_MSG = "Hi. Welcome to String Shift\
    \n\nThis program will take a string input x and an integer input y then shift the string to the right by y places.\n"


def get_first_input() -> str:
    """Get first input.

    Returns:
        str: Non-empty string <= 20 characters.
    """

    PROMPT = "Please enter a string <= 20 characters in length: "

    while True:
        s = input(PROMPT)
        if not s or s == "":
            print("The input is empty. Please try again.\n")
        elif len(s) > 20:
            print("The input is greater than 20 characters. Please try again.\n")
        else:
            break

    return s


def get_second_input() -> int:
    """Get second input.

    Returns:
        int: A positive integer between 0 and 50, inclusive.
    """
    PROMPT = "Please enter an integer between 0 and 50, inclusive: "

    while True:
        n = input(PROMPT)
        if not n or n == "":
            print("The input is empty. Please try again.\n")
        elif not n.isdigit():
            print("The input is not a positive integer. Please try again.\n")
        elif int(n) > 50:
            print("The input must be between 0 and 50, inclusive. Please try again.\n")
        else:
            break

    return int(n)


def shift():
    """Main shift function
    """

    while True:
        print(WELCOME_MSG)
        s = get_first_input()
        n = get_second_input()

        i = 0
        while i < n:
            s = s[-1] + s[0:-1]
            i += 1

        print(f'\nYour string [{s}], shifted [{n}] places: [{s}]')

        if input("\nWould you like to try again? (y): ").lower() != 'y':
            break


def main():
    shift()


if __name__ == "__main__":
    main()
