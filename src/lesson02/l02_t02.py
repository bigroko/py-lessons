# -*- coding: UTF-8 -*-

DIM = 6

matrix = [[col + 1 for col in range(DIM - row)] for row in range(DIM)]
for item in matrix:
    print(item)
