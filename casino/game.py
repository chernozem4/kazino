from casino.game_logic import game, result
from decouple import config

def play_casino(my_money):
    while True:
        print(f"ваш счет: ${my_money}")
        bet = int(input("ваше число от 1 до 10?"))
        if bet > my_money:
            print("мало!")
            continue
        is_winning = game(bet)
        my_money = result(bet, is_winning)
        print(f"ваш счет: ${my_money}")
        if my_money > 1000:
            print("вы выиграли!")
            break
        elif my_money <= 0:
            print("вы проиграли...")
            break
        play_again = input("хотите еще? (да/не): ")
        if play_again != 'да':
            break


if __name__ == "__main__":
    my_money = int(config('MY_MONEY', default='1000'))
    play_casino(my_money)