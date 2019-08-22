import numpy as np
import random


column = 10
row = 10
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