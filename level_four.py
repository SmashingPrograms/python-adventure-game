# CONNOR

import random

def game_end(player1):
    if player1.game == False:
        return True

def choice(player1):
    player1.user_input = input("What will you do? (Select A, B, or C) ").upper()
    while True:
        if player1.user_input == 'A' or player1.user_input == 'B' or player1.user_input == 'C':
            break
        else:
            player1.user_input = input("Please select A, B, or C. ")
            print(player1.user_input)

def give_satchel(player1):
    player1.item.append('satchel')
    player1.health += 2
            

def choice1(player1):
    print("***Your vision becomes clearer as your eyes adjust. You take note of your surroundings. A man stands in the doorway of the room you are in. You are on some sort of bed. There is another door to your left***\n")
    print("STRANGE MAN: So you made it out. Well done, I expected less. Everything you've experienced up until now was an illusion...and illusion of my creation!\n")
    print("The man doesn't seem threatening when you look at him. Also, you are wearing the same thing you remember wearing the last time you were conscious. You see the top of a bag in the view of the doorway. Your items perhaps?...\n")
    print("Your options:\n")
    print("A: Try and catch him off gaurd by standing up and running for the window. Hopefully you can survive the jump...\n")
    print("B: Attack the man head on, hoping you can beat him in a fight\n")
    print("C: Run for the door to your left. Maybe it'll be a step in the right direction...\n")
    print(f"Current Health: {player1.health}\nCurrent EXP: {player1.exp}\nCurrent Bounty: {player1.bounty}")
    choice(player1)

    if player1.user_input == 'A':
        print('***You run as fast as you can to thw window. You hear the man sigh as you begin to leap out.***\n')
        if player1.health < -5:
            print('***The ground approaches quickly. You brace for impact...***\n......\n(You died)')
            player1.game = False
            return
        else:
            print('***The ground approaches quickly. You brace for impact...***\n.....\n***You roll as you hit the ground, taking little damage. You see a single cobblestone road leading from the house to a gate. Better get out of here, right?***')
            player1.health -= 5
            player1.exp += 3

    elif player1.user_input == 'B':
        print('***You run at the man and try to knock him out***\n')
        player1.bounty += 3

        while True:
            attack = random.randint(1,5)
            if attack < 6:
                print("\n***You knock him out! After grabbing your items, you run down the hall and through the front door of the building. You see a single cobblestone road leading from the house to a gate. Better get out of here, right?***\n")
                player1.exp += 3
                break
            else:
                print("\n***A swing and a miss! STRANGE MAN counters with a swift right hook!***\n")
                player1.health -= 1
                continue

    elif player1.user_input == 'C':
        print('\n***You run for the door on the left as STRANGE MAN chases you from behind. It leads into a hallway connected to the hallway in front of your room. You make a right, pick up your items, and keep going. In order to escape, you decide to throw an item at your pursuer to trip him up.***\n')
        if len(player1.item) == 0:
            print('\n***You have nothing left to throw!***\nSTRANGE MAN: GOTCHA!\n***STRANGE MAN TACKLES YOU AND PULLS OUT A KNIFE***\nSTRANGE MAN: This is it for you...\n.....\n(You died)\n')
        else:
            index = random.randint(0, len(player1.item) - 1)
            del player1.item[index]
            chance_to_fail = random.randint(0, 20)
            print(chance_to_fail)
            if chance_to_fail < 2:
                print('\n***STRANGE MAN easily avoids your item***\nSTRANGE MAN: GOTCHA!\n***STRANGE MAN TACKLES YOU AND PULLS OUT A KNIFE***\nSTRANGE MAN: This is it for you...\n.....\n(You died)')
                player1.game = False
            else:
                print('\n***STRANGE MAN trips over your item and is knocked out! You continue down the hallway and out the door. You see a single cobblestone road leading from the house to a gate. Better get out of here, right?***\n')
                player1.exp += 3
                player1.bounty += 1

    
def choice2(player1):
    print("\n***You approach the gate. There is a single armored gaurd manning it. You are confident you can escape, but what if you can do more?***\n")
    print("Your Options:\n")
    print('A: Attempt to scare the gaurd. With a high enough bounty, he might offer you more than passage...\n')
    print('B: Sprint at the gate and climb it. The gaurd is wearing heavy armor, you can assume he is significantly slower than you.\n')
    print('C: Fight him. Hey, your funeral! After all, it is easy to rob a man if hes unconscious.\n')
    print(f"Current Health: {player1.health}\nCurrent EXP: {player1.exp}\nCurrent Bounty: {player1.bounty}\n")
    choice(player1)

    if player1.user_input == 'A':
        print(f"***You attempt to scare the gaurd.***\n{player1.name.upper()}: Do you know who I am?\n***You point to a conveniently placed wanted poster to the right. It has your name on it along with you bounty.\n")
        if player1.bounty < 56:
            print("GAURD: HAHAHAHAHAHA! Not enough to scare me! You want to get past? You'll have to go through me.\n")
            print("***You sigh and dart beside him, jumping onto the gate. His armor restricts his movements and he is unable to catch you. You make it over the gate and run down the street, losing the gaurd.\n")
        else:
            print(f"GAURD: Look man I just work here, please just leave. I won't stop you.\n{player1.name.upper()}: I'll do more than leave if you don't give me that satchel on your hip!\n")
            print("GAURD: Fine, take it and go.\n***You take the satchel and, once opened by the gaurd, walk out of the gate and down the street.\n")
            give_satchel()
            print("Obtained SATCHEL: Contains the belongings of the gaurd you robbed at a gate.\n")

    elif player1.user_input == 'B':
        print("***You dart to the gaurds left, sprinting for the gate.***\nGAURD: HEY! Get back here!\n ***You hear the clank of armor as the gaurd tries to catch you. To little to late, however, as you are much faster and scale the gate. You hop down and run down the street, losing the gaurd.\n")

    else:
        print("You charge the gaurd as hard as you can (really dude, he has ARMOR. Read it with me. A R M O R).\n")
        attack_roll = random.randint(0, 30)

        if attack_roll > 5:
            print("You punch the gaurd as hard as you can and...it hurts like hell because hes wearing ARMOR...\nGAURD: Whats wrong? Hand hurt?\n***With a smirk, the gaurd draws his sword and...***\n.....\n(Your dead).")
            player1.game = False
        else:
            print("You punch the gaurd as hard as you can and...it hurts like hell because hes wearing ARMOR...\nBut WAIT! The punch was enough to throw him off balance!\nGAURD: Dang it, I cant get up!")
            print("***You notice a satchel on the gaurds hip. You dart at it, ripping the strap and snatching it off his hip.***\n")
            give_satchel(player1)
            print('***You walk past the gaurd, scale the gate, and walk down the street.***\n')

def ending(player1):
    print("You walk down the street, highly confused about what just happened. Whatever the case, you escaped. Thats what matters. Time for your next adventure...***\n")
    print(f"Current Health: {player1.health}\nCurrent EXP: {player1.exp}\nCurrent Bounty: {player1.bounty}\n")


def game(player1):
    print("\nSTRANGE MAN: .....\n\nReally...\n\n.....\n\nA sunset? You really believed that?\n\nYou blink your eyes a few times, squinting at the light of the sun piercing into your eyes. You feel groggy, as if you've been asleep for a long time...\n\n")
    choice1(player1)
    if game_end(player1):
        return
    choice2(player1)
    if game_end(player1):
        return
    ending(player1)

def level_4(player1):
    game(player1)
    
