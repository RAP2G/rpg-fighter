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


class Goblin:
    def __init__(self, hp, attack, armor, id):
        self.hp = hp
        self.attack = attack
        self.armor = armor
        self.id = id

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
