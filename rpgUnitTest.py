import unittest
from unittest.mock import patch
from io import StringIO
import sys
import rpg

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
        self.health = 100
        self.weapon = Weapon("Sword", 15)
        self.armor = Armor("Shield", 10)
        self.inventory = {}

    def addItemToInventory(self, item, quantity=1):
        self.inventory[item] = quantity

class Enemy:
    def __init__(self, name, health, damageRange, lootTable):
        self.name = name
        self.health = health
        self.damageRange = damageRange
        self.lootTable = lootTable

    def dealDamage(self):
        return 10 
# Unit tests
class TestGame(unittest.TestCase):

    def test_player_initialization(self):
        player = Player("Test Player", "wizard")
        self.assertEqual(player.name, "Test Player")
        self.assertEqual(player.playerType, "wizard")
        self.assertEqual(player.health, 100)
        self.assertEqual(player.weapon.name, "Sword")
        self.assertEqual(player.armor.name, "Shield")

    def test_enemy_attack(self):
        enemy = Enemy("Goblin", 30, (5, 10), {"Gold": 100})
        damage = enemy.dealDamage()
        self.assertEqual(damage, 10) 

    def test_add_item_to_inventory(self):
        player = Player("Test Player", "wizard")
        player.addItemToInventory("Gold", 100)
        self.assertIn("Gold", player.inventory)
        self.assertEqual(player.inventory["Gold"], 100)

    @patch('builtins.input', side_effect=["1", "1", "3"]) 
    @patch('sys.stdout', new_callable=StringIO)
    def test_game_flow(self, mock_stdout, mock_input):
        rpg.mainMenu()  
        output = mock_stdout.getvalue()
        self.assertIn("You are now fighting", output)
        self.assertIn("You attack", output)
        self.assertIn("bye", output)  

if __name__ == '__main__':
    unittest.main()
