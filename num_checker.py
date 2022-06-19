import colours
import time
import clear

def number_checker(question, prefix, low, high, allow_infinity):
    try:

        print(question)
        chosen_number = input(prefix)
        clear.clear_console()

        if chosen_number == "": # Checks if user wanted infinity
            return float("infinity")

        chosen_number = int(chosen_number)

        if low <= chosen_number <= high: # Checks if input is in range

            return chosen_number

        else:
            print(colours.colour_yellow("Please enter a whole number between {} and {}.".format(low, high)))
            return number_checker(question, prefix, low, high, allow_infinity) # Ask the question again

    except:
        
        print(colours.colour_yellow("Please enter a valid whole number"))
        return number_checker(question, prefix, low, high, allow_infinity) # Ask the question again


def answer_checker(question,answer):
    # Error function
    def error():
        clear.clear_console()
        print("Please enter a valid whole number")
        return answer_checker(question,answer)

    try:

        attempt_number = 0
        # Loop until user is out of turns
        while attempt_number < 3:

            print(question)
            chosen_number = input(colours.colour_yellow("\nYou can type xxx to quit")+"\nAnswer here: ")

            if chosen_number == "":
                return error()
            if chosen_number == "xxx":
                return chosen_number

            chosen_number = int(chosen_number)
            attempt_number += 1
            # User question feedback
            if chosen_number == answer:

                clear.clear_console()
                print(colours.colour_green("You got it correct!"))
                time.sleep(2)
                clear.clear_console()

                return {
                    "question": question,
                    "attempts": attempt_number,
                    "status": "correct"
                }

            # Says the user is incorrect unless it is the last turn
            elif attempt_number < 3:
                clear.clear_console()
                print(colours.colour_orange("Incorrect, try again"))
                time.sleep(2)
                clear.clear_console()

        clear.clear_console()
        # Tells user the correct answer and waits 2 seconds
        print(colours.colour_red("The answer was {}, let's try another question".format(answer)))
        time.sleep(2)
        clear.clear_console()
        # Returns question information
        return {
            "question": question,
            "attempts": attempt_number,
            "status": "incorrect"
        }

    except:

        return error()