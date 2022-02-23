from resources import Character, Goblin, load_characters, save_character, create_character
from random import choice, randint, shuffle


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
    players = load_characters()
    print("Do you want to create new chracters?")
    create_new = input("y/n: ").lower()
    if create_new == "y":
        how_many = int(input("How many chracters would you like to create?"))
        for i in range(how_many):
            players.append(create_character())
    amount_of_goblins = int(input("How many goblins do you want to fight?"))
    for i in range(amount_of_goblins):
        enemies.append(Goblin(randint(10, 15), randint(0, 2), i+1))

    fight_round = 1
    while len(players) != 0 or len(enemies) != 0:
        print(enemies)
        print(f"ROUND {fight_round}, FIGHT!")
        fight(players, enemies)
        print()
        fight_round += 1
        if len(players) == 0 or len(enemies) == 0:
            break

    if len(players) == 0:
        print("The enemies have won!")

    else:
        print("The players have won!")
        print("Would you like to save the remaining chracters?")
        save_choice = input("y/n").lower()
        if save_choice == "y":
            save_character(players)
        else:
            print("No progress has been saved!")
