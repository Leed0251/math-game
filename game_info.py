import generate_question
# Multiple dictionaries on game difficulties

# Generate questions with + - operators and 2 random numbers between 1 and 10
easy_game = {
    "operations": ["+", "-"],
    "low": 1,
    "high": 10,
    "number_count": 2
}

# Generate questions with + - / x operators and 2 random numbers between 1 and 10
medium_game = {
    "operations": ["+", "-", "/", "*"],
    "low": 1,
    "high": 10,
    "number_count": 2
}

# Generate questions with + - / x operators and 3 random numbers between 1 and 15
hard_game = {
    "operations": ["+", "-", "/", "*"],
    "low": 1,
    "high": 15,
    "number_count": 3
}

# Generate questions with + - / x operators and 4 random numbers between 1 and 25
very_hard_game = {
    "operations": ["+", "-", "/", "*"],
    "low": 1,
    "high": 25,
    "number_count": 4
}