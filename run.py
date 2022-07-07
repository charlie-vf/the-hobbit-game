# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import sys
import random
import time

inventory = []

# slowprint tutorial taken from Slack Overflow - info in ReadMe
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(random.random() * 0.1)

def about_game():
    slowprint(
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
        slowprint("Amazing! Let's begin...\n")
    elif play_game_choice == "n":
        slowprint("Okay! Maybe another time...\n")
        sys.exit()
    else:
        slowprint("Please enter either y or n.\n")
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
    slowprint(
        "The Dwarves would like to offer you a weapon.\n"
        "Your choices are:\n"
        "a) Bow & Arrow\n"
        "b) Sword & Shield\n"
        "c) Daggers\n"
        "d) Greatsword\n"
    )

    choose_weapon = input("Please choose either a, b, c or d\n").lower()

    if "a" in choose_weapon:
        slowprint(
            "Excellent choice!\n"
            "You are given a dark-stained wood longbow.\n"
            "Sometimes, attacking from afar is the best option.\n"
            "Bow & Arrow was added to your inventory.\n"
            )
        add_to_inventory("Bow & Arrow")
    elif "b" in choose_weapon:
        slowprint(
            "Excellent choice!\n"
            "You are given a silver sword with intricate gold carving"
            "and a matching shield.\n"
            "With these, you can defend and attack with ease.\n"
            "Sword & Shield was added to your inventory.\n"
        )
        add_to_inventory("Sword & Shield")
    elif "c" in choose_weapon:
        slowprint(
            "Excellent choice!\n"
            "You are given two small daggers with bronze leaf detail.\n"
            "These will allow you to perform amazing sneak attacks.\n"
            "Daggers were added to your inventory.\n"
        )
        add_to_inventory("Daggers")
    elif "d" in choose_weapon:
        slowprint(
            "Excellent choice!\n"
            "You are given a beautiful greatsword with a curved blade.\n"
            "With this, you can perform powerful attacks and do immense damage.\n"
            "Greatsword was added to your inventory.\n"
        )
        add_to_inventory("Greatsword")
    else:
        print("Please choose either a, b, c or d.\n")
        weapon_choice()


def first_battle():
    slowprint(
        "After travelling through torrential rain, you and the Dwarves "
        "stumble across a run-down farm building. Here, you decide to "
        "take shelter for the night.\n"
        "You join two of the Dwarves, Dwalin and Bifur, to hunt "
        "for firewood.\n"
    )

    slowprint(
        "You enter a clearing. It looks like this is a common area for wood "
        "collection - the area is littered with branches and chopped trees.\n"
        "The three of you begin to gather what you can carry.\n"
        "Suddenly, you hear a rustling over to the east, followed by a "
        "low growl."
        "The Dwarves motion for silence and ready their weapons.\n"
        ""
    )

    slowprint(
        "From the other side of the clearing emerge five Orcs and a Warg!\n"
        "The Orcs position themselves, ready to fight.\n"
        "a) One approaches with the Warg, teeth bared.\n"
        "b) One stays in the middle, defending the back line.\n"
        "c) Two remain at the back, shouting viciously.\n"
        "d) One drifts to the side, ducking into the foliage.\n"
    )

    slowprint("It's time to put your new weapon to good use!\n")

    first_battle_choice = input("Which enemy do you target? a, b, c or d \n").lower()

    if "a" in first_battle_choice and "Sword & Shield" in inventory:
        slowprint(
            "You ready a defensive stance in front of the Dwarves.\n"
            "The Orc and Warg attack, but you successfully deflect them "
            "with your shield.\n"
            "Phew! That's two down, and the Dwarves have dealt "
            "with the rest!\n"
        )
    
    elif "a" in first_battle_choice and "Sword & Shield" not in inventory:
        slowprint(
            "Oh no! Your chosen weapon is not suitable for this type "
            "of combat.\n"
            "The Orc and Warg attack, forcing you to fall back.\n"
            "Luckily, Dwalin stops them before they can kill any of you.\n"
        )
        add_to_inventory("Injury1")

    elif "b" in first_battle_choice and "Greatsword" in inventory:
        slowprint(
            "You charge past the first Orc and Warg to the Orc "
            "in the middle.\n"
            "Letting loose a cry, you swing your greatsword "
            "down on the enemy.\n"
            "Success! The Orc is severely wounded. It retreats "
            "back into the forest.\n"
        )
    
    elif "b" in first_battle_choice and "Greatsword" not in inventory:
        slowprint(
            "Oh no! The Orc deflects your attack, knocking you back.\n"
            "You take cover, reassessing the situation as the Dwarves "
            "counterattack.\n"
        )
        add_to_inventory("Injury1")

    elif "c" in first_battle_choice and "Bow & Arrow" in inventory:
        slowprint(
            "You ready your bow, drawing back the string and letting loose "
            "an arrow.\n It sails past the first two Orcs and the Warg, "
            "finding its mark in one of the Orcs at the back.\n You "
            "repeat the action, taking down the second Orc as well."
        )
    
    elif "c" in first_battle_choice and "Bow & Arrow" not in inventory:
        slowprint(
            "You charge towards the enemies at the back, but they see you "
            "coming, loosing their own arrows.\n You narrowly escape the "
            "flying blades and are forced to retreat.\n"
        )
        add_to_inventory("Injury1")
    
    elif "d" in first_battle_choice and "Daggers" in inventory:
        slowprint(
            "You crouch, taking a wide birth to sneak up on the hidden Orc.\n"
            "They don't see you coming, and you successfully land a hit!\n"
            "Nice, that's one down! Bifur and Dwalin can deal with the rest.\n"
        )
    
    elif "d" in first_battle_choice and "Daggers" not in inventory:
        slowprint(
            "It's difficult to crouch with your weapon ready, and you stumble, "
            "alerting the hidden Orc to your approach.\n They spring from the "
            "foliage, charging at you.\n Time to retreat back behind "
            "the Dwarves!\n"
        )
        add_to_inventory("Injury1")
    
    else:
        slowprint("Please choose either a, b, c or d \n")
        first_battle()


def post_first_battle():
    slowprint(
        "The three of you return to the others and tell of your encounter "
        "with the Orcs. They are all concerned by the proximity of the enemy "
        "and decide to vote on whether to move on, despite night falling, "
        "or continue to set up camp and stay here for the night."
    )

    post_first_battle_choice = input("Do you vote to move on? y/n\n")

    if post_first_battle_choice == "y":
        slowprint(
            "You and the company quickly gather all your supplies, "
            "keeping an ear out for any sounds from the forest.\n"
            "You form a protective huddle, and together push forward "
            "through the forest."
        )
    
    elif post_first_battle_choice == "n":
        slowprint(
            "The company votes to stay. A couple of hours into the night, "
            "the forest becomes alive with growls and sounds of movement.\n"
            "Before any of you can prepare, a hoard of Orcs and Wargs emerges "
            "and attacks!\n"
            "Game Over!"
        )
        sys.exit()
    
    else:
        slowprint("Please choose either y or n. \n")
        post_first_battle()

def second_battle():
    slowprint(
        "You make it safely through the night"
    )
    if "Injury1" in inventory:
        slowprint(
            "However, the injury you sustained in battle slows you down."
        )
    else:
        slowprint(
            "Perhaps this adventuring business isn't too difficult, after all."
        )
    
    slowprint(
        "You continue along the path, but are soon stopped by a powerfully "
        "flowing river.\n"
        "In your packs, you each carry a bundle of rope.\n"
        "One of the Dwarves points out a large tree which could be used "
        "to affix the rope, allowing you all to move across.\n"
    )
    
    second_battle_choice = input("Do you take the lead here, or let one of the others try first? y/n \n").lower()
    
    if second_battle_choice == "y" and "Bow & Arrow" in inventory and "Injury1" in inventory:
        slowprint(
            "You wind the rope securely around an arrow and aim it at the tree...\n"
            "But your injury jars you at the last second...\n"
            "The arrow lands in the tree, anyway, so you begin to climb across...\n"
            "But oh no! The arrow wasn't deep enough in the tree and it dislodges, "
            "dropping you into the raging river below. \n"
            "Game Over!"
        )
        sys.exit()
    
    elif second_battle_choice == "y" and "Bow & Arrow" in inventory:
        slowprint(
            "You wind the rope securely around an arrow and aim it at the tree...\n"
            "Success! Your arrow stuck! You tie the other end round a tree "
            "near you and begin to climb across...\n"
            "The others soon follow.\n"
        )
    elif second_battle_choice == "y" and "Bow & Arrow" not in inventory:
        slowprint(
            "Interesting, do you plan to hurl your blade across the river at the tree?\n"
            "Needless to say, that won't work.\n"
            "Game Over!"
        )
        sys.exit()
    else:
        slowprint(
            "It was a wise decision to let an archer take this task.\n"
            "Kili successfully lands an arrow in the tree and, after tying "
            "the other end around a nearby tree, you all safely reach the "
            "other side!"
        )




def choose_name():
    """
    Asks player to choose a character name.
    """
    name_input = input("Please choose a name for your character: ").capitalize()

    slowprint(f"\nWelcome to the company, {name_input}! \n")

def add_to_inventory(item):
    inventory.append(item)
    print(inventory)

# def start_game():

# def exit_game():



def main():
    about_game()
    play_game()
    #start_game()
    #exit_game()
    choose_name()
    weapon_choice()
    first_battle()
    post_first_battle()
    second_battle()

main()