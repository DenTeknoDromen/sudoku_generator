from random import randrange
from create_cords import dict_lst

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
board_cords = {1: "00", 2: "03", 3: "06", 4: "30",
               5: "33", 6: "36", 7: "60", 8: "63", 9: "66"}

for empty_list in board.values():
    for x in range(9):
        empty_list.append(0)


def get_cords(cords, square, index):
    x = (int(cords[index][0])) + (int(square[0]))
    y = (int(cords[index][1])) + (int(square[1]))
    return [x, y]


def set_nums(num, index):
    for cords in dict_lst:
        xy = get_cords(dict_lst[cords], board_cords[cords], index)
        x = xy[0]
        y = xy[1]
        board[x][y - 1] = num


for index in range(9):
    num_index = randrange(len(nums))
    num = nums[num_index]
    set_nums(num, index)
    nums.pop(num_index)
