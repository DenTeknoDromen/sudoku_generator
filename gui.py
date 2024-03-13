import tkinter as tk
from create_board import board

# initialvalues used for tkinter
window_width = 600
window_height = 400

draw_width = 300
draw_height = 300

root = tk.Tk()
root.title("Sudoku")
root.geometry(f'{window_width}x{window_height}')
canvas = tk.Canvas(root, width=window_width, height=window_height, bg="White")

# Draw base square
x = 150
y = 50
default_line_width = 1
canvas.create_rectangle(
    (x, y), (x + draw_width, y + draw_height), width=default_line_width, fill=None)

# Draw vertivcal and horisontal lines
xspace = x
yspace = y
lines = 9
for a in range(1, lines):
    xspace += draw_width/lines
    yspace += draw_height/lines
    line_width = default_line_width
    if a % 3 == 0:
        line_width += 2

    canvas.create_line(
        (xspace, y), (xspace, y + draw_height), width=line_width)
    canvas.create_line(
        (x, yspace), (x + draw_height, yspace), width=line_width)

# Write numbers in every square
xspace = x
yspace = y
for a in board:
    xspace = x + 7
    for b in board[a]:
        curr_num = b
        canvas.create_text((xspace, yspace), text=curr_num,
                           anchor="nw", font="tkDefaultFont 24")
        xspace += draw_width/9

    yspace += draw_height/9

canvas.pack(anchor=tk.CENTER, expand=True)
root.mainloop()
