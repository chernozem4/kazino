import random
from decouple import config

def game(bet):
    slot = random.randint(1, 10)
    if bet == slot:
        return True
    else:
        return False

def result(bet, is_winning):
    my_money = int(config('MY_MONEY', default='1000'))
    if is_winning:
        my_money += bet * 2
    else:
        my_money -= bet
    return my_money