from src.map import Map
from src.player import Player
from src.bot import Bot

def game_show(player_1, player_2):
    map_1 = player_1.map
    map_2 = player_2.map

    print('-' * (map_1.shape[0] * 2 + 3), end='\t')
    print('-' * (map_2.shape[0] * 2 + 3))

    for row_1, row_2  in zip(map_1.show(), map_2.war_mist()):
        print('|', *row_1, '|', end='\t')
        print('|', *row_2, '|')

    print('-' * (map_1.shape[0] * 2 + 3), end='\t')
    print('-' * (map_2.shape[0] * 2 + 3))

if __name__ == '__main__':
    map1 = Map.generate((8, 8))
    player1 = Player(map1)

    map2 = Map.generate((8, 8))
    player2 = Bot(map2)

    turn = 0

    while True:
        if turn == 1:
            player1.do_attack(player2)
            game_show(player1, player2)
            turn = 2

            if player1.is_lose():
                print("Player 2 wins!")
                break

            elif player2.is_lose():
                print("Player 1 wins!")
                break

        elif turn == 2:
            player2.do_attack(player1)
            game_show(player1, player2)
            turn = 1

            if player1.is_lose():
                print("Player 2 wins!")
                break

            elif player1.is_lose():
                print("Player 1 wins!")
                break

        elif turn == 0:
            game_show(player1, player2)
            turn = 1