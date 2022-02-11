# DANIEL

import random


def level_3(player1):

    global battle_success
    battle_success = 0
    fight_counter = 0

    def change_health(num):  # global for the tea
        player1.health += num

    def change_bounty(bounty):  # global for the team
        player1.bounty += bounty

    def change_exp(experience):  # global for the team
        player1.exp += experience

    global world_items
    world_items = {'Cow': -5,
                   'Limbs': 10,
                   'Crown': 30,
                   }

    global combat_steps
    combat_steps = {
        'die': 'YOU HAVE LOST YOUR HEAD, YOU ARE DEAD!!',
        'enemy_damage': 'YOU ARE SUCCESFUL IN YOUR TACTICS AND LAND A HIT',
        'player_damage': 'YOU HAVE BEEN SLAPPED FOR BEING A HORRIBLE THIEF!',
        'bunny_damage': 'BUNNY NOISES',
        'king_damange': 'HOW DARE YOU ATTACK ME, FOR I AM KING ARUTHER OF THE ROUND TABLE, AND MY KNIGHTS SHALL DO DAMAGE TO YOU. NI!'
    }

    def user_choice():  # global for the team
        player1.user_input = input(
            'What do you choose? A, B, or C? Pick carefully ').upper()

    def fight_mechanic(num):
        battle_result = random.randint(1, num)
        if battle_result == 3:
            player1.health = 0
            print(combat_steps['die'])
        elif battle_result == 2:
            print(combat_steps['enemy_damage'])
            global battle_success
            battle_success += 1
        else:
            print(combat_steps['player_damage'])

    def enter_python():
        print('Will you (A)(choose a drink), (B)(continue to see what other things are to be found), or (C)(see if you can take some coin from the tavern?\n')
        user_choice()

    def king_fight(player1):
        print('(A)(Stay in the bog), (B)(Charge at the King), (C)(Fall on the rusty sword that mysteriously is at the feet of', player1.name)
        user_choice()

    # enter the world

    print(player1.name, 'pops out of the pipe......where an I!', player1.name,
          'look out and see a tavern.', player1.name, 'is thirsty\n')
    enter_python(player1)

    if player1.user_input == 'A':
        print(
            player1.name, ' grab a drink, and hear about an emience treasure directly North of the tavern\n')
        change_health(-5)
        change_exp(1)
    elif player1.user_input == 'B':
        print(player1.name,
              'travels Northwards in search for this eminence treasure\n')
    elif player1.user_input == 'C':
        print(player1.name, 'heads into the tavern for some coin!!!!\n')

    while player1.user_input == 'A':
        print(player1.name, 'heads out of the tavern, what will',
              player1.name, 'do next?\n')
        enter_python(player1)

    while player1.user_input == 'C':
        print(player1.name,
              'senses wealth in this establishment and decides to attempt to steal!!\n')
        fight_mechanic(2)
        fight_mechanic(2)
        if battle_success == 2:
            print(player1.name, 'successful stole some coin\n')
            change_bounty(3)
            battle_success = 0
            break
        else:
            print(player1.name, 'was unsuccessful, and was kick out by the bartender\'s that say NI!! Into a dark nasty bog\n')
            battle_success = 0
            break

    # next section in the world

    if player1.user_input == 'C':
        player1.user_input = 'B'
    else:
        print('As you head north', player1.name,
              'finds a bog! To the East as impenetrable mountains, to the west there is a mystrious fog, which direction will', player1.name, ' go?\n')
        print('(A)(West), (B)(North)')
        user_choice()

    if player1.user_input == 'A':
        print(player1.name, 'heads into the mysterious fog, they come across castle. The castle seems deserted./n')
        if player1.exp < 50:
            print('After a long examination', player1.name, 'finds nothing and continues through the fog', player1.name,
                  'finds that they are completely surroned by the bog found before and continue on through the dark, stinky waters\n')
            player1.user_input = 'B'
        elif player1.bounty > 50:
            print(player1.name, 'yells out, and peaking over the top of the castle a group of french soliders appear, knowing who', player1.name, 'is they scream be gone thief. The french throw over the wall and it lands next to',
                  player1.nam, player1.name, 'runs way from the french not wishing more cow!!!!!!', player1.name, 'finds that they are completely surroned by the bog found before and continue on through the dark, stinky waters\n')
            player1.item.append('Cow')
            change_health(world_items['Cow'])
            player1.user_input = 'B'
        else:
            print(player1.name, 'yells out, and peaking over the top of the castle a group of french soliders appear. Not knowing who', player1.name, 'is they yell to continue on as visitors are not welcome here!! As',
                  player1.name, 'continues on they run finds that they are completely surroned by the bog found before and continue on through the dark, stinky waters\n')
            change_bounty(-5)
            player1.user_input = 'B'

    #King section

    if player1.user_input == 'B':
        change_exp(5)
        print('As', player1.name, 'eventually find the other side of the bog. King Authr is waiting to destory', player1.name, 'they must being getting close the the great spoils. King Arthur challenges you to a duel!!!!\n')
        king_fight()

    if player1.user_input == 'A':
        change_health(-5)
        change_exp(5)
        king_fight()

    elif player1.user_input == 'C':
        player1.health = 0
        print(combat_steps['die'])
    else:
        print('hi')


        while fight_counter < 3:
            fight_mechanic(2)
            fight_counter += 1

        while fight_counter < 5 and fight_counter > 3:
            fight_mechanic(3)
            fight_counter += 1

    #Bunny section

    #End section

