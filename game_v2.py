#This is a simplified version made for 2 players.
#Later i could make a game for even more like 4 players.
import random

class Character:
    def __init__(self, name, health):
        self.health = health
        self.name = name
        self.defense = self.dmg = random.randint(1, 5)
        self.dmg = random.randint(10, 20)
        
    def chara_information(self):
        return f"Name: {self.name}    Health: {self.health}    Defense: {self.defense}    Dmg: {self.dmg}"
    
    def __str__(self):
        return self.chara_information()

    def take_damage(self, damage):
        old_health = self.health
        self.health -= (damage - self.defense)
        print(f"{self.name}'s health was {old_health}. Now it is {self.health}.")

    def attack(self, target):
        print(f"{self.name} is attacking {target.name}!")
        target.take_damage(self.dmg)

# Function to print the characters from character_list TODO maybe an easier way to accomplish this?
def print_character_list(character_list):
    for i, character in enumerate(character_list, start=1):
        print(f"{i} | {character}")

# Start of the game             
print("Welcome to this game.\n")

# Creation of characters and storing them in a list 
character_list = []

for i in range(2):
    name = input(f"\nEnter name for character {i + 1}:\n")
    character = Character(name, 100)
    character_list.append(character)
    print(character)

print_character_list(character_list)
# Loop for attacking and choosing which character to play as during that turn.
while True:
    player1 = input("\nType which character 'Number' you want to play as: ")
    
    if player1 == "1":
        print(f"You chose the first character \n{character_list[0]}")
        break

print("\nFight over!")