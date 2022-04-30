def get_player_numbers():
    """Gets the player's chosen numbers."""
    player_numbers = []
    while len(player_numbers) < 5:
        while True:
            while True:
                try:
                    new_number = int(input('Please enter a number between 1 and 20:  '))
                except ValueError:
                    print('Please enter a valid input.')
                    continue
                break
            if (new_number > 20) or (new_number < 0):
                print('Please enter a valid input.')
                continue
            elif isinstance(new_number, int) is False:
                print('Please enter a valid input.')
                continue
            else:
                break
        if new_number not in player_numbers:
            player_numbers.append(new_number)
        else:
            print('That number has already been chosen.')
            continue
    return(player_numbers)

def get_player_thunderball():
    """Gets the player's chosen Thunderball number."""
    thunderball = 0
    while thunderball == 0:
        while True:
            try: 
                new_thunderball = int(input('Please choose a Thunderball between 1 and 20\n'))
            except ValueError:
                print('Please enter a valid input.')
                continue
            break
        if (new_thunderball > 20) or (new_thunderball < 0):
            print('Please enter a valid input.')
        else:
            thunderball = new_thunderball
    return thunderball


def get_winning_numbers():
    """Generates a list of random, unique winning numbers."""
    import random
    winning_numbers = []
    while len(winning_numbers) < 5:
        x = random.randint(0, 21)
        if x not in winning_numbers:
            winning_numbers.append(x)
        else: continue  
    return winning_numbers

def get_winning_thunderball():
    """Generates a list of random, unique winning numbers."""
    import random
    winning_thunderball = random.randint(0, 20)  
    return winning_thunderball

def count_matching_numbers(list1, list2):
    """Counts how many numbers in list1 are present in list2."""
    matching_numbers = len(set(list1) & set(list2))
    return matching_numbers

def does_thunderball_match(player_thunderball, winning_thunderball):
    """Checks if the player has chosen the winning Tunderball."""
    if player_thunderball == winning_thunderball:
        matching_thunderball = True
    else:
        matching_thunderball = False
    return matching_thunderball

def decide_prize(matching_numbers, matching_thunderball=False):
    """Assigns a prize based on number of matching numbers."""
    if matching_numbers == 5:
        if matching_thunderball is True:
            prize = 500000
        else:
            prize = 5000
    elif matching_numbers == 4:
        if matching_thunderball is True:
            prize = 250
        else:
            prize = 100
    elif matching_numbers == 3:
        if matching_thunderball is True:
            prize = 20
        else:
            prize = 10
    elif matching_numbers == 2:
        if matching_thunderball is True:
            prize = 10
        else:
            prize = 0
    elif matching_numbers == 1:
        if matching_thunderball is True:
            prize = 5
        else:
            prize = 0
    elif matching_numbers == 0:
        if matching_thunderball is True:
            prize = 3
        else:
            prize = 0
    else:
        prize = 0
    return prize

