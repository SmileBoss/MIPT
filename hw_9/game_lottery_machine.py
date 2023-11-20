import random


def play_game():
    player_money = 0
    total_games = 100000

    for _ in range(total_games):
        player_money -= 1

        number = random.randint(0, 999)

        if number == 777:
            player_money += 200
        elif number == 999:
            player_money += 100
        elif number == 555:
            player_money += 50
        elif number == 333:
            player_money += 15
        elif number == 111:
            player_money += 10
        elif number % 100 == 77:
            player_money += 5
        elif number % 10 == 7:
            player_money += 3
        elif number % 100 == 0:
            player_money += 2
        elif number % 10 == 0:
            player_money += 1

    average_money = player_money / total_games

    return average_money
