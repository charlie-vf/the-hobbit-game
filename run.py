# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def about_game():
    print(
        "Welcome to the Hobbit adventure game!\n"
        "The Dwarves of Erebor are in need of someone to join their quest.\n"
        "They seek to reclaim their home from the terrible dragon, Smaug.\n"
        "This adventure is not for the weak of heart.\n"
    )


def choose_name():
    """
    Asks player to choose a character name
    """
    name_input = input("Please choose a name for your character!")

    print(f"Welcome to the company, {name_input}!")


def main():
    about_game()
    choose_name()

main()