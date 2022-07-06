import colours

def display_summary(info_table):
    if len(info_table) > 0:
        
        full_string = ""
        # Loop through table and give index value
        for index,value in enumerate(info_table):
            # Create string in variable to speed up the process of showing the user
            full_string += colours.colour_green("\n----- Round {} -----\n".format(index+1))

            full_string += (

                colours.colour_gray("question: \033[1m{}\n".format(value["question"]))+
                colours.colour_green("answer: \033[1m{}\n".format(int(eval(value["question"]))))+
                colours.colour_red("attempts made: \033[1m{}\n".format(value["attempts"]))+
                colours.colour_yellow("\033[1m{}\n".format(value["status"]))

            )
        # Print the final string
        print(full_string)
    else:
        print(colours.colour_red("No round data :("))