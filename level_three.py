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
    world_items = {'Cow': -5,
                   'Limbs': 10,
                   'Crown': 30,
                   }

    def user_choice():  # global for the team
        global user_input
        user_input = input(
            'What do you choose? A, B, or C? Pick carefully ').upper()

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
        print('Will you (A)(choose a drink), (B)(continue to see what other things are to be found), or (C)(see if you can take some coin from the tavern?\n')
        user_choice()

    #enter the world
        
    print(player1.name, 'pops out of the pipe......where an I! You look out and see a tavern.', player1.name, 'is thristy\n')
    enter_python(player1)

    if user_input == 'A':
        print(
            player1.name, ' grab a drink, and hear about an emience treasure directly North of the tavern\n')
        player1.health -= 5
    elif user_input == 'B':
        print(player1.name,
                'travels Northwards in search for this eminence treasure\n')
    elif user_input == 'C':
        print(player1.name, 'heads into the tavern for some coin!!!!\n')

    while user_input == 'A':
        print(player1.name, 'heads out of the tavern, what will',
              player1.name, 'do next?\n')
        enter_python(player1)

    while user_input == 'C':
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
            print(player1.name, 'was unsuccessful, and was kick out by the bartender that say Ne!! Into a dark nasty bog\n')
            battle_success = 0
            break
    
    #next section in the world

    if user_input == 'C':
        global user_input
        user_input = 'B'
    else:
        print('As you head north', player1.name, 'finds a bog! To the East as impenetrable mountains, to the west there is a mystrious fog, which direction will', player1.name,' go?\n')
        print('(A)(West), (B)(North)')
        user_choice()

    if user_input == 'A':
        print(player1.name, 'heads into the mysterious fog, they come across castle. The castle seems deserted./n')
        if player1.exp < 50:
            print('After a long examination', player1.name, 'finds nothing and continues through the fox')
            user_input = 'B'
        elif player1.bounty > 50:
            print(player1.name, 'yells out, and peaking over the top of the castle a group of french soliders appear, knowing who', player1.name, 'is they scream be gone thief. The french throw over the wall and it lands next to', player1.nam, player1.name, 'runs way from the french not wishing more cow!!!!!!', player1.name, 'find that they are completely surroned by the bog found before and continue on through the dark, stinky waters\n')
            player1.item.append('Cow')
            change_health(world_items['Cow'])
            user_input = 'B'
        else:
            print(player1.name, 'yells out, and peaking over the top of the castle a group of french soliders appear. Not knowing who', player1.name, 'is they yell to continue on as visitors are not welcome here!! As', player1.name, 'continues on they run find that they are completely surroned by the bog found before and continue on through the dark, stinky waters\n')
            change_bounty(-5)
            user_input = 'B'
    

    if user_input == 'B':
        print('hi')


        


      
    


