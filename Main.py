import random
from data import pokemon_list
from battle import start_battle

player_team = random.sample(pokemon_list, 3)
computer_team = random.sample([i for i in pokemon_list if i not in player_team], 3)

print("Welcome to Pokémon Battle!\n")
print("Your Team:")

start_battle(player_team, computer_team)
