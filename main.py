from casino.game import play_casino

def main():
    my_money = int(input("Введите ваше начальное количество денег: "))
    play_casino(my_money)

if __name__ == "__main__":
    main()