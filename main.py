#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/11/12 18:51
# @Author  : summer
# @File    : main.py
from data import TheData

BEGIN = 'B'
END = 'E'

if __name__ == '__main__':
    # 实例化
    # 调用data/__init__.py里面的class TheData()的__init__函数 A
    main_data = TheData()
    instruction = BEGIN
    main_data.start_game()
    while not instruction[0] == END:
        instruction = input()
        if (instruction == ''):
            main_data.input_error()
        elif (instruction[0] == 'W'):
            main_data.move_up()
        elif (instruction[0] == "A"):
            main_data.move_left()
        elif (instruction[0] == "S"):
            main_data.move_down()
        elif (instruction[0] == "D"):
            main_data.move_right()
        elif (instruction[0] != 'E'):
            main_data.input_error()
        for i in range(len(main_data.matrix)):
            for j in range(len(main_data.matrix[i])):
                if main_data.matrix[i][j]==2048:
                    main_data.game_over()
