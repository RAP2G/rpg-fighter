# Imports
from mimetypes import init
from random import randint, choice


# Global Variables


# Classes

class Weapon:
    def __init__(self, name, damage) -> None:
        self.name = name
        self.damage = damage

    def get_damage(self):
        return self.damage


GOBLIN_WEAPONS = [Weapon("Rusty Cleaver", 2),
                  Weapon("Rusty Spear", 3),
                  Weapon("Stone Axe", 1)]


class Character:
    def __init__(self, name, hp, attack, armor):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.armor = armor

    def __str__(self):
        return f"Name: {self.name}\n HP: {self.hp}\n Attack: {self.attack}\n Armor: {self.armor}"

    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.hp

    def get_name(self):
        return self.name

    def take_damage(self, damage):
        relative_damage = damage-self.armor
        if relative_damage > 0:
            self.hp -= relative_damage
            if self.hp < 0:
                self.hp = 0

    def get_attributes(self):
        return self.name, self.hp, self.attack, self.armor


class Goblin:
    def __init__(self, hp, armor, id):
        self.hp = hp
        self.armor = armor
        self.id = id
        self.weapon = choice(GOBLIN_WEAPONS)
        self.attack = self.weapon.get_damage()

    def __str__(self):
        return f"Goblin #{self.id}\n HP: {self.hp}\n Attack: {self.attack}\n Armor: {self.armor}"

    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.hp

    def get_name(self):
        return f"Goblin #{self.id}"

    def take_damage(self, damage):
        relative_damage = damage-self.armor
        if relative_damage > 0:

            self.hp -= relative_damage
            if self.hp < 0:
                self.hp = 0

# functions


def save_character(chars: list()):
    save_list = []
    for char in chars:
        name, health, attack, armor = char.get_attributes()
        save_string = f"{name}/{health}/{attack}/{armor}\n"
        save_list.append(save_string)
    with open("saved_characters.txt", "w", encoding="utf8") as f:
        for char in save_list:
            f.write(char)
        print("Characters has been saved!")


def load_characters():
    characters = []
    with open("saved_characters.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            attributes = line.split("/")
            char = Character(attributes[0],
                             int(attributes[1]),
                             int(attributes[2]),
                             int(attributes[3]))
            characters.append(char)
    return characters


def create_character():
    print("Welcome to the character creator!")
    name = input("What is your character called?")
    health = randint(10, 30)
    attack = randint(1, 5)
    armor = randint(0, 5)

    return_char = Character(name, health, attack, armor)

    print()
    print(return_char)
    print("Character has been created!")
    return return_char
