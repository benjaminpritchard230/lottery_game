from functions import get_player_numbers, get_winning_numbers, count_matching_numbers, decide_prize, get_player_thunderball, does_thunderball_match, get_winning_thunderball



player_numbers = get_player_numbers()
player_thunderball = get_player_thunderball()
winning_numbers = get_winning_numbers()
winning_thunderball = get_winning_thunderball()
matching_thunderball = does_thunderball_match(player_thunderball, winning_thunderball)



print(f'Player numbers: {player_numbers}.')
print(f'Winning numbers: {winning_numbers}')
print(f'Player Thunderball: {player_thunderball}')
print(f'Winning thunderball: {winning_thunderball}')


matching_numbers = count_matching_numbers(player_numbers, winning_numbers)
print(f'Matching numbers: {matching_numbers}')

prize = decide_prize(matching_numbers, matching_thunderball=False)
print(f'Prize: {prize}.')