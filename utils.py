import json
import random


def round_my_config(item):
    item = float("{:.2f}".format(item))
    return item


def read_json_file(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


def write_json_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file)
        return data


def course_change():
    my_file = read_json_file("live_config.json")
    my_file_1 = read_json_file("config.json")
    common = my_file["course"]
    delta = my_file_1["delta"]
    my_new_course = random.triangular(common - delta, common + delta)
    my_new_course = round_my_config(my_new_course)
    my_file["course"] = my_new_course
    write_json_file(my_file, "live_config.json")
    return my_new_course


def live_course():
    current_course = read_json_file("live_config.json")
    return print(current_course["course"])


def my_account_balance():
    my_file = read_json_file("live_config.json")
    return print("UAN:", my_file["UAN"], "USD:", my_file["USD"])


def buy_usd(summa: int):
    my_file = read_json_file("live_config.json")
    dollars = summa * my_file["course"]
    my_balance = my_file["UAN"]
    if dollars > my_balance:
        return print(f" UNAVAILABLE, REQUIRED BALANCE {dollars}, AVAILABLE {my_balance}")
    else:
        my_new_balance = my_balance - dollars
        my_new_balance = round_my_config(my_new_balance)
        my_file["USD"] += summa
        my_file["UAN"] = my_new_balance
        write_json_file(my_file, "live_config.json")
    return my_new_balance


def sell_usd(summa):
    my_file = read_json_file("live_config.json")
    uan = summa * my_file["course"]
    my_balance = my_file["USD"]
    my_balance_gr = my_file["UAN"]
    if summa > my_balance:
        return print(f" UNAVAILABLE, REQUIRED BALANCE {summa}, AVAILABLE {my_balance}")
    else:
        my_new_balance = my_balance_gr + uan
        my_new_balance = round_my_config(my_new_balance)
        my_file["USD"] -= summa
        my_file["UAN"] = my_new_balance
        write_json_file(my_file, "live_config.json")
    return my_new_balance


def buy_all_usd():
    my_file = read_json_file("live_config.json")
    my_balance = my_file["UAN"]
    my_course = my_file["course"]
    dollars = my_balance / my_course
    dollars = round_my_config(dollars)
    my_file["USD"] += dollars
    my_file["UAN"] -= my_balance
    write_json_file(my_file, "live_config.json")
    return dollars


def sell_all_usd():
    my_file = read_json_file("live_config.json")
    my_balance = my_file["USD"]
    my_course = my_file["course"]
    my_new_uan = my_balance * my_course
    my_new_uan = round_my_config(my_new_uan)
    my_file["USD"] -= my_balance
    my_file["UAN"] += my_new_uan
    write_json_file(my_file, "live_config.json")
    return my_new_uan


def next_course() -> float:
    return course_change()


def restart_game():
    my_file = read_json_file("config.json")
    my_new_file = my_file.copy()
    my_new_file.popitem()
    write_json_file(my_new_file, "live_config.json")
    return my_new_file