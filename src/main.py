from operator import imod
from turtle import pensize
from resources import Character, Goblin
from random import randint
if __name__ == "__main__":
    vonala = Character("Vonala", 20, 5, 2)
    goblin_one = Goblin(10, 3, 1)
    print(vonala)
    print()
    print(goblin_one)
    fight_round = 1
    print("========FIGHT========")
    while vonala.get_health() != 0 and goblin_one.get_health() != 0:
        print(f"Round: {fight_round}")
        goblin_one.take_damage(vonala.damage())
        if goblin_one.get_health() == 0:
            print("Goblin has died")
            break
        else:
            print(f"Goblin has {goblin_one.get_health()}hp left.")
            vonala.take_damage(goblin_one.damage())
            print(f"{vonala.name} has {vonala.get_health()}hp left")
            if vonala.get_health() == 0:
                print(f"{vonala.name} has died.")
        fight_round += 1

    if vonala.get_health() == 0:
        print("The goblin has won!")
    else:
        print(f"{vonala.name} has won!")
