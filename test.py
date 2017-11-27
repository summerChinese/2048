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
    # 这个是测试用的矩阵
    matrix = [
        [16, 2, 8, 4],
        [32, 16, 4, 2],
        [2, 32, 16, 8],
        [16, 2, 32, 16]
    ]
    main_data = TheData(matrix)
    instruction = BEGIN
    main_data.start_game()
    while not instruction[0] == END:
        instruction = input()
        if (instruction == ''):
            main_data.input_error()
        elif (instruction[0] == 'W'):
            main_data.move_up()
            main_data.compare_equal()
        elif (instruction[0] == "A"):
            main_data.move_left()
            main_data.compare_equal()
        elif (instruction[0] == "S"):
            main_data.move_down()
            main_data.compare_equal()
        elif (instruction[0] == "D"):
            main_data.move_right()
            main_data.compare_equal()
        elif (instruction[0] != 'E'):
            main_data.input_error()
        for i in range(len(main_data.matrix)):
            for j in range(len(main_data.matrix[i])):
                if main_data.matrix[i][j] == 2048:
                    main_data.game_over()

