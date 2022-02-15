# DANIEL

import random


def level_3(player1):

    global battle_success
    battle_success = 0
    fight_counter = 0
    global limb_status
    limb_status = False

    # def change_health(num):  
    #     player1.health += num

    def change_bounty(bounty):  
        player1.bounty += bounty

    def change_exp(experience):  
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
        player1.health = 0
        player1.game = False

    def user_choice():  
        player1.user_input = input(
            'What do you choose? A, B, or C? Pick carefully ').upper()

    def fight_mechanic(num):
        global battle_result
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
        print('Will you (A)(choose to drink), (B)(continue to see what other things are to be found), or (C)(see if you can take some coin from the tavern?\n')
        user_choice()

    def king_fight(player1):
        print('(A)(Stay in the bog), (B)(Charge at the King), (C)(Fall on the rusty sword that mysteriously is at the feet of', player1.name)
        user_choice()

    # enter the world

    print(player1.name, 'pops out of the pipe......where am I!', player1.name,
          'looks out and sees a tavern.', player1.name, 'is thirsty\n')
    enter_python()

    if player1.user_input == 'A':
        print(
            player1.name, ' grab a drink, and hear about an emience treasure directly North of the tavern\n')
        change_health(-5)
        change_exp(1)
        print(player1.name,
              'heads out of the tavern, and heads North to find eminence treasure\n')
    elif player1.user_input == 'B':
        print(player1.name,
              'travels Northwards in search for  eminence treasure\n')
    elif player1.user_input == 'C':
        print(player1.name, 'heads into the tavern for some coin!!!!\n')

    while player1.user_input == 'C':
        print(player1.name,
              'senses wealth in this establishment and decides to attempt to steal!!\n')
        fight_mechanic(2)
        if battle_result == 2:
            print(
                player1.name, 'successfully stole some coin, and run into a dark nasty bog\n')
            change_bounty(2)
            battle_success = 0
            break
        else:
            print(player1.name, 'was unsuccessful, and was kick out by the bartender\'s that say NI!! Into a dark nasty bog\n')
            battle_success = 0
            break

    # next section in the world
    while player1.game == True:

        if player1.user_input == 'C':
            player1.user_input = 'B'
        else:
            print('As', player1.name, 'heads north', player1.name,
                  'finds a bog! To the East as impenetrable mountains, to the west there is a mystrious fog, which direction will', player1.name, ' go?\n')
            print('(A)(West), (B)(North), (C)(Die)')
            user_choice()

        if player1.user_input == 'A':
            print(player1.name, 'heads into the mysterious fog, they come across castle. The castle seems deserted./n')
            if player1.exp < 50:
                print('After a long examination', player1.name, 'finds nothing and continues through the fog', player1.name,
                      'finds that they are completely surronded by the bog found before and continue on through the dark, stinky waters\n')
                player1.user_input = 'B'
            elif player1.bounty > 50:
                print(player1.name, 'yells out, and peaking over the top of the castle a group of french soliders appear, knowing who', player1.name, 'is they scream BE GOND THIEF!!. The french throw a dead cow over the wall and it lands next to',
                      player1.name, '!', player1.name, 'runs way from the french not wishing more cows!!!!!!', player1.name, 'finds that they are completely surroned by the bog found before and continue on through the dark, stinky waters\n')
                player1.item.append('Cow')
                player1.change_health(world_items['Cow'])
                player1.user_input = 'B'
            else:
                print(player1.name, 'yells out, and peaking over the top of the castle a group of french soliders appear. Not knowing who', player1.name, 'is they yell to continue on as visitors are not welcome here!! As',
                      player1.name, 'continues on they run finds that they are completely surroned by the bog found before and continue on through the dark, stinky waters\n')
                change_bounty(-5)
                player1.user_input = 'B'

        # King section

        if player1.user_input == 'B':
            change_exp(5)
            print('As', player1.name, 'eventually find the other side of the bog. King Author is waiting to destory',
                  player1.name, 'they must being getting close to the great spoils. King Arthur challenges you to a duel!!!!\n')
            king_fight(player1)

        if player1.user_input == 'A':
            print(
                player1.name, 'lose health, but gains insight to help in the upcoming battle again King Author. After careful study', player1.name, 'charges into battle with the King!' )
            player1.change_health(-5)
            change_exp(5)
            print('After preparing themselves', player1.name,
                  'charges at the King, ready for their fate!!')

        elif player1.user_input == 'C':
            player_health()
            print(combat_steps['die'])

        elif player1.user_input == 'B':
            while fight_counter < 4:
                fight_mechanic(2)
                fight_counter += 1
                if battle_result == 1:
                    print(combat_steps['king_damange'])

            while fight_counter == 4:
                fight_mechanic(3)
                fight_counter += 1
                if battle_result == 1:
                    print(combat_steps['king_damange'])
                elif battle_result == 3:
                    player_health()

        fight_counter = 0
        if player1.game == False:
            break

        print('After an exhausting battle between', player1.name, 'and King Authur. With an amazing strike of the rusty sword',
              player1.name, 'lands a deadly strike on the King, who falls to his death yelling one last NI!\n')
        change_exp(20)
        player1.item.append('Crown')
        change_bounty(world_items['Crown'])

        # Bunny section
        print('After the battle with the King,', player1.name,
              'proceeds through a barren plans. Until in the distance they see a cave. Could this be the resting place of the treasure they are in search for?\n')
        print('(A)(Yes), (B)(Yes), (C)(......yes)')
        user_choice()

        print('As', player1.name, 'approaches the cave out jumps a super bunny with a love for limbs!!',
              player1.name, 'knows this must be the final boss of this world and the protector of the treasure.\n')
        print('How will they choose to proceed? (A)(Head bravely into battle,(B)(Head fearfully into battle,(C)faint!......do not do this!!! ')
        user_choice()

        if player1.user_input == 'C':
            print('I told you not to do this!', player1.name,
                  'fell when they fainted and hit their head on rock. They are now dead')
            player_health()
        elif player1.user_input == 'B':
            while fight_counter < 3:
                fight_mechanic(3)
                fight_counter += 1
                if battle_result == 1:
                    print(combat_steps['bunny_damage'])
                    limb_status = True
                elif battle_result == 3:
                    break
        else:
            while fight_counter < 2:
                fight_mechanic(3)
                fight_counter += 1
                if battle_result == 1:
                    limb_status = True
                    print(combat_steps['bunny_damage'])
                elif battle_result == 3:
                    break

        if player1.game == False:
            break

        print(player1.name, 'has successfully beat the bunny. As they look up, there it is. Can it be!!! A golden cup!! the Holy Grail!!!! This find will surely make',
              player1.name, 'the most famous individual in the world!! We shall see!')
        player1.item.append('Grail')
        change_bounty(world_items['Grail'])
        change_exp(world_items['Grail'])
        player1.change_health(world_items['Grail'])

        # End section
        print('As', player1.name,
              'perpares to leave, the police show up and ask to talk with', player1.name, '\n')
        print(('(A)(Talk to the police), (B)(Do not talk to the police), (C)(Run!!)'))
        user_choice()

        if player1.user_input == 'A':
            if limb_status == True:
                print('The police wish', player1.name,
                      'the best of luck on their journey, and give them their limbs lost in the great battle with the bunny to take for future adventures.', player1.name, 'goes off into the sunset')
                player1.item.append('Limbs')
                player1.change_health(world_items['Limbs'])
                change_exp(5)
            else:
                print('The police wish', player1.name,
                      'safe travels for their future adventures, off to the sunset they go. \n')
                change_exp(5)
        elif player1.user_input == 'B':
            print('With questioning gaze the police question', player1.name,
                  'however not finding anything immediately susupious, let them go. Now off through the sunset', player1.name, 'goes\n')
        else:
            print('Scared', player1.name,
                  'runs into the sunset, the police take note')
            print(player1.bounty)
            change_bounty(5)
            print(player1.bounty)
        break
