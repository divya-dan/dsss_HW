import random


def get_random_integer(min_val, max_val):
    """
    Get a random integer within a specified range.
    
    Parameters:
    min_val (int): The minimum value of the range.
    max_val (int): The maximum value of the range.

    Returns:
    int: A random integer within the range [min_val, max_val].
    """
    assert min_val <= max_val, "Minimum value should be less than or equal to the maximum value."

    return random.randint(min_val, max_val)


def get_random_operator():
    """
    Get a random mathematical operator from '+', '-', or '*'.
    
    Returns:
    str: A random operator as a string.
    """
    return random.choice(['+', '-', '*'])


def generate_math_problem(num1, num2, operator):
    """
    Generates a math problem string and calculates the answer based on the operator.
    
    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    operator (str): The operator, which can be '+', '-', or '*'.

    Returns:
    tuple: A tuple containing the problem as a string and the correct answer.
    """
    problem = f"{num1} {operator} {num2}"
    # Calculate the correct answer based on the operator
    
    if operator == '+': 
        answer = num1 + num2
    elif operator == '-': 
        answer = num1 - num2
    else: 
        answer = num1 * num2
    return problem, answer

def math_quiz():
    score = 0 # Initialize the score to 0
    total_questions = 3 # Set the total number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and operator
        num1 = get_random_integer(1, 10)
        num2 = get_random_integer(1, 5)
        operator = get_random_operator()

        problem, correct_answer = generate_math_problem(num1, num2, operator)

        print(f"\nQuestion: {problem}")

        # Input validation and error handling
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue # Skip the rest of the loop and start the next iteration
        
        #check the answer
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")


    # display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
