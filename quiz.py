# Python imports
import time
# File imports
import clear
import colours
import decorate_text
import generate_question
import num_checker
import responses
import summary

import game_info

# Clean the console

clear.clear_console()

# Main routine

user_selected = {"success": False, "response": "No data yet"}
error = ""

# Repeat until the user says they want to quit
while user_selected["response"] != "quit":
    # Display text for input
    user_selected = responses.get_response(

        colours.colour_green(decorate_text.Decorate_text("#","Welcome to math quiz").surround(4,1))+
        colours.colour_gray("\nYour options:\n")+
        colours.colour_blue("  Information\n")+
        colours.colour_green("  Play\n")+
        colours.colour_red("  Quit"),
        # Allowed inputs
        ["information","play","quit"],
        # Text before user input line
    error
)
    if user_selected["success"] == False: # Checks if the user has typed something valid.
        clear.clear_console()
        if len(user_selected["response"]) > 0: # Checks if the user has typed anything at all.
            error = colours.colour_yellow('"{}" is not an option '.format(user_selected["response"])) # Tells the user they typed an invalid response
        else:
            error = colours.colour_yellow("Please type something ") # Tells the user to type something.
    else:
        error = ""
        if user_selected["response"] == "information":
            clear.clear_console()
            print("""
Upon entering the game, you will be given a \033[1m{}\033[0m\n
{}\n
You are only given \033[1m{}\033[0m attempts to guess correctly before you move on to the next question.\n
Higher difficulties can give \033[1m{}\033[0m but can also add different operations.\n
{} contains \033[1m(+,-)\033[0m while {} includes everything in easy along with \033[1m* and /.\033[0m\n
Every \033[1m{}\033[0m answer will increase the difficulty by \033[1m1\033[0m and every \033[1m{}\033[0m answer will decrease it by \033[1m2\033[0m
            """.format(colours.colour_purple("random math related question."),colours.colour_green("These questions must be answered correctly."),colours.colour_purple("3"),colours.colour_red("Higher numbers"),colours.colour_green("Easy"),colours.colour_orange("Medium"),colours.colour_green("correct"),colours.colour_red("incorrect")))

            input(colours.colour_gray("Press <enter> to continue to main screen\n"))

            clear.clear_console()
        if user_selected["response"] == "play": # Checks if the user wants to play.
            clear.clear_console() # Clean console
            repeat = num_checker.number_checker(
                colours.colour_orange("How many questions would you like to answer\n"), # Text over input box
                "{}\n{} ".format(colours.colour_green("Whole number higher or equal to 1"),colours.colour_gray("or press enter for continuous")), # Text before input box
                1, float("infinity"), # low,high
                True # Allow infinity
            )
            difficulty = { # Initialize difficulty variable
                "success": False,
                "response": ""
            }
            while difficulty["success"] == False: # Repeat until user input is valid
                # Ask the user for their desired difficulty
                difficulty = responses.get_response(
                    colours.colour_orange("What difficulty would you like to play?\n\n")+
                    colours.colour_gray("Your options:\n")+
                    colours.colour_green("  Easy\n")+
                    colours.colour_yellow("  Medium\n")+
                    colours.colour_orange("  Hard\n")+
                    colours.colour_red("  Very Hard\n"),
                    
                    ["easy","medium","hard","very hard"],
                    ""
                )
                if difficulty["response"] == "very hard":
                    difficulty["response"] = "very_hard"
                clear.clear_console()
            games_played = 0
            # Sets selected_game_info to the selected difficulty
            selected_game_info = getattr(game_info, "{}_game".format(difficulty["response"]))
            if selected_game_info:
                game_history = []
                while games_played < repeat:
                    
                    games_played += 1
                    # generates random question to ask
                    question = generate_question.generate(
                        selected_game_info["low"],
                        selected_game_info["high"],
                        selected_game_info["number_count"],
                        selected_game_info["operations"]
                    )
                    # Display round number
                    # If not playing continuous, show how many games are left to play
                    if repeat == float("infinity"):
                        print(colours.colour_green("Question #{}".format(games_played)))
                    else:
                        print(colours.colour_green("Question {} / {}".format(games_played,repeat)))
                    user_correct = num_checker.answer_checker(question["question"],question["answer"])
                    # If the user wants to quit
                    if user_correct == "xxx":

                        games_played = repeat
                        clear.clear_console()

                    else:
                        # Increases and decreases difficulty if answer is correct or not
                        if user_correct["status"] == "correct":
                            selected_game_info["high"] += 2
                            selected_game_info["low"] += 1

                        else:

                            if selected_game_info["low"] > 1:
                                selected_game_info["high"] -= 4
                                selected_game_info["low"] -= 2

                        game_history.append(user_correct)
                        
                # End game summary will go here
                print(colours.colour_green(decorate_text.Decorate_text("#", "End game summary").surround(2,1)))
                summary.display_summary(game_history)
                input(colours.colour_gray("Press <enter> to continue to main screen\n"))
                clear.clear_console()
                
# Thank the user for playing the game
clear.clear_console()
print(colours.colour_purple("Thank you for playing"))
time.sleep(1.5)