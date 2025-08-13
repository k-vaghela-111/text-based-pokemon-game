# Type advantage chart
type_advantage = {
    "Grass": ["Water", "Ground", "Rock"],
    "Fire": ["Grass", "Bug", "Ice", "Steel"],
    "Water": ["Fire", "Ground", "Rock"],
    "Electric": ["Water", "Flying"],
    "Bug": ["Grass", "Psychic", "Dark"],
    "Flying": ["Grass", "Bug", "Fighting"],
    "Poison": ["Grass", "Fairy"],
    "Ground": ["Electric", "Fire", "Poison", "Rock", "Steel"],
    "Normal": [],
    "Fighting": ["Normal", "Rock", "Ice", "Dark", "Steel"],
    "Psychic": ["Fighting", "Poison"],
    "Rock": ["Fire", "Flying", "Bug", "Ice"],
    "Ice": ["Grass", "Flying", "Ground", "Dragon"],
    "Dragon": ["Dragon"],
    "Steel": ["Rock", "Ice", "Fairy"],
    "Dark": ["Psychic", "Ghost"],
    "Fairy": ["Fighting", "Dragon", "Dark"],
    "Ghost": ["Psychic", "Ghost"]
}


pokemon_list = [
    {"name": "Charizard", "type": "Fire", "hp": 150, "attacks": [
        {"name": "Flamethrower", "power": 30},
        {"name": "Fire Blast", "power": 35},
        {"name": "Ember", "power": 25}
    ]},
    {"name": "Blastoise", "type": "Water", "hp": 160, "attacks": [
        {"name": "Hydro Pump", "power": 35},
        {"name": "Water Gun", "power": 25},
        {"name": "Surf", "power": 30}
    ]},
    {"name": "Venusaur", "type": "Grass", "hp": 160, "attacks": [
        {"name": "Vine Whip", "power": 25},
        {"name": "Solar Beam", "power": 35},
        {"name": "Leaf Blade", "power": 30}
    ]},
    {"name": "Pikachu", "type": "Electric", "hp": 130, "attacks": [
        {"name": "Thunderbolt", "power": 30},
        {"name": "Thunder", "power": 35},
        {"name": "Spark", "power": 25}
    ]},
    {"name": "Gengar", "type": "Ghost", "hp": 140, "attacks": [
        {"name": "Shadow Ball", "power": 30},
        {"name": "Night Shade", "power": 25},
        {"name": "Hex", "power": 35}
    ]},
    {"name": "Machamp", "type": "Fighting", "hp": 170, "attacks": [
        {"name": "Close Combat", "power": 35},
        {"name": "Karate Chop", "power": 25},
        {"name": "Dynamic Punch", "power": 30}
    ]},
    {"name": "Alakazam", "type": "Psychic", "hp": 140, "attacks": [
        {"name": "Psychic", "power": 35},
        {"name": "Confusion", "power": 25},
        {"name": "Psybeam", "power": 30}
    ]},
    {"name": "Onix", "type": "Rock", "hp": 160, "attacks": [
        {"name": "Rock Throw", "power": 25},
        {"name": "Stone Edge", "power": 35},
        {"name": "Rock Slide", "power": 30}
    ]},
    {"name": "Snorlax", "type": "Normal", "hp": 180, "attacks": [
        {"name": "Body Slam", "power": 30},
        {"name": "Hyper Beam", "power": 35},
        {"name": "Headbutt", "power": 25}
    ]},
    {"name": "Lapras", "type": "Ice", "hp": 160, "attacks": [
        {"name": "Ice Beam", "power": 30},
        {"name": "Blizzard", "power": 35},
        {"name": "Frost Breath", "power": 25}
    ]},
    {"name": "Scyther", "type": "Bug", "hp": 150, "attacks": [
        {"name": "X-Scissor", "power": 30},
        {"name": "Bug Bite", "power": 25},
        {"name": "Fury Cutter", "power": 35}
    ]},
    {"name": "Aerodactyl", "type": "Flying", "hp": 150, "attacks": [
        {"name": "Wing Attack", "power": 25},
        {"name": "Hurricane", "power": 35},
        {"name": "Aerial Ace", "power": 30}
    ]},
    {"name": "Kangaskhan", "type": "Normal", "hp": 170, "attacks": [
        {"name": "Double-Edge", "power": 35},
        {"name": "Stomp", "power": 25},
        {"name": "Mega Punch", "power": 30}
    ]},
    {"name": "Hitmonlee", "type": "Fighting", "hp": 160, "attacks": [
        {"name": "High Jump Kick", "power": 35},
        {"name": "Low Kick", "power": 25},
        {"name": "Brick Break", "power": 30}
    ]},
    {"name": "Electabuzz", "type": "Electric", "hp": 150, "attacks": [
        {"name": "Thunder Punch", "power": 30},
        {"name": "Shock Wave", "power": 25},
        {"name": "Volt Tackle", "power": 35}
    ]},
    {"name": "Magmar", "type": "Fire", "hp": 150, "attacks": [
        {"name": "Flame Wheel", "power": 25},
        {"name": "Lava Plume", "power": 30},
        {"name": "Overheat", "power": 35}
    ]},
    {"name": "Jynx", "type": "Ice", "hp": 140, "attacks": [
        {"name": "Ice Punch", "power": 30},
        {"name": "Aurora Beam", "power": 25},
        {"name": "Glaciate", "power": 35}
    ]},
    {"name": "Pinsir", "type": "Bug", "hp": 150, "attacks": [
        {"name": "Bug Buzz", "power": 30},
        {"name": "Leech Life", "power": 25},
        {"name": "Megahorn", "power": 35}
    ]},
    {"name": "Tauros", "type": "Normal", "hp": 160, "attacks": [
        {"name": "Horn Attack", "power": 25},
        {"name": "Giga Impact", "power": 35},
        {"name": "Body Slam", "power": 30}
    ]},
    {"name": "Articuno", "type": "Ice", "hp": 160, "attacks": [
        {"name": "Freeze-Dry", "power": 25},
        {"name": "Ice Beam", "power": 30},
        {"name": "Blizzard", "power": 35}
    ]},
    {"name": "Zapdos", "type": "Electric", "hp": 160, "attacks": [
        {"name": "Thunder Shock", "power": 25},
        {"name": "Discharge", "power": 30},
        {"name": "Thunder", "power": 35}
    ]},
    {"name": "Moltres", "type": "Fire", "hp": 160, "attacks": [
        {"name": "Flame Charge", "power": 25},
        {"name": "Fire Spin", "power": 30},
        {"name": "Inferno", "power": 35}
    ]},
    {"name": "Dragonite", "type": "Dragon", "hp": 170, "attacks": [
        {"name": "Dragon Breath", "power": 25},
        {"name": "Dragon Claw", "power": 30},
        {"name": "Outrage", "power": 35}
    ]},
    {"name": "Mewtwo", "type": "Psychic", "hp": 170, "attacks": [
        {"name": "Psystrike", "power": 35},
        {"name": "Confusion", "power": 25},
        {"name": "Psychic", "power": 30}
    ]},
    {"name": "Raichu", "type": "Electric", "hp": 150, "attacks": [
        {"name": "Volt Switch", "power": 25},
        {"name": "Thunderbolt", "power": 30},
        {"name": "Zap Cannon", "power": 35}
    ]},
    {"name": "Gyarados", "type": "Water", "hp": 170, "attacks": [
        {"name": "Aqua Tail", "power": 30},
        {"name": "Hydro Pump", "power": 35},
        {"name": "Waterfall", "power": 25}
    ]},
    {"name": "Kabutops", "type": "Rock", "hp": 150, "attacks": [
        {"name": "Stone Edge", "power": 35},
        {"name": "Rock Blast", "power": 30},
        {"name": "Smack Down", "power": 25}
    ]},
    {"name": "Omastar", "type": "Rock", "hp": 150, "attacks": [
        {"name": "Rock Tomb", "power": 25},
        {"name": "Ancient Power", "power": 30},
        {"name": "Stone Edge", "power": 35}
    ]},
    {"name": "Sudowoodo", "type": "Rock", "hp": 160, "attacks": [
        {"name": "Rock Throw", "power": 25},
        {"name": "Rock Slide", "power": 30},
        {"name": "Head Smash", "power": 35}
    ]},
    {"name": "Typhlosion", "type": "Fire", "hp": 150, "attacks": [
        {"name": "Flame Wheel", "power": 25},
        {"name": "Eruption", "power": 35},
        {"name": "Lava Plume", "power": 30}
    ]},
    {"name": "Feraligatr", "type": "Water", "hp": 160, "attacks": [
        {"name": "Water Gun", "power": 25},
        {"name": "Aqua Tail", "power": 30},
        {"name": "Hydro Cannon", "power": 35}
    ]},
    {"name": "Sceptile", "type": "Grass", "hp": 150, "attacks": [
        {"name": "Leaf Blade", "power": 30},
        {"name": "Energy Ball", "power": 25},
        {"name": "Solar Beam", "power": 35}
    ]},
    {"name": "Blaziken", "type": "Fire", "hp": 160, "attacks": [
        {"name": "Blaze Kick", "power": 30},
        {"name": "Flare Blitz", "power": 35},
        {"name": "Fire Punch", "power": 25}
    ]},
    {"name": "Swampert", "type": "Water", "hp": 170, "attacks": [
        {"name": "Muddy Water", "power": 30},
        {"name": "Waterfall", "power": 25},
        {"name": "Hydro Pump", "power": 35}
    ]},
    {"name": "Torterra", "type": "Grass", "hp": 170, "attacks": [
        {"name": "Leaf Storm", "power": 35},
        {"name": "Razor Leaf", "power": 25},
        {"name": "Seed Bomb", "power": 30}
    ]},
    {"name": "Infernape", "type": "Fire", "hp": 150, "attacks": [
        {"name": "Fire Punch", "power": 25},
        {"name": "Flare Blitz", "power": 35},
        {"name": "Flamethrower", "power": 30}
    ]},
    {"name": "Empoleon", "type": "Water", "hp": 160, "attacks": [
        {"name": "Water Pulse", "power": 25},
        {"name": "Aqua Jet", "power": 30},
        {"name": "Hydro Pump", "power": 35}
    ]},
    {"name": "Serperior", "type": "Grass", "hp": 150, "attacks": [
        {"name": "Vine Whip", "power": 25},
        {"name": "Leaf Blade", "power": 30},
        {"name": "Solar Beam", "power": 35}
    ]},
    {"name": "Samurott", "type": "Water", "hp": 160, "attacks": [
        {"name": "Surf", "power": 30},
        {"name": "Aqua Tail", "power": 25},
        {"name": "Hydro Pump", "power": 35}
    ]},
    {"name": "Chesnaught", "type": "Grass", "hp": 170, "attacks": [
        {"name": "Needle Arm", "power": 25},
        {"name": "Seed Bomb", "power": 30},
        {"name": "Wood Hammer", "power": 35}
    ]},
    {"name": "Delphox", "type": "Fire", "hp": 150, "attacks": [
        {"name": "Flamethrower", "power": 30},
        {"name": "Fire Spin", "power": 25},
        {"name": "Overheat", "power": 35}
    ]},
    {"name": "Greninja", "type": "Water", "hp": 150, "attacks": [
        {"name": "Water Shuriken", "power": 25},
        {"name": "Surf", "power": 30},
        {"name": "Hydro Cannon", "power": 35}
    ]},
    {"name": "Decidueye", "type": "Grass", "hp": 150, "attacks": [
        {"name": "Leaf Blade", "power": 30},
        {"name": "Razor Leaf", "power": 25},
        {"name": "Solar Beam", "power": 35}
    ]},
    {"name": "Inteleon", "type": "Water", "hp": 140, "attacks": [
        {"name": "Snipe Shot", "power": 35},
        {"name": "Water Gun", "power": 25},
        {"name": "Surf", "power": 30}
    ]}
]
