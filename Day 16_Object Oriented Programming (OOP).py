# Object Oriented Programming (OOP)
# Attribute = Data
# Method = Functionality
# Class = Object genrated from the same bleprint.

# car.speed # object.attribute

# car.stop() # object.method
import random

class Pokemon:
    def __init__(self, name, ascii_art, abilities, poke_type, weight, height, link):
        self.name = name
        self.ascii_art = ascii_art
        self.abilities = abilities
        self.poke_type = poke_type
        self.weight = weight
        self.height = height
        self.link = link

    def display(self):
        """Displays the Pokémon's name and ASCII art."""
        print(f"\nYou caught: {self.name}!\n")
        print(self.ascii_art)

    def get_info(self):
        """Displays the Pokémon's details."""
        print(f"Name: {self.name}")
        print(f"Type: {', '.join(self.poke_type)}")
        print(f"Abilities: {', '.join(self.abilities)}")
        print(f"Height: {self.height}m, Weight: {self.weight}kg")
        print(f"More info: {self.link}")

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon_collection = []

    def catch_pokemon(self, pokemon):
        """Adds the caught Pokémon to the trainer's collection."""
        self.pokemon_collection.append(pokemon)
        print(f"{self.name} caught {pokemon.name}!")

    def show_collection(self):
        """Displays all caught Pokémon."""
        if not self.pokemon_collection:
            print(f"{self.name} has no Pokémon yet.")
        else:
            print(f"\n{self.name}'s Pokémon Collection:")
            for pkmn in self.pokemon_collection:
                print(f"- {pkmn.name}")

import pokemon
from pokemon.master import catch_em_all, get_pokemon

# Create a trainer
player = Trainer("Ash")

# Get Pokémon data
pokemons = catch_em_all()
catch = get_pokemon(pokemons=pokemons)

# Extract the first Pokémon ID
pokemon_id = list(catch.keys())[0]
pokemon_data = catch[pokemon_id]

# Create a Pokémon object
wild_pokemon = Pokemon(
    name=pokemon_data["name"].title(),
    ascii_art=pokemon_data["ascii"],
    abilities=pokemon_data["abilities"],
    poke_type=pokemon_data["type"],
    weight=pokemon_data["weight"],
    height=pokemon_data["height"],
    link=pokemon_data["link"]
)

# Display the Pokémon
wild_pokemon.display()

# Catch the Pokémon
player.catch_pokemon(wild_pokemon)

# Show trainer’s Pokémon collection
player.show_collection()

class Pokemon:
    def __init__(self, name, hp, attack_moves):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_moves = attack_moves  # Dictionary of moves

    def attack(self, move, opponent):
        """Perform an attack move on the opponent."""
        if move in self.attack_moves:
            damage = self.attack_moves[move]
            print(f"{self.name} used {move}!")
            opponent.take_damage(damage)
        else:
            print(f"{self.name} doesn't know {move}!")

    def take_damage(self, damage):
        """Reduce HP when taking damage."""
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} fainted!")

    def is_alive(self):
        """Check if the Pokémon is still alive."""
        return self.hp > 0

    def display_hp(self):
        """Display HP in a nice format."""
        hp_bar = "█" * int((self.hp / self.max_hp) * 10)  # HP bar visualization
        return f"{self.name} HP: [{hp_bar:<10}] {self.hp}/{self.max_hp}"
# List of Pokémon with their moves and stats
pokemon_pool = [
    Pokemon("Pikachu", 90, {"Thunderbolt": 25, "Quick Attack": 15, "Iron Tail": 20, "Electro Ball": 30}),
    Pokemon("Charizard", 120, {"Flamethrower": 30, "Dragon Claw": 25, "Air Slash": 20, "Fire Spin": 15}),
    Pokemon("Blastoise", 130, {"Hydro Pump": 35, "Bite": 20, "Water Gun": 15, "Skull Bash": 25}),
    Pokemon("Venusaur", 125, {"Solar Beam": 40, "Razor Leaf": 20, "Sludge Bomb": 25, "Vine Whip": 15}),
    Pokemon("Gengar", 100, {"Shadow Ball": 30, "Lick": 15, "Dream Eater": 35, "Dark Pulse": 25}),
    Pokemon("Machamp", 140, {"Dynamic Punch": 35, "Karate Chop": 20, "Cross Chop": 30, "Bulk Up": 10}),
    Pokemon("Gyarados", 135, {"Hydro Pump": 35, "Bite": 20, "Dragon Rage": 25, "Ice Fang": 30}),
    Pokemon("Alakazam", 110, {"Psychic": 40, "Confusion": 20, "Shadow Ball": 25, "Teleport": 10}),
    Pokemon("Snorlax", 160, {"Body Slam": 35, "Rest": 0, "Crunch": 25, "Hyper Beam": 50}),
    Pokemon("Dragonite", 150, {"Outrage": 40, "Fire Punch": 30, "Thunder Punch": 30, "Aqua Tail": 25}),
]
class Trainer:
    def __init__(self, name):
        self.name = name
        self.team = random.sample(pokemon_pool, 6)  # Randomly select 6 Pokémon
        self.current_pokemon = self.team[0]  # Start with the first Pokémon

    def choose_attack(self, opponent):
        """Trainer selects an attack (for Player or CPU)."""
        if self.name == "Red":
            print("\nChoose an attack:")
            moves = list(self.current_pokemon.attack_moves.keys())
            for i, move in enumerate(moves):
                print(f"{i+1}. {move}")

            choice = int(input("Enter move number: ")) - 1
            if 0 <= choice < len(moves):
                self.current_pokemon.attack(moves[choice], opponent.current_pokemon)
            else:
                print("Invalid choice! Turn skipped.")
        else:
            # CPU chooses randomly
            move = random.choice(list(self.current_pokemon.attack_moves.keys()))
            self.current_pokemon.attack(move, opponent.current_pokemon)

    def switch_pokemon(self):
        """Switch to the next available Pokémon if current one faints."""
        for poke in self.team:
            if poke.is_alive():
                self.current_pokemon = poke
                print(f"{self.name} switched to {poke.name}!")
                return
        print(f"{self.name} has no Pokémon left!")

    def has_pokemon_left(self):
        """Check if the trainer has any Pokémon left alive."""
        return any(poke.is_alive() for poke in self.team)
def battle(trainer1, trainer2):
    print("\n⚔️ Battle Start! ⚔️\n")

    # Show initial teams
    print(f"🔴 {trainer1.name}'s Team: " + ", ".join(p.name for p in trainer1.team))
    print(f"🔵 {trainer2.name}'s Team: " + ", ".join(p.name for p in trainer2.team))

    # Show initial Pokémon
    print(f"\n{trainer1.name} sends out {trainer1.current_pokemon.name}!")
    print(f"{trainer2.name} sends out {trainer2.current_pokemon.name}!\n")

    # Battle loop
    while trainer1.has_pokemon_left() and trainer2.has_pokemon_left():
        print("\n----- Red's Turn -----")
        trainer1.choose_attack(trainer2)

        if not trainer2.current_pokemon.is_alive():
            trainer2.switch_pokemon()
            if not trainer2.has_pokemon_left():
                print(f"\n🏆 {trainer1.name} wins the battle!")
                break

        print("\n----- CPU's Turn -----")
        trainer2.choose_attack(trainer1)

        if not trainer1.current_pokemon.is_alive():
            trainer1.switch_pokemon()
            if not trainer1.has_pokemon_left():
                print(f"\n🏆 {trainer2.name} wins the battle!")
                break

        # Display HP after each turn
        print("\n🔥 HP Status 🔥")
        print(trainer1.current_pokemon.display_hp())
        print(trainer2.current_pokemon.display_hp())

    print("\nBattle Over! 🎉")

# Create Trainers
red = Trainer("Red")
cpu = Trainer("CPU")

# Start the battle
battle(red, cpu)
