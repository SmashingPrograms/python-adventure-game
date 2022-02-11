# DANIEL

import random

def level_3(player1):

    global battle_success
    battle_success = 0

    def change_health(num): #global for the tea
        player1.health += num

    def change_bounty(bounty):  #global for the team
        player1.bounty += bounty

    def change_exp(experience):  #global for the team
        player1.exp += experience

    global world_items
    world_items = {'Cow': change_health(-5),
                   'Limbs': change_health(10),
                   'Crown': change_bounty(30),
                   }

    def user_choice():  # global for the team
        global user_input
        user_input = input(
            'What do you choose? A, B, or C? Pick carefully').upper()

    def fight_mechanic(num):
        battle_result = random.randint(1, num)
        if battle_result == 3:
            player1.health = 0
            print('YOU HAVE LOST YOUR HEAD, YOU ARE DEAD!!')
        elif battle_result == 2:
            print('Hit!')
            global battle_success
            battle_success += 1
        else:
            print(player1.name, 'have been slapped for being a horrible thief!')

    def enter_python(player1):
        print(player1.name, 'pops out of the pipe......where an I! You look out and see a tavern.',
              player1.name, 'is thirsty. Will you (A)(choose a drink), (B)(continue to see what other things are to be found), or (C)(see if you can take some coin from the tavern?')
        user_choice()

        enter_python(player1)

        if user_input == 'A':
            print(
                player1.name, ' grab a drink, and hear about an emience treasure directly North of the tavern')
            player1.health -= 5
            print(player1.name, 'heads out of the tavern, what will',
              player1.name, 'do next?')
            enter_python(player1)
        elif user_input == 'B':
            print(player1.name,
                  'travels Northwards in search for this eminence treasure')
        elif user_input == 'C':
            print(player1.name, 'heads into the tavern for some coin!!!!')

    # while user_input == 'A':
    #     print(player1.name, 'heads out of the tavern, what will',
    #           player1.name, 'do next?')
    #     enter_python(player1)

    # while user_input == 'C':
    #     print(player1.name,
    #           'senses wealth in this establishment and decides to attempt to steal!!')
    #     user_choice()
    #     fight_mechanic(2) 
    #     fight_mechanic(2)
    #     if battle_success == 2:
    #         print(player1.name, 'successful stole some coin')
    #         change_bounty(3)
    #         battle_success = 0
    #     else: 
    #         print(player1.name, 'was unsuccessful, and was kick out by the bartender that say Ne!! Into a dark nasty bog')
    #         battle_success = 0


