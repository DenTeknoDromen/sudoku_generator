asc = "123"
desc = "321"

all_lists = []
combinations = []


def create_roman(start, list_1, list_2):
    curr_list = ""
    a = list_1.index(str(start))
    b = list_2.index(list_1[a]) + 1

    for x in range(1, 10):
        if a >= len(list_1):
            a = 0
        if b >= len(list_2):
            b = 0
        curr_list += list_1[a]
        if x % 3 == 0:
            a = list_1.index(list_2[b])
            b += 1
        else:
            a += 1

    return curr_list


def combine_roman(list_1, list_2):
    curr_list = []
    for i in range(len(list_1)):
        curr_list.append(list_1[i] + list_2[i])
    return curr_list


def get_combinations():
    return combinations


for x in range(1, 4):
    all_lists.append(create_roman(x, asc, asc))
    all_lists.append(create_roman(x, asc, desc))
    all_lists.append(create_roman(x, desc, desc))
    all_lists.append(create_roman(x, desc, asc))

for x in all_lists:
    for y in all_lists:
        combinations.append(combine_roman(x, y))
