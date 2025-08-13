import random
from data import type_advantage
from utils import choose_pokemon, show_attacks

def start_battle(player_team, computer_team):
    player_pokemon = choose_pokemon(player_team)
    computer_pokemon = computer_team.pop(0)
    computer_hp = computer_pokemon["hp"]

    print(f"\nYou chose {player_pokemon['name']} ({player_pokemon['type']})")
    print(f"Computer chose {computer_pokemon['name']} ({computer_pokemon['type']})")

    while True:
        print(f"\n🔄 {player_pokemon['name']} HP: {player_pokemon['hp']} | {computer_pokemon['name']} HP: {computer_hp}")
        action = input("Choose action: [A] Attack or [S] Switch: ").lower()

        if action == "s":
            if not player_team:
                print("❌ No other Pokémon to switch to!")
                continue
            player_team.append(player_pokemon)
            print("\n🎮 Your Team:")
            player_pokemon = choose_pokemon(player_team)

            # Computer free attack
            comp_attack = random.choice(computer_pokemon["attacks"])
            comp_damage = comp_attack["power"]  # changed here
            if player_pokemon["type"] in type_advantage.get(computer_pokemon["type"], []):
                comp_damage *= 2
                print(f"⚡ {computer_pokemon['name']} has type advantage! Power boosted.")
            elif computer_pokemon["type"] in type_advantage.get(player_pokemon["type"], []):
                comp_damage = int(comp_damage * 0.75)
                print(f"⚡ {computer_pokemon['name']} has type disadvantage! Power reduced.")
            player_pokemon["hp"] -= comp_damage
            print(f"{computer_pokemon['name']} attacked during switch! {player_pokemon['name']} HP is now {max(player_pokemon['hp'], 0)}")
            if player_pokemon["hp"] <= 0:
                print(f"\n💀 {player_pokemon['name']} is down.")
                if player_team:
                    print("\n🎮 Your Team:")
                    player_pokemon = choose_pokemon(player_team)
                    continue
                else:
                    print("😢 All your Pokémons are down. You lose!")
                    break
            continue

        elif action == "a":
            show_attacks(player_pokemon)
            atk_choice = int(input("Choose your attack (1-3): ")) - 1
            attack = player_pokemon["attacks"][atk_choice]
            damage = attack["power"]  # changed here

            if computer_pokemon["type"] in type_advantage.get(player_pokemon["type"], []):
                damage *= 2
                print("🔥 Type advantage! Power boosted.")
            elif player_pokemon["type"] in type_advantage.get(computer_pokemon["type"], []):
                damage = int(damage * 0.75)
                print("🌱 Type disadvantage! Power reduced.")

            computer_hp -= damage
            print(f"{player_pokemon['name']} used {attack['name']}! {computer_pokemon['name']} HP is now {max(computer_hp, 0)}")

            if computer_hp <= 0:
                print(f"\n✅ {computer_pokemon['name']} is down.")
                if computer_team:
                    computer_pokemon = computer_team.pop(0)
                    computer_hp = computer_pokemon["hp"]
                    print(f"\n🤖 Computer sends out {computer_pokemon['name']} ({computer_pokemon['type']})!")
                    continue
                else:
                    print("\n🏆 You win! All computer Pokémons are down.")
                    break

            # Computer's turn
            comp_attack = random.choice(computer_pokemon["attacks"])
            comp_damage = comp_attack["power"]  # changed here
            if player_pokemon["type"] in type_advantage.get(computer_pokemon["type"], []):
                comp_damage *= 2
                print(f"{computer_pokemon['name']} has type advantage! Power boosted.")
            elif computer_pokemon["type"] in type_advantage.get(player_pokemon["type"], []):
                comp_damage = int(comp_damage * 0.75)
                print(f"{computer_pokemon['name']} has type disadvantage! Power reduced.")

            player_pokemon["hp"] -= comp_damage
            print(f"{computer_pokemon['name']} used {comp_attack['name']}! {player_pokemon['name']} HP is now {max(player_pokemon['hp'], 0)}")

            if player_pokemon["hp"] <= 0:
                print(f"\n💀 {player_pokemon['name']} is down.")
                if player_team:
                    print("\n🎮 Your Team:")
                    player_pokemon = choose_pokemon(player_team)
                else:
                    print("😢 All your Pokémons are down. You lose!")
                    break
        else:
            print("❓ Invalid action. Please choose [A] Attack or [S] Switch.")
