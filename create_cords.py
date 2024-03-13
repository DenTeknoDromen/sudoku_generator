from random import randrange
from create_combinations import get_combinations

dict_lst = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
combinations = []


def set_combinations():
    for x in get_combinations():
        combinations.append(x)


def fill_dict():
    check = 0
    index = randrange(len(combinations))
    curr_list = combinations[index]
    combinations.pop(index)

    for i in range(len(curr_list)):
        if curr_list[i] not in dict_lst[i + 1]:
            check += 1

    if check == 9:
        index = 0
        for a in dict_lst.values():
            a.append(curr_list[index])
            index += 1


def clear_dict():
    for x in dict_lst.values():
        x.clear()


def set_dict():
    clear_dict()
    set_combinations()
    loops = 0
    while len(dict_lst[9]) != 9 and loops < 100000:
        fill_dict()
        loops += 1


while True:
    try:
        set_dict()
        break
    except ValueError:
        continue

# for x in dict_lst.values():
#     print(x)
