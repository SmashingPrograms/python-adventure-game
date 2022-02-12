# DANIEL

from cgi import print_environ_usage
from ctypes.wintypes import WORD
import random
from tkinter.tix import Balloon


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
                   'Limbs': -10,
                   'Crown': 30,
                   'Grail': 50,
                   }

    global combat_steps
    combat_steps = {
        'die': 'YOU HAVE LOST YOUR HEAD, YOU ARE DEAD!!',
        'enemy_damage': 'YOU ARE SUCCESFUL IN YOUR TACTICS AND LAND A HIT',
        'player_damage': 'YOU HAVE BEEN SLAPPED FOR BEING A HORRIBLE THIEF!',
        'bunny_damage': 'BUNNY NOISES',
        'king_damange': 'HOW DARE YOU ATTACK ME, FOR I AM KING ARUTHER OF THE ROUND TABLE, AND MY KNIGHTS SHALL DO DAMAGE TO YOU. NI!'
    }

    def player_health():
        if player1.health == 0:
            exit

    def user_choice():  # global for the team
        player1.user_input = input(
            'What do you choose? A, B, or C? Pick carefully ').upper()

    def fight_mechanic(num):
        battle_result = random.randint(1, num)
        if battle_result == 3:
            player_health()
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
    enter_python()

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
        enter_python()

    while player1.user_input == 'C':
        print(player1.name,
              'senses wealth in this establishment and decides to attempt to steal!!\n')
        fight_mechanic(2)
        fight_mechanic(2)
        if battle_success == 2:
            print(player1.name, 'successful stole some coin\n')
            change_bounty(2)
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
        print('As', player1.name, 'eventually find the other side of the bog. King Author is waiting to destory', player1.name, 'they must being getting close the the great spoils. King Arthur challenges you to a duel!!!!\n')
        king_fight(player1)

    if player1.user_input == 'A':
        change_health(-5)
        change_exp(5)
        king_fight(player1)

    elif player1.user_input == 'C':
        player_health()
        print(combat_steps['die'])
        player1.game = False
    else:
        while fight_counter < 4:
            fight_mechanic(2)
            fight_counter += 1
            if battle_success == 1:
                print(combat_steps['king_damange'])


        while fight_counter == 4:
            fight_mechanic(3)
            fight_counter += 1
            if battle_success == 1:
                print(combat_steps['king_damange'])
            elif battle_success == 3:
                player_health()

    fight_counter = 0
    print('After an exhausting battle between', player1.name, 'and King Authur. With an amazing strike of the rusty sword', player1.name, 'lands a deadly strike on the King, who falls to his death yelling one last NI!\n')
    change_exp(20)
    player1.item.append('Crown')
    change_bounty(world_items['Crown'])

    #Bunny section
    print('After the battle with the King', player1.name, 'proceeds through a barren plans. Until in the distance they see a cave. Could this be the resting place of the treasure they are in search for?\n')
    print('(A)(Yes), (B)(Yes), (C)(......yes)')
    user_choice()
    print('As', player1.name, 'approaches the out jumps a super bunny with a love for limbs!!', player1.name,'knows this must be the final boss of this world and the protector of the treasure.\n')
    print('How will they choose to proceed? (A)(Head bravely into battle,(B)(Head fearfully into battle,(C)faint!......do not do this!!! ')

    if player1.user_input == 'C':
        print('I told you not to do this!', player1.name, 'fell when they fainted and hit their head on rock. They are now dead')
        player_health()
    elif player1.user_input == 'B':
        while fight_counter < 3:
            fight_mechanic(3)
            fight_counter += 1
    else:
        while fight_counter < 2:
            fight_mechanic(3)
            fight_counter += 1
    
    print(player1.name, 'has successfully beat the bunny. As they look up, there it is. Can it be!!! A golden cup!! the Holy Grail!!!! This find will surely make', player1.name, 'the most famous individual in the world!! We shall see!')
    player1.item.append('Grail')
    change_bounty(world_items['Grail'])
    change_exp(world_items['Grail'])
    change_health(world_items['Grail'])
    

    #End section

    
