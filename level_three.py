def level_3(player1):
    user_input = ''

    print(player1.name, 'pops out of the pipe......where an I! You look out and see a tavern.',
          player1.name, 'is thirsty.')
    user_input = input(
        'Will you (A)(choose a drink), (B)(continue to see what other things are to be found), or (C)(see if you can take some coin from the tavern?').upper()

    if user_input == 'A':
        print('You grab a drink, and here about an emience treasure directly North of the tavern')
        player1.health -= 5
    elif user_input == 'B':
        print('You travel Northwards in search for this eminence treasure')
    elif user_input == 'C':
        print('You head into the tavern for some coin!!!!')

    
    while user_input == 'C':
        print('hi')
    
