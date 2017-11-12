#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/11/12 18:51
# @Author  : summer
# @File    : main.py
from data import TheData

BEGIN = 'B'
END = 'E'

if __name__ == '__main__':
    main_data = TheData()
    instruction = BEGIN
    main_data.start_game()
    while not instruction[0] == END:
        instruction = input()
        if (instruction == ''):
            main_data.input_error()
        elif (instruction[0] == 'W'):
            main_data.move_up()
        elif (instruction[0] != 'E'):
            main_data.input_error()
    main_data.game_over()
