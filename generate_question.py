import random

def generate(low,high,number_count,operations):
    answer = -1
    answer = -1
    while answer < 0:
        removed_operations = []
        numbers = []
        divided = False
        # Loops for each number in the operation
        for i in range(number_count):
            
            number = random.randint(low,high) # Generate a random number

            if divided != False: # Checks if there was a division sum
                numbers.append(divided)
            else:
                numbers.append(number)

            if i != number_count-1:
                
                op = random.choice(operations)
                while op in numbers:
                    op = random.choice(operations)
                
                if op == "/":
                    # Creates random number to divide and replace to random number
                    divided = random.randint(low,high)
                    newnumber = number * divided
                    numbers.pop()
                    numbers.append(newnumber)

                numbers.append(op) # Creates operation

        question = "".join([str(item) for item in numbers]) # Print all the items in the table as a string
        answer = eval(question)
    
    return { # Returns table of the question string and answer
        "question": question,
        "answer": int(answer)
    }