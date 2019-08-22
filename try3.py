import numpy as np
import random
import tkinter as tk


def create_canvas():
    root = tk.Tk()
    canvas = tk.Canvas(root, width = 690, height = 690)
    canvas.pack()
    return canvas, root

def create_squares(canvas):
    square_list = []
    square_matrix = []
    for i in range(0, 690):
        for j in range(0, 690):
            square = canvas.create_rectangle(j, i, j+15, i+15, fill = 'grey')
            square_list.append(square)
            j += 15
        # square_matrix.append(square_list)
        i += 15
    # print(square_list)
    # print(square_matrix)
    return square_list

def convert_matrix():
    column = 46
    row = 46
    old = np.random.randint(2, size = (column, row))
    new = old
    print("old_matrix:")
    print(old)
    for i in range(0, column):
        for j in range(0, row):
            adja_sum = 0
            if i == 0:
                if j == 0:
                    adja_sum = new[i + 1][j] + new[i + 1][j + 1] + new[i][j + 1]
                    if adja_sum == 2 or adja_sum == 3:
                        new[i][j] = 1
                    else:
                        new[i][j] = 0
                else:

                    if j == row - 1:
                        adja_sum = new[i][j - 1] + new[i + 1][j - 1] + new[i + 1][j - 1]
                        if adja_sum == 2 or adja_sum == 3:
                            new[i][j] = 1
                        else:
                            new[i][j] = 0
                    else:

                        adja_sum = new[i][j - 1] + new[i + 1][j - 1] + new[i + 1][j] + new[i + 1][j + 1] + new[i][j + 1]
                        if adja_sum == 2 or adja_sum == 3:
                            new[i][j] = 1
                        else:
                            new[i][j] = 0
            else:


                if i == column - 1:
                    if j == 0:
                        adja_sum = new[i - 1][j] + new[i - 1][j + 1] + new[i][j + 1]
                        if adja_sum == 2 or adja_sum == 3:
                            new[i][j] = 1
                        else:
                            new[i][j] = 0
                    else:

                        if j == row - 1:
                            adja_sum = new[i - 1][j - 1] + new[i - 1][j] + new[i][j - 1]
                            if adja_sum == 2 or adja_sum == 3:
                                new[i][j] = 1
                            else:
                                new[i][j] = 0
                        else:

                            adja_sum = new[i - 1][j - 1] + new[i - 1][j] + new[i - 1][j + 1] + new[i][j - 1] + new[i][j + 1]
                            if adja_sum == 2 or adja_sum == 3:
                                new[i][j] = 1
                            else:
                                new[i][j] = 0
                else:


                    if j == 0:
                        adja_sum = new[i - 1][j] + new[i - 1][j + 1] + new[i][j + 1] + new[i + 1][j + 1] + new[i + 1][j]
                        if adja_sum == 2 or adja_sum == 3:
                            new[i][j] = 1
                        else:
                            new[i][j] = 0
                    else:


                        if j == row - 1:
                            adja_sum = new[i - 1][j] + new[i - 1][j - 1] + new[i][j - 1] + new[i + 1][j - 1] + new[i + 1][j]
                            if adja_sum == 2 or adja_sum == 3:
                                new[i][j] = 1
                            else:
                                new[i][j] = 0


            if i != 0 and i != column - 1 and j != 0 and j != row - 1:
                adja_sum = new[i - 1][j - 1] + new[i][j - 1] + new[i + 1][j - 1] + new[i - 1][j] + new[i + 1][j] + new[i - 1][j + 1] + new[i][j + 1] + new[i + 1][j + 1]
                if adja_sum == 2 or adja_sum == 3:
                    new[i][j] = 1
                else:
                    new[i][j] = 0
    print("new_matrix:")
    print(new)
    return new

def change_color(square_list, new_matrix, canvas):
    for i in range(0, 46):
        for j in range(0, 46):
            if new_matrix[i][j] == 1:
                canvas.itemconfig(square_list[i][j], fill = "yellow")
            if new_matrix[i][j] == 0:
                canvas.itemconfig(square_list[i][j], fill = "grey")

def main():
    canvas, root = create_canvas()
    # square_list = create_squares(canvas)
    # new_matrix = convert_matrix()
    # change_color(square_list, new_matrix, canvas)
    # root.mainloop()


main()