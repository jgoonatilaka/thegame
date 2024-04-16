import json
import random

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

class Player:
    def __init__(self, name, playerType):
        self.name = name
        self.playerType = playerType
        self.health = self.totalHealth(playerType)
        self.weapon = self.chooseWeapon(playerType)
        self.armor = self.chooseArmor(playerType)
        self.inventory = {}

    def chooseWeapon(self, playerType):
        if playerType == "wizard":
            return Weapon("Staff", 10)
        elif playerType == "soldier":
            return Weapon("Sword", 15)
        elif playerType == "elf":
            return Weapon("Wand", 5)

    def chooseArmor(self, playerType):
        if playerType == "wizard":
            return Armor("Robe", 5)
        elif playerType == "soldier":
            return Armor("PlateArmor", 10)
        elif playerType == "elf":
            return Armor("Cloak", 3)
    
    def totalHealth(self, playerType):
        if playerType == "wizard":
            return 15
        elif playerType == "soldier":
            return 20
        elif playerType == "elf":
            return 13

    def addItemToInventory(self, itemName, quantity=1):
        if itemName in self.inventory:
            self.inventory[itemName] += quantity
        else:
            self.inventory[itemName] = quantity

    def showInventory(self):
        if self.inventory:
            print(f"{self.name}'s Inventory:")
            for item, quantity in self.inventory.items():
                print(f"{item}: {quantity}")
        else:
            print("Your inventory is empty.")

    def saveInventory(self):
        with open(f"{self.name}_inventory.json", 'w') as file:
            json.dump(self.inventory, file, indent=4)
        print("Inventory saved successfully.")

class Enemy:
    def __init__(self, name, health, damageRange, lootTable):
        self.name = name
        self.health = health
        self.damageRange = damageRange
        self.lootTable = lootTable

    def dealDamage(self):
        return random.choice(self.damageRange)

    def dropLoot(self):
        return self.lootTable

# List of enemies
enemies = [
    Enemy("Demon Monkey", 30, (5, 7, 8), {"janiduCoin": 10, "Golden Banana": 1, "Monkey Tail": 1}),
    Enemy("The Big Bear Man", 20, (4, 6, 10), {"janiduCoin": 10, "Bear Claw": 1, "Pooh's Hunny": 1}),
    Enemy("The SoundCloud Rapper", 40, (7, 12), {"janiduCoin": 10, "Mixtape": 1, "EP": 1}),
    Enemy("Elon Musk", 100, (1, 2, 3), {"janiduCoin": 100, "Tesla": 1, "X": 1, "BOSS COIN": 1})
]

def mainMenu():
    print("Welcome to the Garbage Game!")
    print("Choose your player:")
    print("1. Wizard")
    print("2. Soldier")
    print("3. Elf")
    playerTypeChoice = input("Choose your player: ")
    playerTypeDict = {"1": "wizard", "2": "soldier", "3": "elf"}
    playerType = playerTypeDict.get(playerTypeChoice)
    if playerType:
        player = Player(name="Janidu", playerType=playerType)
        showPlayerDetails(player)
        selectEnemyAndFight(player)
    else:
        print("Invalid choice, try again.")
        mainMenu()

def showPlayerDetails(player):
    print("\nYour player details:")
    print(f"Player Type: {player.playerType.capitalize()}")
    print(f"Your Total Health: {player.health}")
    print(f"Weapon: {player.weapon.name} (Damage: {player.weapon.damage})")
    print(f"Armor: {player.armor.name} (Defense: {player.armor.defense})")
    print("You are now ready to begin your adventure!")

def selectEnemyAndFight(player):
    print("\nEnemies:")
    for i, enemy in enumerate(enemies, 1):
        print(f"{i}. {enemy.name} (Health: {enemy.health})")
    enemyChoice = input("Choose an enemy: ")
    enemyIndex = int(enemyChoice) - 1
    if 0 <= enemyIndex < len(enemies):
        battle(player, enemies[enemyIndex])
    else:
        print("Invalid choice, try again.")
        selectEnemyAndFight(player)

def battle(player, enemy):
    print(f"\nYou are fighting {enemy.name}!")
    while player.health > 0 and enemy.health > 0:
        print(f"\n{enemy.name}'s Health: {enemy.health}")
        print(f"{player.name}'s Health: {player.health}")
        print("What do you want to do?")
        print("1. Attack")
        print("2. View Inventory")
        print("3. Run away like a baby")
        choice = input("What will you do? ")
        if choice == "1":
            damage = player.weapon.damage
            enemy.health -= damage
            print(f"You attack {enemy.name} with your {player.weapon.name}, dealing {damage} damage!")
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated!")
                loot = enemy.dropLoot()
                for item, quantity in loot.items():
                    player.addItemToInventory(item, quantity)
                    print("Open Inventory to see dropped loot")
                postBattleMenu(player)
                break
            enemyDamage = enemy.dealDamage()
            player.health -= enemyDamage
            print(f"{enemy.name} attacks you, dealing {enemyDamage} damage!")
            if player.health <= 0:
                print("You have been defeated.")
        elif choice == "2":
            player.showInventory()

        elif choice == "3":
            print("You ran away")
            postBattleMenu(player)
        else:
            print("Invalid choice, try again.")
    if player.health <= 0:
        print("\nGame Over.")

def postBattleMenu(player):
    print("\nWhat would you like to do now?")
    print("1. Fight another enemy")
    print("2. View inventory")
    print("3. Save inventory")
    print("4. Exit game")
    choice = input("Enter your choice: ")
    if choice == "1":
        selectEnemyAndFight(player)
    elif choice == "2":
        player.showInventory()
        postBattleMenu(player)
    elif choice == "3":
        player.saveInventory()
        postBattleMenu(player)
    elif choice == "4":
        print("Thanks for playing! Goodbye.")
    else:
        print("Invalid choice, try again.")
        postBattleMenu(player)

mainMenu()
