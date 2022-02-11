# LAUREN

def level_5(player):

    Prompts = [
        {'prompt_number': 1,
         'prompt': "You walk into a small village. This village is loaded. Like really loaded. Everyone knows this bank keeps tons of jewels on hand and you're going to relieve them of their burden.  As you walk down the main street to the bank, you start to feel that everyone in town is watching you out of the corner of their eye, but everytime you turn to look, everyone seems to be going about their business as normal. You walk by the doorway of the bank and see several men loitering outside...", 'options': ["A) You head into the bank, as planned.", "B) You keep walking, maybe this isn't the right moment"]},
        {'prompt_number': 2, 'prompt': "You walk by the bank and around the corner, right into the hands of 5 waiting men. The men throw a bag over your head.",
            'options': ['A) Headbutt the nearest man. ', 'B) Attempt to run with the bag on your head']},
        {'prompt_number': 3, 'prompt': "You walk into the bank. And up to the bank clerk. The clerk immediatly draws a bow and tells you to put your hands on your head.",
            'options': ["A) You put your hands up.", "B) You yell, attempting to startle the men. "]}
    ]

    def get_user_input():
        player.user_choice = input(
            'What do you choose? Pick carefully. ').upper()

    def print_options(**kwargs):
        if 'prompt' in kwargs:
            print('\n' + kwargs['prompt'] + '\n')
        if 'options' in kwargs:
            for option in kwargs['options']:
                print(option)

    def choose_option(num):
        return next(item for item in Prompts if item["prompt_number"] == num)

    print_options(**choose_option(1))
    get_user_input()

    def display_choice():
        if(player.user_choice == 'A'):
            print('you picked A')
        elif(player.user_choice == 'B'):
            print('you picked B')
        else:
            print(player.user_choice)
    display_choice()
