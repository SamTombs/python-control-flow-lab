# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

# def print_greeting():
#     # Your code goes here. Remember to indent!
#     python_is_fun = True
#     if python_is_fun:
#         print("Exercise 0 = Python is fun!")

# # Call the function
# print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#


# I can imagine there is a better way to do this.

def check_letter():
    letter = input("Enter a letter (A-Z or a-z)")
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVEWXYZ"
    if letter in vowels:
        print(f"The letter {letter} is a vowel")
    elif letter in consonants:
        print(f"The letter {letter} is a consonant")
    else:
        print("Invalid Input")
    
# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#


def check_voting_eligibility():
    age = input("Enter your age: ")
    voting_age = int(age) >= 16
    if voting_age:
        print("You can vote")
    else:
        print("Sorry you aren't old enough yet")



# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    dog_age = int(input("What is your dog's age: "))
    if dog_age > 2:
        dog_years = dog_age * 7 + 20
        print(f"The dogs age in dog years is {dog_years}")
    elif dog_age <= 2:
        dog_years = dog_age * 10
        print(f"The dogs age in dog years is {dog_years}")
    

# Call the function
calculate_dog_years()


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    is_cold = input("Is it cold (yes/no): ").strip().lower()
    is_raining = input("Is it raining (yes/no): ").strip().lower()

    is_cold = (is_cold == "yes")
    is_raining = (is_raining == "yes")

    if is_cold and is_raining:
        print("Wear a waterproof coat")
    elif is_cold and not is_raining:
        print("Wear a warm coat")
    elif not is_cold and is_raining:
        print("Carry an umbrella")
    elif not is_cold and not is_raining:
        print("Wear light clothing")


# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():

    months = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
        "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
        "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }
   
    month = input("Enter the month of the year (Jan - Dec): ")
    day = int(input("Enter the day of the month: "))

    try:
     month_num = months[month]
    except:
        raise ValueError("Not a month")

    if (month_num == 12 and day >= 21) or (1 <= month_num <= 2) or (month_num == 3 and day <= 19):
        season = "Winter"
    elif (month_num == 3 and day >= 20) or (4 <= month_num <= 5) or (month_num == 6 and day <= 20):
        season = "Spring"
    elif (month_num == 6 and day >= 21) or (7 <= month_num <= 8) or (month_num == 9 and day <= 21):
        season = "Summer"
    elif (month_num == 9 and day >= 22) or (10 <= month_num <= 11) or (month_num == 12 and day <= 20):
        season = "Fall"
    else:
        print("Invalid date entered.")
    
    print(f"{month} {day} is in {season}.")

# Call the function
determine_season()

# Exercise 6: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    target_number = 42  
    max_attempts = 5
    
    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}: Guess a number from 1 to 100: "))

        if guess == target_number:
            print("Congratulations!")
            return
        
        if guess < target_number and not (guess == target_number):
            print("Guess is too low.")
        elif guess > target_number and not (guess == target_number):
            print("Guess is too high.")
    
    print("Mission failed, better luck next time")
    

# Call the function
guess_number()