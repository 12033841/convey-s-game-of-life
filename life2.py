import numpy as np
import random, sys
import tkinter as tk
import time


class World:

    def __init__(self, matrix_size):
        self.the_matrix = None
        self.new_matrix = None
        self.num_rows = matrix_size[0]
        self.num_columns = matrix_size[1]

        self.init_matrix()

    def init_matrix(self):
        self.the_matrix = np.zeros([self.num_rows, self.num_columns], int)
        self.new_matrix = np.zeros([self.num_rows, self.num_columns], int)

        for i in range(self.num_rows):
            for j in range(self.num_columns):
                if i == 0 or i == self.num_rows-1 or j == 0 or j == self.num_columns-1:
                    self.the_matrix[i,j] = 0

    def onclick_init(self, i, j, original):
        if original == 0:
            self.the_matrix[i, j] = 1
        if original == 1:
            self.the_matrix[i, j] = 0

    def next(self):
        for i in range(1, self.num_rows-1):
            for j in range(1, self.num_columns-1):

                num_on_neighbors = 0

                for m in range(-1, 2):
                    for n in range(-1, 2):
                        num_on_neighbors += self.the_matrix[i + m, j + n]

                if self.the_matrix[i, j] == 1:
                    num_on_neighbors -= 1

                    if 2 <= num_on_neighbors <= 3:
                        self.new_matrix[i, j] = 1
                        changed = True
                    else:
                        self.new_matrix[i, j] = 0
                else:
                    if num_on_neighbors == 3:
                        self.new_matrix[i, j] = 1
                        changed = True
                    else:
                        self.new_matrix[i, j] = 0
        tempor_matrix = self.the_matrix
        self.the_matrix = self.new_matrix
        self.new_matrix = tempor_matrix

class Window:

    def __init__(self, the_world):
        self.root = tk.Tk()

        self.display_frame = tk.Frame(self.root)
        self.display_frame.pack()
        self.canvas = tk.Canvas(self.display_frame, width=690, height=690)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.onclick)
        self.canvas.pack()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.start_button = tk.Button(self.button_frame, text="Start", fg="black", command=self.start)
        self.next_button = tk.Button(self.button_frame, text="Next", fg="black", command=self.next)
        self.reset_button = tk.Button(self.button_frame, text="Reset", fg="black", command=self.reset)
        self.quit_button = tk.Button(self.button_frame, text="Quit", fg="black", command=self.quit)
        self.start_button.pack(side=tk.LEFT)
        self.next_button.pack(side=tk.LEFT)
        self.reset_button.pack(side=tk.LEFT)
        self.quit_button.pack(side=tk.LEFT)

        self.square_matrix = None

        self.the_world = the_world
        self.running = False

        self.init_window()

    def init_window(self):
        self.draw_world()

    def next(self):
        self.the_world.next()
        self.draw_world()

    def start(self):
        if self.running:
            self.running = False
            self.start_button.config(text="Start")
        else:
            self.running = True
            self.start_button.config(text="Pause")

        while self.running:
            self.next()
            self.root.update()
            time.sleep(0.1)


    def reset(self):
        self.the_world.init_matrix()
        self.draw_world()

    def onclick(self, event):
        x, y = event.x, event.y
        i = int(x / 15)
        j = int(y / 15)

        if self.the_world.the_matrix[i,j] == 0:
            original = 0
            color = "yellow"
            self.canvas.create_rectangle(i * 15, j * 15, (i + 1) * 15, (j + 1) * 15, fill=color)
            self.the_world.onclick_init(i, j, original)
        else:
            original = 1
            color = "grey"
            self.canvas.create_rectangle(i * 15, j * 15, (i + 1) * 15, (j + 1) * 15, fill=color)
            self.the_world.onclick_init(i, j, original)

    def draw_world(self):
        self.square_matrix = []
        for i in range(self.the_world.num_rows):
            square_list = []
            for j in range(self.the_world.num_columns):

                if i == 0 or i == self.the_world.num_rows - 1 or j == 0 or j == self.the_world.num_columns - 1:
                    color = 'black'
                else:
                    if self.the_world.new_matrix[i,j] == 0:
                        color = "grey"
                    else:
                        color = "yellow"
                square = self.canvas.create_rectangle(i * 15, j * 15, (i + 1) * 15, (j + 1) * 15, fill=color)
                square_list.append(square)
                j += 1
            self.square_matrix.append(square_list)
            i += 1

    def quit(self):
        sys.exit()


def main():
    matrix_size = (46, 46)
    the_world = World(matrix_size)
    the_window = Window(the_world)
    the_window.root.mainloop()
main()