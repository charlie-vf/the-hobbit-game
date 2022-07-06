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

    """
    Asks player if they would like to start the game.
    """
    play_game_choice = input("Will you help them? y/n \n").lower()

    if play_game_choice == "y":
        #start_game()
        print("Starting game.\n")
    elif play_game_choice == "n":
        #exit_game()
        print("Exiting game.\n")
    else:
        print("Please enter either y or n.\n")
        play_game()


def weapon_choice():
    """
    Asks player to choose a weapon for their character.
    """

    weapons = [
        "Bow & Arrow",
        "Sword & Shield",
        "Daggers"
        "Greatsword"
    ]
    print(
        "The Dwarves would like to offer you a weapon.\n"
        "Your choices are:\n"
        "a) Bow & Arrow\n"
        "b) Sword & Shield\n"
        "c) Daggers\n"
        "d) Greatsword\n"
    )

    choose_weapon = input("Please choose either a, b, c or d\n")

    if "a" in choose_weapon:
        print(
            "Excellent choice!\n"
            "You are given a dark-stained wood longbow.\n"
            "Sometimes, attacking from afar is the best option.\n"
            )
    elif "b" in choose_weapon:
        print(
            "Excellent choice!\n"
            "You are given a silver sword with intricate gold carving"
            "and a matching shield.\n"
            "With these, you can defend and attack with ease.\n"
        )
    elif "c" in choose_weapon:
        print(
            "Excellent choice!\n"
            "You are given two small daggers with bronze leaf detail.\n"
            "These will allow you to perform amazing sneak attacks.\n"
        )
    elif "d" in choose_weapon:
        print(
            "Excellent choice!\n"
            "You are given a beautiful greatsword with a curved blade.\n"
            "With this, you can perform powerful attacks and do immense damage.\n"
        )
    else:
        print("Please choose either a, b, c or d.\n")
        weapon_choice()


def first_battle():
    print(
        "After travelling through torrential rain, you and the Dwarves"
        "stumble across a run-down farm building. Here, you decide to"
        "take shelter for the night.\n"
        "You join two of the Dwarves, Dwalin and Bifur, to hunt for firewood.\n"
    )

    print(
        "You enter a clearing. It looks like this is a common area for wood"
        "collection - the area is littered with branches and chopped trees.\n"
        "The three of you begin to gather what you can carry.\n"
        "Suddenly, tou hear a rustling over to the east, followed by a low growl"
        "The Dwarves motion for silence and ready their weapons.\n"
        ""
    )

    print(
        "From the other side of the clearing emerge five Orcs and a Warg!\n"
        "The Orcs position themselves, ready to fight.\n"
        "a) One approaches with the Warg, teeth bared.\n"
        "b) One stay in the middle, defending the back line.\n"
        "c) Two remain at the back, shouting viciously.\n"
        "d) One drifts to the side, ducking into the foliage.\n"
    )

    print("It's time to put your new weapon to good use!\n")

    first_battle_choice = input("Which enemy do you target? a, b, c or d \n")


def choose_name():
    """
    Asks player to choose a character name.
    """
    name_input = input("Please choose a name for your character:").capitalize()

    print(f"Welcome to the company, {name_input}! \n")


# def start_game():

# def exit_game():



def main():
    about_game()
    play_game()
    #start_game()
    #exit_game()
    choose_name()
    weapon_choice()

main()