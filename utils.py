def choose_pokemon(team):
    for i , p in enumerate(team):
        print(f"{i + 1}. {p['name']} ({p['type']}) - HP: {p['hp']}")
    choice = int(input("Choose your Pokémon: ")) - 1
    return team.pop(choice)

def show_attacks(pokemon):
    print("\nChoose your attack:")
    for i, atk in enumerate(pokemon["attacks"]):
        print(f"{i + 1}. {atk['name']} (Power: {atk['power']})")

