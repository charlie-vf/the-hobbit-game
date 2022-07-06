# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def choose_name():
    """
    Asks player to choose a character name
    """
    name_input = input("Please choose a name for your character!")

    print(f"Welcome to the company, {name_input}!")

    choose_name()