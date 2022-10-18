#!/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/10/18
# Takes the user input for whether the user is rich
# Or good looking and determines whether the user
# Would be eligible to date the program's grandchild.


def main():

    # Title of the program
    print("Dating Game: Can you date my grandchild?")

    # Explanation
    print("Please answer 1 for yes and 0 for no:")

    # User inputs for the questions
    rich_answer = input("Are you at least moderately rich?: ")
    looks_answer = input("are you VERY good looking??: ")

    # Try Catch statement to make sure the guess is an integer
    try:
        rich_integer = int(rich_answer)
        looks_integer = int(looks_answer)

    # Exception which tells the user to enter an integer
    except Exception:
        print("Please enter an integer.")

    else:
        # If the input is not 1 or 0
        if (
            rich_integer != 1
            and rich_integer != 0
            or looks_integer != 1
            and looks_integer != 0
        ):
            print("That is not an input of 1 or 0. Try again!")

        else:

            # IF statement for if the user is rich or good looking
            if rich_integer == 1 or looks_integer == 1:
                print("You are allowed to date my grandchild. You passed!")

            # ELSE statement if the user answers no to both questions
            else:
                print(
                    "Apologies, but you have not met my standards. You cannot "
                    "date my grandchild!"
                )


if __name__ == "__main__":
    main()
