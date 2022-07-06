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

def play_game():
    play_game_choice = input("Will you help them? y/n \n").lower()

    if play_game_choice == "y":
        #start_game()
        print("Starting game.\n")
    elif play_game_choice == "n":
        #exit_game()
        print("Exiting game.\n")
    else:
        print("Please enter either y or n.\n")


def choose_name():
    """
    Asks player to choose a character name
    """
    name_input = input("Please choose a name for your character:").capitalize()

    print(f"Welcome to the company, {name_input}! \n")



def main():
    about_game()
    play_game()
    choose_name()

main()