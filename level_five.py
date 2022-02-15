# LAUREN

def level_5(player):

    player.item.append('lint from your pockets')
    is_rope_tight = False
    guessed_mother = False

    def get_items():
        if len(player.item) > 1:
            printout = ', '.join(player.item[:-1]) + ', and ' + player.item[-1]
        else:
            printout = player.item[-1]
        return printout

    Prompts = [
        {
            'prompt_label': 'intro',
            'prompt': "You walk into a small village. This village is loaded. Like really loaded. Everyone knows this village bank keeps tons of jewels on hand and you're going to relieve them of their burden.\n As you make your way to the bank, you feel like everyone in town is watching you, but you can't seem to catch anyone in the act. You walk by the doorway of the bank and see several men loitering outside...", 'options': ["A) You head into the bank, as planned.", "B) You keep walking, maybe this isn't the right moment"]
         },{
            'prompt_label': 'alley',
            'prompt': "You walk by the bank and around the corner, right into the hands of 5 waiting men. The men throw a bag over your head.",
            'options': ['A) Headbutt the nearest man. ', "B) Attempt to run even though you can't see"]
        },{
            'prompt_label': 'bank',
            'prompt': "You walk into the bank. And up to the bank clerk. The clerk immediatly draws a bow and tells you to put your hands on your head.",
            'options': ["A) You put your hands up.", "B) You yell, attempting to surprise them. "]
        },{
            'prompt_label': 'hands_up',
            'prompt': "You put your hands up. Someone immediately throws a bag over your head."
        },{
            'prompt_label': 'yell',
            'prompt': "You yell. No one jumps. Someone immediately throws a bag over your head."
         },{
             'prompt_label': 'headbutt',
            'prompt': "You attempt to headbutt the nearest body and hit a brick wall instead. You immediately blackout."
         },{
            'prompt_label': 'run',
            'prompt': "You run headfirst into a brick wall. You immediately blackout."
         },{
            'prompt_label': 'jail',
            'prompt': f"Someone rips the bag off of your head. You find yourself sitting in a small, windowless room. Your arms are tied to the chair. You see the contents of your journey spread out before you on the table. Your {get_items()}. A man is sitting across from you at the table. ", 'options': ["A) Get into a staring contest with the man.", "B) Try to break the ropes"]
         },{
            'prompt_label': 'staring_contest',
            'prompt': "You attempt the beat the man in a staring contest. You win, but your eyes are now watering. You lose 5 health."
         },{
             'prompt_label': 'pull_ropes', 'prompt': "You try to pull on the ropes. They seem to get tighter around your wrists. You lose 5 health."
        }, {
             'prompt_label': 'bounty_reveal',
             'prompt': f"""The man across from you speaks. "Well, well, well. The great {player.name}. You know, you look shorter in real life. Also, your nose is a lot bigger than this wanted poster. Anyways, I bet you're wondering how we caught you. Turns out you can put a price on loyalty. ${player.bounty} to be exact. You'll never guess who tipped us off.""", 'options': ["A) 'Bowser?' ", "B) 'My mother?'"]
         }, {
             'prompt_label': 'bowser',
             'prompt': """"Who??? No! It was your mother." You lose 5 exp points"""
        }, {
             'prompt_label': 'mother',
             'prompt': """"Your... yes. Good guess." You gain 5 exp points"""
        }, {
            'prompt_label': 'escape_attempt', 'prompt': 'You have one last chance to escape and retire to your own private island with all your loot. ', 'options': ['A) You attempt to convince the man that you look nothing like the person in the wanted posters and that you never even knew your mother. ', 'B) You ask the man about his own mother and try to see if you are able to loosen the knot on the rope while he monologues. ']
        }, {
            'prompt_label': 'mother_fail', 'prompt': "The man doesn't buy it. Since you just guessed your own mother turned you in, the ploy fails and you realize with growing horror that you will have to spend the rest of your life in jail. But, at least you'll never have to see your mother again, the traitor."
        }, {
            'prompt_label': 'mother_exp_fail', 'prompt': "Your experience isn't high enough. The man doesn't buy it and you realize with growing horror that you will have to spend the rest of your life in jail. Your only regret is that you didn't steal more along the way. Maybe if you had, you'd have escaped."
        }, {
            'prompt_label': 'mother_success', 'prompt': "Your experience is high enough that the man believes you. It helps that the sketch artist never got your nose quite right. The man unties you and says you can go. You leave the jailhouse with no regets for your life of crime, but deep down you know you'll never truly repair your relationship with your mother. "
        }, {
            'prompt_label': 'rope_fail', 'prompt': "You try to untie the knot, but, unfortunately, you made it too tight when you tried to break the ropes earlier. You can't untie them. You start to realize that you'll spend the rest of your life in jail. You have no regrets, except maybe pulling on the ropes earlier. "
        }, {
            'prompt_label': 'rope_exp_fail', 'prompt': "You try to untie the rope, but unfortunately your experience isn't high enough and the man notices what you're doing. The man walks over, tightens the ropes, and you realize that you're going to jail for the rest of your life. Your only regret is that you didn't steal more along the way. Maybe if you had, you'd have escaped."
        }, {
            'prompt_label': 'rope_success', 'prompt': "You try to untie the rope. Your experience is high enough that you're able to do so without the man noticing. While monologuing, the man realizes it's Mother's Day. He steps outside of the room to call his mother and you make quick work of grabbing your stuff. You leave the room and slip into a group of tourists sightseeing the local police station. You live to steal another day. "
        }
    

    ]

    def get_user_input():
        while True:
            player.user_choice = input(
                '\nWhat do you choose? Pick carefully. ').upper()
            print('________________________________________________')
            if player.user_choice == 'A' or player.user_choice == "B":
                break
            else:
                print('Not a valid option. Please choose again. ')
                print('________________________________________________')
                continue

    def continue_input():
        player.user_choice = input('Press enter to continue').upper()
        print('________________________________________________')

    def print_options(**kwargs):
        if 'prompt' in kwargs:
            print('\n' + kwargs['prompt'] + '\n')
        if 'options' in kwargs:
            for option in kwargs['options']:
                print(option)

    def get_option(label):
        return next(option for option in Prompts if option["prompt_label"] == label)

# introduction

    print_options(**get_option('intro'))
    get_user_input()


    if player.user_choice == 'A':
        print_options(**get_option('bank'))
        get_user_input()
        if player.user_choice == 'A':
            print_options(**get_option('hands_up'))
        elif player.user_choice == 'B':
            print_options(**get_option('yell'))
    elif player.user_choice == 'B':
        print_options(**get_option('alley'))
        get_user_input()
        if player.user_choice == 'A':
            print_options(**get_option('headbutt'))
        if player.user_choice == 'B':
            print_options(**get_option('run'))
    continue_input()

#goes to jail
    print_options(**get_option('jail'))
    get_user_input()
    if player.user_choice == 'A':
        print_options(**get_option('staring_contest'))
    else:
        print_options(**get_option('pull_ropes'))
        is_rope_tight = True
    player.change_health(-5)
    continue_input()

    print_options(**get_option('bounty_reveal'))
    get_user_input()

    if player.user_choice == 'A':
        print_options(**get_option('bowser'))
        player.change_exp(-5)
    if player.user_choice == 'B':
        print_options(**get_option('mother'))
        player.change_exp(5)
        guessed_mother = True
    continue_input()

#escape attempt

    print_options(**get_option('escape_attempt'))
    get_user_input()
    if player.user_choice == 'A':
        if guessed_mother == True:
            print_options(**get_option('mother_fail'))
        elif player.exp < 75:
            print_options(**get_option('mother_exp_fail'))
        else: 
            print_options(**get_option('mother_success'))
    if player.user_choice == 'B':
        if is_rope_tight == True:
            print_options(**get_option('rope_fail'))
        elif player.exp < 75:
            print_options(**get_option('rope_exp_fail'))
        else:
            print_options(**get_option('rope_success'))


