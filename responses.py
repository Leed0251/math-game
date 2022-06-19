def get_response(question,availableresponses,prefix):
    print(question)
    response = input(prefix)
    if len(response) > 0:
        # Loops through possible responses and returns it when it matches the users answer
        for i in range(len(availableresponses)):
            if availableresponses[i][0:len(response)] == response.lower():
                return {
                    "success": True, # Return the response
                    "response": availableresponses[i]
                }
                
    # Return the user input being invalid and their response
    return {
        "success": False,
        "response": response
    }