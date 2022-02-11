import random


def level_3(player1):
    global user_input
    user_input = ''  # global for the team

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
        user_input = print(
            'What do you choose? A, B, or C? Pick carfully').upper()

    def fight_mechanic(num):
        battle_result = random.randint(1, num)
        if battle_result == 3:
            player1.health = 0
            print('YOU HAVE LOST YOUR HEAD, YOU ARE DEAD!!')
        elif battle_result == 2:
            print('Hit!')
        else:
            print(player1.name, 'have been slapped for being a horrible thief!')

    def enter_python(player1):
        print(player1.name, 'pops out of the pipe......where an I! You look out and see a tavern.',
              player1.name, 'is thirsty. Will you (A)(choose a drink), (B)(continue to see what other things are to be found), or (C)(see if you can take some coin from the tavern?')
        user_choice()

        if user_input == 'A':
            print(
                player1.name, ' grab a drink, and hear about an emience treasure directly North of the tavern')
            player1.health -= 5
        elif user_input == 'B':
            print(player1.name,
                  'travels Northwards in search for this eminence treasure')
        elif user_input == 'C':
            print(player1.name, 'heads into the tavern for some coin!!!!')

    while user_input == 'A':
        print(player1.name, 'heads out of the tavern, what will',
              player1.name, 'do next?')
        enter_python(player1)

    while user_input == 'B':
        print(player1.name,
              'senses wealth in this establishment will you choose to steal?')
        fight_mechanic(2) * 2

    while user_input == 'C':
        print('hi')
