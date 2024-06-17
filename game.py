import random

class Character:
    def __init__(self, dmg, name):
        self.health = random.randint(1, 100)
        self.dmg = dmg
        self.name = name

    def chara_information(self):
        return f"Name: {self.name}    Health: {self.health}    Dmg: {self.dmg}"
    
    def __str__(self):
        return self.chara_information()

    def take_damage(self, damage):
        old_health = self.health
        self.health -= damage
        print(f"{self.name}'s health was {old_health}. Now it is {self.health}.")

    def attack(self, target):
        print(f"{self.name} is attacking {target.name}!")
        target.take_damage(self.dmg)

# Function to print the characters from character_list TODO maybe an easier way to accomplish this?
def print_character_list(character_list):
    for i, character in enumerate(character_list, start=1):
        print(f"character{i} | {character}")

# Start of the game             
print("Welcome to this game.\r\n")

# Creation of characters and storing them in a list 
character_list = []
character_amount = int(input("How many characters do you want to create (Enter a number)? "))

for i in range(character_amount):
    name = input(f"\r\nEnter name for character {i + 1}:\r\n")
    character = Character(10, name)
    character_list.append(character)
    print(character)

# Loop for attacking and choosing which character to play as during that turn.
while True:
    player_name = input("\r\nType which character 'Name' you want to play as: ").lower()
    enemy_name = input("\r\nType which character will be your enemy: ").lower()
    
    player_found = None
    enemy_found = None
    # Find the objects in the character_list
    for character in character_list:
        if character.name.lower() == player_name:
            player_found = character
        if character.name.lower() == enemy_name:
            enemy_found = character
    
    # Check if both player and enemy names are valid
    if player_found is not None and enemy_found is not None:
        if player_found != enemy_found:
            attack_or_not = input(f"Do you want {player_found.name} to attack {enemy_found.name}? (yes/no): \n").lower()
            if attack_or_not == "yes":
                player_found.attack(enemy_found)
                if enemy_found.health <= 0:
                    print(f"{enemy_found.name} is defeated!")
                    break
            elif attack_or_not == "no":
                break
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
        else:
            print("You can't fight yourself!")
    else:
        print("\r\nInvalid input. Either player or enemy was not from the list.")
        print("Characters available:")
        print_character_list(character_list)
        print("Type the 'Name' of a character")
print("\r\nFight over!")