from utils import live_course, my_account_balance, buy_usd, sell_usd, \
    buy_all_usd, sell_all_usd, next_course, restart_game
from argparse import ArgumentParser

if __name__ == "__main__":
    test_1 = ArgumentParser()
    test_1.add_argument("param_1", type=str, nargs='?')
    test_1.add_argument("summa", type=int, nargs='?')
    test_1 = vars(test_1.parse_args())
    if test_1['param_1'] == "rate":
        live_course()
    elif test_1['param_1'] == "avaliable":
        my_account_balance()
    elif test_1['param_1'] == "buy":
        buy_usd(test_1['summa'])
    elif test_1['param_1'] == "sell":
        sell_usd(test_1['summa'])
    elif test_1['param_1'] == "buyall":
        buy_all_usd()
    elif test_1['param_1'] == "sellall":
        sell_all_usd()
    elif test_1['param_1'] == "next":
        next_course()
    elif test_1['param_1'] == "restart":
        restart_game()
