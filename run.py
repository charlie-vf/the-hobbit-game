"""
Imports
"""
import sys
import random
import time
import os


inventory = []
WEAPONS = []


# CONSTS

INJURY_DIALOGUE = "You have sustained an injury. \n"

SENSIBLE_DIALOGUE = "You have gained the sensible attribute. \n"

COWARDLY_DIALOGUE = "You have gained the cowardly attribute. \n"

FOOL_DIALOGUE = "You have gained the fool attribute. \n"


def slowprint(s):
    """
    Formats print statements to print one letter at a time after a delay
    Tutorial taken from slack overflow - credits in ReadMe
    """
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.12)


def about_game():

    """
    Welcome message and option for instructions
    """
    slowprint(
        "Welcome to the Hobbit adventure game!\n"
        "The Dwarves of Erebor are in need of someone to join their quest.\n"
        "They seek to reclaim the key to the Misty Mountain \n"
        "so they can take their home back from the dragon, Smaug... \n"
        "This adventure is not for the weak of heart.\n"
    )
    game_instructions = input("Would you like some instructions? y/n \n")
    if game_instructions == "y":
        slowprint(
            "\n"
            "Throughout the game, you will be presented with a number of \n"
            "choices... \n"
            "Some will be ABCD - please type either a b c or d... \n"
            "Other choices will be yes/no (y/n)... \n"
            "y will always refer to the first choice presented... \n"
            "n will always refer to the second choice presented... \n"
            "Read the content carefully, and make decisions based on "
            "previous answers...\n"
            "You have three health points. If you choose poorly three \n"
            "times, the game will be over...\n"
            "Some responses will result in immediate game over... \n"
        )
    elif game_instructions == "n":
        slowprint(
            "\n"
            "Okay!\n"
        )
    else:
        yn_error()
        about_game()


def play_game():

    """
    Asks player if they would like to start the game.
    """

    play_game_choice = input("Will you help them? y/n \n").lower()

    if play_game_choice == "y":
        slowprint("\nAmazing! You're going on an adventure...\n")
    elif play_game_choice == "n":
        slowprint("\nOkay! Maybe another time...\n")
        game_over()
    else:
        yn_error()
        play_game()


def weapon_choice():

    """
    Asks player to choose a weapon for their character.
    """

    global WEAPONS
    WEAPONS = [
        "a) Bow & Arrow",
        "b) Sword & Shield",
        "c) Daggers",
        "d) Greatsword"
    ]
    slowprint(
        "The Dwarves would like to offer you a weapon.\n"
        "Your choices are:\n"
        f"{', '.join(WEAPONS)}"
    )

    choose_weapon = input("Please choose either a, b, c or d\n").lower()

    if "a" in choose_weapon:
        slowprint(
            "\nExcellent choice!\n"
            "You are given a dark-stained wood longbow. \n"
            "Sometimes, attacking from afar is the best option. \n"
            "Bow & Arrow was added to your inventory. \n"
            )
        WEAPONS = "Bow & Arrow"
        add_to_inventory("Bow & Arrow")
    elif "b" in choose_weapon:
        slowprint(
            "\nExcellent choice! \n"
            "You are given a silver sword with intricate gold carving \n"
            "and a matching shield. \n"
            "With these, you can defend and attack with ease. \n"
            "Sword & Shield was added to your inventory. \n"
        )
        WEAPONS = "Sword & Shield"
        add_to_inventory("Sword & Shield")
    elif "c" in choose_weapon:
        slowprint(
            "\nExcellent choice!\n"
            "You are given two small daggers with bronze leaf detail. \n"
            "These will allow you to perform amazing sneak attacks. \n"
            "Daggers were added to your inventory. \n"
        )
        WEAPONS = "Daggers"
        add_to_inventory("Daggers")
    elif "d" in choose_weapon:
        slowprint(
            "\nExcellent choice!\n"
            "You are given a beautiful greatsword with a curved blade. \n"
            "With this, you can perform powerful attacks and do immense "
            "damage. \n"
            "Greatsword was added to your inventory. \n"
        )
        WEAPONS = "Greatsword"
        add_to_inventory("Greatsword")
    else:
        abcd_error()
        weapon_choice()


def first_battle():
    """
    Runs First Battle & asks player to choose an option
    """
    slowprint(
        "After travelling through torrential rain, you and the Dwarves \n"
        "stumble across a run-down farm building. Here, you decide to \n"
        "take shelter for the night. \n"
        "You join two of the Dwarves, Dwalin and Bifur, to hunt \n"
        "for firewood. \n"
    )

    slowprint(
        "You enter a clearing. It looks like this is a common area for wood \n"
        "collection - the area is littered with branches and chopped trees. \n"
        "The three of you begin to gather what you can carry.\n"
        "Suddenly, you hear a rustling over to the east, followed by a \n"
        "low growl. \n"
        "The Dwarves motion for silence and ready their weapons.\n"
        ""
    )

    slowprint(
        "From the other side of the clearing emerge five Orcs and a Warg! \n"
        "The Orcs position themselves, ready to fight. \n"
        "a) One approaches with the Warg, teeth bared. \n"
        "b) One stays in the middle, defending the back line. \n"
        "c) Two remain at the back, shouting viciously. \n"
        "d) One drifts to the side, ducking into the foliage. \n"
    )

    slowprint("It's time to put your new weapon to good use! \n")

    first_battle_choice = input(
        "Which enemy do you target? a, b, c or d \n"
        ).lower()

    if "a" in first_battle_choice and "Sword & Shield" in inventory:
        slowprint(
            "\nYou ready a defensive stance in front of the Dwarves. \n"
            "The Orc and Warg attack, but you successfully deflect them "
            "with your shield. \n"
            "Phew! That's two down, and the Dwarves have dealt "
            "with the rest! \n"
        )

    elif "a" in first_battle_choice and "Sword & Shield" not in inventory:
        slowprint(
            "\nOh no! Your chosen weapon is not suitable for this type "
            "of combat. \n"
            "Your lack of defense allows the Orc and Warg to attack, \n"
            "forcing you to fall back. \n"
            "Luckily, Dwalin stops them before they can kill any of you. \n"
            f"{INJURY_DIALOGUE}"
        )
        add_to_inventory("Orc Injury")

    elif "b" in first_battle_choice and "Greatsword" in inventory:
        slowprint(
            "\nYou charge past the first Orc and Warg to the Orc \n"
            "in the middle. \n"
            "Letting loose a cry, you swing your greatsword "
            "down on the enemy. \n"
            "Success! The Orc is severely wounded. It retreats \n"
            "back into the forest. \n"
        )

    elif "b" in first_battle_choice and "Greatsword" not in inventory:
        slowprint(
            "\nOh no! Your chosen weapon is not suitable for this type "
            "of combat. \n"
            "The Orc deflects your attack, knocking you back. \n"
            "You take cover, reassessing the situation as the Dwarves "
            "counterattack. \n"
            f"{INJURY_DIALOGUE}"
        )
        add_to_inventory("Orc Injury")

    elif "c" in first_battle_choice and "Bow & Arrow" in inventory:
        slowprint(
            "\nYou ready your bow, drawing back the string and letting loose "
            "an arrow. \nIt sails past the first two Orcs and the Warg, "
            "finding its mark in one of the \nOrcs at the back. You "
            "repeat the action, taking down the second Orc as well. \n"
        )

    elif "c" in first_battle_choice and "Bow & Arrow" not in inventory:
        slowprint(
            "\nOh no! Your chosen weapon is not suitable for this type "
            "of combat. \n"
            "You charge towards the enemies at the back, but they see you "
            "coming, loosing \ntheir own arrows. You attempt to dodge the "
            "flying blades and are forced to \nretreat. \n"
            f"{INJURY_DIALOGUE}"
        )
        add_to_inventory("Orc Injury")

    elif "d" in first_battle_choice and "Daggers" in inventory:
        slowprint(
            "\nYou crouch, taking a wide birth to sneak up on the hidden Orc."
            "\nThey don't see you coming, and you successfully land a hit! \n"
            "Nice, that's one down! Bifur and Dwalin can deal with the rest. "
            "\n"
        )

    elif "d" in first_battle_choice and "Daggers" not in inventory:
        slowprint(
            "\nOh no! Your chosen weapon is not suitable for this type \n"
            "of combat. \n"
            "It's difficult to crouch with your weapon ready, and you "
            "stumble, alerting the \nhidden Orc to your approach. They "
            "spring from the foliage, charging at you. \nTime to retreat "
            "back behind the Dwarves! \n"
            f"{INJURY_DIALOGUE}"
        )
        add_to_inventory("Orc Injury")

    else:
        abcd_error()
        first_battle()
    return inventory


def post_first_battle():
    """
    Runs interlude between First & Second battles & asks player to
    choose an option
    """
    slowprint(
        "The three of you return to the others and tell of your "
        "encounter with the Orcs. \nThey are all concerned by the "
        "proximity of the enemy and decide to vote on \nwhether to "
        "move on, despite night falling, or continue to set up camp and \n"
        "stay here for the night. \n"
    )

    post_first_battle_choice = input("Do you vote to move on? y/n\n")

    if post_first_battle_choice == "y":
        slowprint(
            "\nYou and the company quickly gather all your supplies, "
            "keeping an ear out for \nany sounds from the forest. \n"
            "You form a protective huddle, and together push forward "
            "through the forest. \n"
        )

    elif post_first_battle_choice == "n":
        slowprint(
            "\nThe company votes to stay. A couple of hours into the night, \n"
            "the forest becomes alive with growls and sounds of movement. \n"
            "Before any of you can prepare, a hoard of Orcs and Wargs \n"
            "emerges and attacks! \n"
        )
        game_over()

    else:
        yn_error()
        post_first_battle()


def second_battle():
    """
    Runs Second Battle & asks player to choose an option
    """
    slowprint(
        "You make it safely through the night... \n"
    )
    if "Orc Injury" in inventory:
        slowprint(
            "However, the injury you sustained in battle slows you down. \n"
        )
    else:
        slowprint(
            "Perhaps this adventuring business isn't so difficult, \n"
            "after all. \n"
        )

    slowprint(
        "You continue along the path, but are soon stopped by a powerfully "
        "flowing \nriver. \n"
        "In your packs, you each carry a bundle of rope. \n"
        "One of the Dwarves points out a large tree which could be used "
        "to affix the \nrope, allowing you all to move across. \n"
        "Somebody with an accurate and strong shot is needed, here... \n"
    )
    second_battle_choice = input(
        "Do you take the lead here, or let one of the others try first? y/n \n"
    ).lower()

    if (
            "y" in second_battle_choice and
            "Bow & Arrow" in inventory and
            "Orc Injury" in inventory):
        slowprint(
            "\nYou wind the rope securely around an arrow and aim it at the "
            "tree... \n"
            "But your injury jars you at the last second... \n"
            "The arrow lands in the tree, anyway, so you begin to climb "
            "across... \n"
            "But oh no! The arrow wasn't deep enough in the tree and "
            "it dislodges, \n"
            "dropping you into the raging river below. \n"
        )
        game_over()

    elif "y" in second_battle_choice and "Bow & Arrow" in inventory:
        slowprint(
            "\nYou wind the rope securely around an arrow and aim it at "
            "the tree... \n"
            "Success! Your arrow stuck! You tie the other end round a tree "
            "near you and \nbegin to climb across... \n"
            "The others soon follow. \n\n"
        )
    elif "y" in second_battle_choice and "Bow & Arrow" not in inventory:
        slowprint(
            "\nInteresting, do you plan to hurl your blade across the river "
            "at the tree? \n"
            "Needless to say, that doesn't work. \n"
            "Your weapon lands in the raging water, never to be seen \n"
            "again... \n"
            "Good job the Dwarves carry spares, eh? \n"
        )
        slowprint(f"{FOOL_DIALOGUE}")
    elif (
            "n" in second_battle_choice and
            "Bow & Arrow" in inventory and
            "Orc Injury" not in inventory):
        slowprint(
            "\nYou know, sometimes you have to step up to the task. \n"
            "Thankfully, you're not the only archer in this company. \n"
            "Kili successfully lands an arrow in the tree and, after tying \n"
            "the other end around a nearby tree, you all safely reach the \n"
            "other side... \n\n"
            f"{COWARDLY_DIALOGUE}"
        )
        add_to_inventory("Cowardly")
    elif "n" in second_battle_choice and "Bow & Arrow" not in inventory:
        slowprint(
            "\nIt was a wise decision to let an archer take this task. \n"
            "Kili successfully lands an arrow in the tree and, after tying "
            "the other end \naround a nearby tree, you all safely reach the "
            "other side... \n\n"
        )
    else:
        yn_error()
        second_battle()


def post_second_battle():
    """
    Runs interlude between Second & Third Battles.
    If player is injured - reminds them of their weapon and character status
    """
    if "Orc Injury" in inventory and "Cowardly" in inventory:
        slowprint(
            "Somebody should really have supplied you with an adventuring "
            "handbook.\n"
            "As a reminder, your weapon is "
            f"{WEAPONS}, you have sustained an injury and your fellow "
            "travellers view you as a bit cowardly.\n"
        )
    elif "Orc Injury" in inventory:
        slowprint(
            "Somebody should really have supplied you with an adventuring "
            "handbook.\n"
            "As a reminder, your weapon is "
            f"{WEAPONS} and you have sustained an injury."
        )
    elif "Cowardly" in inventory:
        slowprint(
            "Things are going quite well, although it wouldn't hurt to have "
            "a bit more \nconfidence in yourself."
        )
    else:
        slowprint(
            "This is all going quite well... \n"
        )


def third_battle_bow():
    """
    Runs Third Battle for Bow in inventory & asks player
    to choose an option
    """
    third_battle_choice = input(
        "Do you take cover behind the others, or join those who are "
        "attacking? y/n\n"
        ).lower()

    if "y" in third_battle_choice:
        if "Orc Injury" in inventory and "Cowardly" in inventory:
            slowprint(
                f"Wise decision. Your {WEAPONS} is best suited to ranged "
                "\n"
                "combat, and your injury means you should avoid the heat "
                "of battle. \n"
                "You may be a bit cowardly, but you're also sensible. \n"
                f"{SENSIBLE_DIALOGUE}"
            )
            add_to_inventory("Sensible")
            inventory.remove("Cowardly")
        elif "Cowardly" in inventory:
            slowprint(
                f"Wise decision. Your {WEAPONS} is best suited to ranged "
                "combat. \n"
                "You may be a bit cowardly, but you're also sensible. \n"
                f"{SENSIBLE_DIALOGUE}"
            )
            add_to_inventory("Sensible")
            inventory.remove("Cowardly")
        else:
            slowprint(
                f"Wise decision. Your {WEAPONS} is best suited to ranged "
                "combat. \n"
            )
    elif "n" in third_battle_choice:
        slowprint(
            "Well, I'm sure you've made better decisions in your life... "
            "\n"
            "Before you can even notch an arrow, you're down for the "
            "count \n"
            f"{INJURY_DIALOGUE}"
        )
        add_to_inventory("Bear Injury")
    else:
        yn_error()
        third_battle_bow()


def third_battle_daggers():
    """
    Runs Third Battle for Daggers in inventory & asks player
    to choose an option
    """
    third_battle_choice = input(
        "Do you take cover behind the others, or join those who are "
        "attacking? y/n\n"
        ).lower()
    if "y" in third_battle_choice:
        slowprint(
            "Yeah, Daggers probably wouldn't have helped out much, here. "
            "\n"
        )
    elif "n" in third_battle_choice:
        slowprint(
            "What's that saying about bringing knives to a gun fight...? "
            "\n"
            "This may be a bear fight, but the same principles apply... \n"
        )
        game_over()
    else:
        yn_error()
        third_battle_daggers()


def third_battle_sword_or_greatsword():
    """
    Runs Third Battle for Sword & Shield or Greatsword in inventory & asks
    player to choose an option
    """
    third_battle_choice = input(
        "Do you take cover behind the others, or join those who are "
        "attacking? y/n\n"
        ).lower()
    if "y" in third_battle_choice:
        if "Orc Injury" in inventory:
            slowprint(
                f"Wise decision. Your {WEAPONS} is suited for this type "
                "of combat, \n"
                "however your injury would likely have got you in "
                "trouble \n"
                f"{SENSIBLE_DIALOGUE}"
            )
            add_to_inventory("Sensible")
        else:
            slowprint(
                "Come on, now. What's the point in choosing the upfront \n"
                "weapons if you're just going to hide at the back? \n"
                f"{COWARDLY_DIALOGUE}"
                )
            add_to_inventory("Cowardly")
    elif "n" in third_battle_choice:
        if "Orc Injury" in inventory and "Cowardly" in inventory:
            slowprint(
                "It's good to see there is some bravery in you, but maybe "
                "you should have \nreserved it for when you aren't \n"
                "injured and being attacked by bears... \n"
                "Better luck next time! \n"
            )
            game_over()
        elif "Orc Injury" in inventory:
            slowprint(
                "It's generally considered wise to hang back if you "
                "recently got \nattacked by Orcs. You land a hit, but "
                " one of the bears \nswipes at you. \n"
                f"{INJURY_DIALOGUE}"
            )
            add_to_inventory("Bear Injury")
        else:
            slowprint(
                "Your bravery is commendable, and rewarded! You land a "
                "solid hit \non one of the bears and, between you, save "
                "yourselves from \nthis threat. \n"
            )
    else:
        yn_error()
        third_battle_sword_or_greatsword()


def pre_third_battle():
    """
    Runs pre-Third-Battle description & allocates a battle to player
    """
    slowprint(
        "Things are quiet for a while. \n"
        "You enjoy the good weather the new day has to offer. \n"
        "Suddenly, Ori shouts, and you and the company see two ginormous "
        "bears bounding \ntowards you... \n"
    )
    if "Bow & Arrow" in inventory:
        third_battle_bow()
    elif "Daggers" in inventory:
        third_battle_daggers()
    else:
        third_battle_sword_or_greatsword()


def post_third_battle():
    """
    Runs interlude between Third & Fourth battles.
    Reminds player of character's name & accumulated inventory traits
    """
    slowprint(
        "Things are certainly getting more dangerous... \n"
        f"Here's {NAME_INPUT}'s weapon & traits so far: {', '.join(inventory)}"
        "\n"
    )


def fourth_battle_injured():
    """
    Runs Fourth Battle if player was injured in either battle
    """
    slowprint(
        "You were injured in the past battles, so your track \n"
        "record isn't much to go on, but the Company believes in you, \n"
        "and so do I! \n"
    )
    if "Bow & Arrow" in inventory:
        slowprint(
            "At least you chose a bow! \n"
            "You join the other archers and prepare to attack...\n"
            "The others loose a battle cry and charge towards the gates \n"
            "as you loose your arrows at the enemy archers. \n"
            "Suddenly, you spot an enemy coming round from the side of the \n"
            "fortress towards your group."
            "Do you: \n"
            "a) Turn your weapon towards them and fire, \n"
            "b) Assume one of the dagger-wielders is protecting the flank, \n"
            "c) Shout for the attention of the others, \n"
        )
        fbsi_archer_choice = input("a, b or c? ")
        fbsi_archer_choice_wrong = (
            "Looks like you're sitting out the rest of "
            "this battle...\n"
        )

        if fbsi_archer_choice == "a":
            slowprint(
                "You pivot, firing an arrow towards the sneaking enemy... \n"
                "Your injuries jar you and you miss... \n"
                "But it's okay, Kili noticed your attempt and lands his own "
                "shot! \n"
                "However, you left yourself exposed, and a turret archer "
                "looses an arrow before \n you can react. \n"
                "It's not a lethal hit, but you're not going to be much use, "
                "now. \n"
            )
            slowprint(fbsi_archer_choice_wrong)
        elif fbsi_archer_choice == "b":
            slowprint(
                "Teamwork is a wonderful thing, truly. \n"
                "You say nothing, losing sight of the enemy until you hear a "
                "cry... \n"
                "Oh no! They attacked Balin! \n"
                "You duck out of battle to lead Balin to safety, leaving only "
                "one archer to take \ndown those on the turrets. \n"
                "The archers quickly overwhelm the Company, the melee users \n"
                "powerless to stop them... \n"
                "So near, and yet so far... \n"
            )
            game_over()
        elif fbsi_archer_choice == "c":
            slowprint(
                "You alert the others to the enemy's approach. \n"
                "While you and Balin maintain the attack on the turret "
                "archers, "
                "Kili successfully takes down the sneaking enemy. \n"
                "Good work! \n"
            )
        else:
            abc_error()
            fourth_battle_injured()

    else:
        slowprint(
            "Well, best of luck to you. \n"
            "Together with the other melee users, you charge through the \n"
            "gates towards the emerging enemies. \n"
            "The battle is loud and violent, the sounds of blades ringing "
            "throughout the space.\n"
            "You notice three enemies attempting to push past to the archers "
            "at the back... \n"
            "Do you: \n"
            "a) Break ranks to target them, \n"
            "b) Attempt to shout loud enough to be heard over the fighting, \n"
            "c) Focus on the enemies around you - the archers will protect "
            "themselves. \n"
        )
        fbsi_melee_choice = input("").lower()
        fbsi_melee_choice_wrong = (
            "Sometimes you need to take intiative. "
            "After \nall, your company is very small, you can't afford to "
            "lose anyone."
        )

        if fbsi_melee_choice == "a":
            slowprint(
                "You made a difficult decision in the heat of battle, \n"
                "thankfully, it pays off, and you prevent the enemies from "
                "moving past, forcing them back into the fray. \n"
                "Good job! \n"
            )
        elif fbsi_melee_choice == "b":
            slowprint(
                "I'm sure you can shout loudly, but not that loudly. \n"
                "Nobody hears you, and the enemies rush past, taking out \n"
                "your archers before the other can stop them. \n"
                "With no ranged defence, the Company is quickly "
                "overwhelmed... \n"
            )
            game_over()
        elif fbsi_melee_choice == "c":
            slowprint(
                "This was a gamble. Balin spots the rebellious trio \n"
                "and attempts to prevent them from attacking. Unfortunately, "
                "he is seriously \ninjured and out of the battle. \n"
            )
            slowprint(fbsi_melee_choice_wrong)
        else:
            abc_error()
            fourth_battle_injured()


def fourth_battle_cowardly():
    """
    Runs Fourth Battle if player has the Cowardly trait in their inventory
    """
    slowprint(
        "You've made some less-than-confident decisions so far, \n"
        "but you're in perfect health, so let's do battle! \n"
    )
    if "Bow & Arrow" in inventory:
        slowprint(
            "You join the other archers in targetting those on the "
            "turrets... \n"
            "Together you make quick work of them, however you spot an enemy "
            "sneaking towards you, blades ready. \n"
            "The others haven't spotted them, yet... \n"
            "Do you attack? Or hope someone else sees them and takes "
            "the lead? y/n \n"
        )
        fbc_archer_choice = input("")
        if fbc_archer_choice == "y":
            slowprint(
                "Look at you, stepping up to the job! You ready an arrow... "
                "fire... and land a hit!\n"
                "Well done, you saved your trio from potentially "
                "assassination.\n"
            )
        elif fbc_archer_choice == "n":
            slowprint(
                "Still a bit cowardly, I see. The others don't see the "
                "approaching enemy until \nit's too late.\n"
                "Balin is injured before you counterattack.\n"
                "You lead him to safety, but this leaves all the remaining "
                "turret archers to one \nman... \n"
            )
        else:
            yn_error()
            fourth_battle_cowardly()
    else:
        slowprint(
            "Time to put that wariness aside and attack. \n"
            "After all, that is why you're here, no? \n"
            "You join the charge of melee users into the fray. \n"
            "The battle is invigorating, blades clash, shields block, cries "
            "are let loose. \n"
            "But, it seems like you might be winning! \n"
            "Out the corner of your eye, you spot an enemy approaching from "
            "behind... \n"
            "Do you move to attack them, or focus on those you're already "
            "fighting? y/n \n"
        )
        fbc_melee_choice = input("").lower()
        if fbc_melee_choice == "y":
            if "Daggers" in inventory:
                slowprint(
                    "You pivot, aim, and throw one of your daggers towards "
                    "the enemy... \n"
                    "Success! Your group is safe from that threat, at least. "
                    "\n"
                )
            else:
                slowprint(
                    "You brace yourself before charging at the approaching "
                    "enemy... \n"
                    "They don't expect it, and are out of the battle before "
                    "they can even react. \n"
                    "Good job! \n"
                )
        elif fbc_melee_choice == "n":
            slowprint(
                "The enemies in front of you are important, yes, but that \n"
                "approaching one is going to be even more important if they \n"
                "get the drop on any of you... \n"
                "Which they do. Gloin is attacked before anyone else can "
                "react, \n"
                "disrupting the flow of the Company. \n"
                "Your reluctance to commit costs another two Dwarves an "
                "injury before the \nsneaky enemy is dispatched. \n"
                "With a significant chunk of the group out of commission, "
                "the Company \n"
                "is quickly overwhelmed... \n"
            )
            game_over()
        else:
            yn_error()
            fourth_battle_cowardly()


def fourth_battle_good():
    """
    Runs Fourth Battle if player has the Sensible trait in inventory or no
    traits (other than their weapon)
    """
    if "Sensible" in inventory:
        slowprint(
            "The Company view you as a sensible companion... \n"
            "Let's not prove them wrong... \n"
        )
    else:
        slowprint(
            "Fuelled by the success of your previous battles, \n"
            "you and the company attack strong, breezing through the enemy \n"
            "and pushing forward to the front doors. \n"
        )

    if "Bow & Arrow" in inventory:
        slowprint(
            "From your position in the back line, you aim high at the turret "
            "archers. \nYour skill with the bow shines through, and together "
            "you keep the other members \nof the group safe from airbourne "
            "attacks... \n"
        )
    else:
        slowprint(
            "You charge towards the emerging enemies with the Company, battle "
            "cries ringing \nthrough the air..."
            "You've done well so far, but this battle is much more difficult "
            "than those \nyou've faced along the way. \n"
            "The enemy attacks relentlessly, and you notice the Company's "
            "left flank \nbecoming overwhelmed... \n"
            "Do you: \n"
            "a) Move across to lend them a hand \n"
            "b) Alert those around you of the growing struggle \n"
            "c) Do nothing: you have your own enemies to worry about \n"
        )
        fbg_melee_choice = input(" ").lower()
        if fbg_melee_choice == "a":
            slowprint(
                "A risky decision, however the rest of the Company is "
                "attacking strong \nand your assistance on the left disrupts "
                "the enemies, forcing them to \nfall back... \n"
            )
        elif fbg_melee_choice == "b":
            slowprint(
                "Somehow, your cry is heard over the turmoil. The Company "
                "shifts as a whole \nto the left, overwhelming the enemy "
                "in turn. \n"
            )
        elif fbg_melee_choice == "c":
            slowprint(
                "Doing nothing in battle is never a wise choice. \n"
                "With the rest of the Company focussed on their immediate "
                "targets nobody goes to \nthe assistance of the left... \n"
                "The enemy makes quick work of your teammates, before setting "
                "their sights on \nthe rest of you... \n"
            )
            game_over()
        else:
            yn_error()
            fourth_battle_good()


def pre_fourth_battle():
    """
    Runs pre-Fourth-Battle description & allocates a battle to player
    """
    slowprint(
        "Finally after many gruelling days the company spots the \n"
        "Fortress only a couple leagues away. \n"
        "You're almost there! \n"
        "Congratulations on making it this far! \n\n"
        "As you and the Company approach, the Fortress is still... \n"
        "Thorin, the leader, gestures to get into position... \n"
        "Suddenly, the front gates swing open and arrows rain down from \n"
        "the turrets above... \n"
        "The battle begins! \n"
    )
    if "Orc Injury" in inventory or "Bear Injury" in inventory:
        fourth_battle_injured()
    elif (
            "Cowardly" in inventory and
            "Orc Injury" not in inventory and
            "Bear Injury" not in inventory):
        fourth_battle_cowardly()
    else:
        fourth_battle_good()


def fourth_battle_end():
    """
    Runs Game-End dialogue
    """
    slowprint(
        "The battle rages on, but it looks like you're winning! \n"
        "Suddenly, a cry sounds from within, as the thief who owns \n"
        "this fortress realises they have been beat. \n"
        "As you defeat their army, something comes flying from a high "
        "window... \n"
        "It's the key! The thief flees their fortress, but you have what you "
        "came for! \n"
        "Congratulations! The road was hard, but you successfully helped the "
        "Dwarves... \n"
        "I suppose it's time to prepare to battle a Dragon... \n"
    )


def choose_name():
    """
    Asks player to choose a character name.
    """
    global NAME_INPUT
    NAME_INPUT = input(
        "Please choose a name for your character: "
    ).capitalize()

    slowprint(f"\nWelcome to the company, {NAME_INPUT}! \n")


def add_to_inventory(item):
    """
    Holds data for player inventory
    """
    inventory.append(item)
    print(inventory)


def abc_error():
    """
    Reminds the user to choose an accepted option
    """
    slowprint(
        "Please choose either a, b or c \n"
    )


def abcd_error():
    """
    Reminds the user to choose an accepted option
    """
    slowprint(
        "Please choose either a, b, c or d \n"
    )


def yn_error():
    """
    Reminds the user to choose an accepted option
    """
    slowprint(
        "Please choose either y or n \n"
    )


def clear_terminal():
    """
    Clears the terminal - used in game_over function
    """
    os.system('clear')


def game_over():
    """
    Runs game over after losing/finishing the game
    Player input to retry or quit game
    """
    slowprint("Game Over!\n")
    replay = input("Would you like to play again? y/n \n")
    if "y" in replay:
        clear_terminal()
        inventory.clear()
        main()
    else:
        slowprint("Okay! Good game!")
        clear_terminal()
        sys.exit()


def main():
    """
    Holds all game functions to run in order
    """
    about_game()
    play_game()
    choose_name()
    weapon_choice()
    first_battle()
    post_first_battle()
    second_battle()
    post_second_battle()
    pre_third_battle()
    post_third_battle()
    pre_fourth_battle()
    fourth_battle_end()
    game_over()


main()
