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
    def __init__(self, name, player_type):
        self.name = name
        self.player_type = player_type
        self.health = self.totalHealth(player_type)
        self.weapon = self.choose_weapon(player_type)
        self.armor = self.choose_armor(player_type)
        self.inventory = {}  

    def choose_weapon(self, player_type):
        if player_type == "wizard":
            return Weapon("Staff", 10)
        elif player_type == "soldier":
            return Weapon("Sword", 15)
        elif player_type == "elf":
            return Weapon("Wand", 5)

    def choose_armor(self, player_type):
        if player_type == "wizard":
            return Armor("Robe", 5)
        elif player_type == "soldier":
            return Armor("PlateArmor", 10)
        elif player_type == "elf":
            return Armor("Cloak", 3)
    
    def totalHealth(self, player_type):
        if player_type == "wizard":
            self.health = 15
        elif player_type == "soldier":
            self.health = 20
        elif player_type == "elf":
            self.health = 13

    def add_item_to_inventory(self, item_name, quantity=1):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def remove_item_from_inventory(self, item_name, quantity=1):
        if item_name in self.inventory and self.inventory[item_name] >= quantity:
            self.inventory[item_name] -= quantity
            if self.inventory[item_name] <= 0:
                del self.inventory[item_name]
            return True
        return False

    def show_inventory(self):
        if self.inventory:
            print(f"{self.name}'s Inventory:")
            for item, quantity in self.inventory.items():
                print(f"{item}: {quantity}")
        else:
            print("Your inventory is empty.")


class Enemy:
    def __init__(self, name, health, damageRange, lootTable):
        self.name = name
        self.health = health
        self.damage_range = damageRange
        self.loot_table = lootTable

    def deal_damage(self):
        return random.choice(self.damage_range)

    def drop_loot(self):
        return self.loot_table



#List of enemies: Name, 

enemies = [
    Enemy("Demon Monkey", 30, (5, 7, 8), {"janiduCoin": 10, "Golden Banana": 1, "Monkey Tail": 1, "Demon Soul or something idk": 1, "another item": 1, "im running out of ideas": 1, "what do you call these": 1, "potion i guess": 1, "banana 2": 1, "another banana": 1}),
]


def main_menu():
    print("Welcome to the Garbage Game!")
    print("Choose your player:")
    print("1. Wizard")
    print("2. Soldier")
    print("3. Elf")
    
    player_type_choice = input("choose your player: ")
    player_type_dict = {"1": "wizard", "2": "soldier", "3": "elf"}
    
    player_type = player_type_dict.get(player_type_choice)
    
    if player_type:
        player = Player(name="Janidu", player_type=player_type)
        show_player_details(player)
    else:
        print("try again")
        main_menu()

def show_player_details(player):
    print("\nYour character details:")
    print(f"Player Type: {player.player_type.capitalize()}")
    print(f"Your Total Health: {player.health}")
    print(f"Weapon: {player.weapon.name} (Damage: {player.weapon.damage})")
    print(f"Armor: {player.armor.name} (Defense: {player.armor.defense})")
    print("You are now ready to begin your adventure!")

if __name__ == "__main__":
    main_menu()
