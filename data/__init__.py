#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/11/12 17:22
# @Author  : summer
# @File    : __init__.py.py
from controler.directions import move_up as DIRECTIONS_MP
import random

# 位置个数
MAXNUM = 16

# 初始数的个数
RANDOMNUM = 2

# 用来生成随机数
MATRIX_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def init_matrix():
    # 主矩阵 用来存储最终生成的初始化矩阵
    main_matrix = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]
    # 随机矩阵，用来表示在哪个位置生成数据
    random_list = random.sample(MATRIX_LIST, RANDOMNUM)
    for i in random_list:
        row = int(i / 4)
        col = int(i % 4)
        index = random.choice([1, 2])
        main_matrix[row][col] = 2 ** index
    return main_matrix


class TheData():
    def __init__(self):
        self.matrix = init_matrix()

    def __print_matrix__(self):
        Str = ""
        for row in self.matrix:
            Str += "\t"
            for item in row:
                Str += str(item)
                Str += "\t"
            Str += "\n"
        print(Str)

    def start_game(self):
        print("Welcome to my 2048 game!Here is the instructions:\n"
              "\t'W' means move up\n"
              "\t'S' means move down\n"
              "\t'A' means move left\n"
              "\t'D' means move Right\n"
              "Please input 'enter' after you input your each instruction\n\n"
              "Let's get started now!")
        self.__print_matrix__()

    def move_up(self):
        self.matrix = DIRECTIONS_MP(self.matrix)
        print("You moved them up!\n"
              "Here is the result:")
        self.__print_matrix__()

    def game_over(self):
        print('GAME OVER!')

    def input_error(self):
        print('WRONG INPUT!Please input again:')
        self.__print_matrix__()

# if __name__ == '__main__':
#     data = TheData()
#     data.start_game()
