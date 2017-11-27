#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/11/12 17:22
# @Author  : summer
# @File    : __init__.py.py
# 这个moveup就是ctr/directions.py 里面的moveup函数
from controler.directions import MOVE_UP,MOVE_DOWN,MOVE_LEFT,MOVE_RIGHT,COMPARE_EQUAL
import random

# 位置个数
MAXNUM = 16

# 初始数的个数
RANDOMNUM = 2

# 用来生成随机数
MATRIX_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# 用来生成初始化矩阵
def init_matrix():
    # 主矩阵 用来存储最终生成的初始化矩阵
    main_matrix = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]
    # 随机矩阵，用来表示在哪个位置生成数据
    random_list = random.sample(MATRIX_LIST, RANDOMNUM)
    for i in random_list:
        # 随机选取行和列
        row = int(i / 4)
        col = int(i % 4)
        index = random.choice([1, 2])
        # 第row行第col列装入数2的index次方，即2的一次或二次
        main_matrix[row][col] = 2 ** index
        # print(main_matrix[0])
    return main_matrix


class TheData():
    def __init__(self,matrix =None):
        if matrix == None:
            self.matrix = init_matrix()
        else:
            self.matrix = matrix

    def __print_matrix__(self):
        # 这就是一个遍历  把这个看懂
        Str = ""
        # for row in self.matrix:
        #     Str += "\t"
        #     for item in row:
        #         Str += str(item)#类型转换
        #         Str += "\t"
        #     Str += "\n"
        # print(Str)
        #     第二种写法
        #     len是求长度，这里把range()里面都写成4都可以
        for i in range(len(self.matrix)):
            Str += "\t"
            for j in range(len(self.matrix[i])):
                Str += str(self.matrix[i][j])
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
        # 这里调用了MOVE_UP函数，把当前的matrix做参数传了进去
        # 然后返回了上移之后的矩阵，重新复制给matrix
        # 类似于这个例子
        # 函数功能，翻倍
        # def double(num):
        #     result = num*2
        #     return result
        # if __name__......:
        #     a = 3
        #     a = double(a)
        #     print(a)
        #
        # console:
        #
        self.matrix = MOVE_UP(self.matrix)
        print("You moved them up!\n"
              "Here is the result:")
        self.__print_matrix__()

    def move_left(self):
        self.matrix = MOVE_LEFT(self.matrix)
        print("You moved them left!\n"
              "Here is the result:")
        self.__print_matrix__()

    def move_down(self):
        self.matrix = MOVE_DOWN(self.matrix)
        print("You moved them down!\n"
              "Here is the result:")
        self.__print_matrix__()

    def move_right(self):
        self.matrix = MOVE_RIGHT(self.matrix)
        print("You moved them right!\n"
              "Here is the result:")
        self.__print_matrix__()

    def game_over(self):
        print('GAME OVER!')

    def input_error(self):
        print('WRONG INPUT!Please input again:')
        self.__print_matrix__()

    # 这里没有参数，self是自带的，引用的时候不用带上
    # 要是需要带别的参数的话要这么定义
    # def compare_equal(self,another_argument):
    #   pass
    def compare_equal(self):
        self.k=COMPARE_EQUAL(self.matrix)
        if self.k==15:
           print("game over")



# if __name__ == '__main__':
#     data = TheData()
#     data.start_game()
