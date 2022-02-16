
from resources import Character, Goblin
from random import choice, shuffle


def fight(players: list, enemies: list):
    participants = players+enemies
    shuffle(participants)
    for char in participants:
        target = ""
        # Is the character a player or an enemy
        if char in players:
            target = choice(enemies)
        else:
            target = choice(players)
        target.take_damage(char.get_attack())
        if target.get_health() == 0:
            print(f"{target.get_name()} has died.")
            if type(target) == Goblin:
                enemies.remove(target)
            else:
                players.remove(target)
            participants.remove(target)
        else:
            print(f"{target.get_name()} has {target.get_health()} hp left.")
        if len(players) == 0 or len(enemies) == 0:
            break


if __name__ == "__main__":
    players = []
    enemies = []
    vonala = Character("Vonala", 20, 5, 2)
    nick = Character("Nick", 15, 2, 1)
    players.append(vonala)
    players.append(nick)
    enemies.append(Goblin(10, 3, 1, 1))
    enemies.append(Goblin(15, 2, 1, 2))
    enemies.append(Goblin(12, 3, 1, 3))
    fight_round = 1
    while len(players) != 0 or len(enemies) != 0:
        print(enemies)
        print(f"ROUND {fight_round}, FIGHT!")
        fight(players, enemies)
        print()
        fight_round += 1

    if len(players) == 0:
        print("The enemies have won!")
    else:
        print("The players have won!")
