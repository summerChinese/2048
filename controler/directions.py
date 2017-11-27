#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/11/12 18:40
# @Author  : summer
# @File    : directions.py
import random

RANDOM = 1
# 行数和列数记得用

MAXCOLS = 4
MAXROWS = 4


def compare_up(matrix, one, line):
    if matrix[one + 1][line] == 0:
        pass  # 不做改变
    elif matrix[one][line] == 0:
        matrix[one][line] = matrix[one + 1][line]
        matrix[one + 1][line] = 0
    elif matrix[one][line] == matrix[one + 1][line]:
        matrix[one][line] = matrix[one][line] * 2
        matrix[one + 1][line] = 0
    else:
        pass  # 不做改变


def compare_left(matrix, one, col):
    if matrix[col][one + 1] == 0:
        pass
    elif matrix[col][one] == 0:
        matrix[col][one] = matrix[col][one + 1]
        matrix[col][one + 1] = 0
    elif matrix[col][one + 1] == matrix[col][one]:
        matrix[col][one] = 2 * matrix[col][one + 1]
        matrix[col][one + 1] = 0
    else:
        pass


def compare_down(matrix, one, line):
    if matrix[one - 1][line] == 0:
        pass
    elif matrix[one][line] == 0:
        matrix[one][line] = matrix[one - 1][line]
        matrix[one - 1][line] = 0
    elif matrix[one][line] == matrix[one - 1][line]:
        matrix[one][line] = 2 * matrix[one - 1][line]
        matrix[one - 1][line] = 0
    else:
        pass


def compare_right(matrix, one, col):
    if matrix[one][col - 1] == 0:
        pass
    elif matrix[one][col] == 0:
        matrix[one][col] = matrix[one][col - 1]
        matrix[one][col - 1] = 0
    elif matrix[one][col - 1] == matrix[one][col]:
        matrix[one][col] = 2 * matrix[one][col - 1]
        matrix[one][col - 1] = 0
    else:
        pass


def generate_random(matrix):
    k = 0;
    zero_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zero_matrix.append([i, j])
    if len(zero_matrix) == 0:
        k = COMPARE_EQUAL(matrix)
        if k <15:
            print("Please change a direction")
    else:
        random_list = random.sample(zero_matrix, RANDOM)
        index = random.choice([1, 2])
        a = random_list[0][0]
        b = random_list[0][1]
        # 第row行第col列装入数2的index次方，即2的一次或二次
        matrix[a][b] = 2 ** index


def COMPARE_EQUAL(matrix):
    k = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 and j == 0:
                if matrix[i][j] != 0 and matrix[i + 1][j] != 0 and matrix[i][j + 1] != 0 and matrix[i][j] != \
                        matrix[i + 1][j] and matrix[i][j] != matrix[i][j + 1]:
                    k += 1
            if i == 0 and j == 3:
                if matrix[i][j] != 0 and matrix[i + 1][j] != 0  and matrix[i][j] != \
                        matrix[i + 1][j]:
                    k += 1
            if i == 3 and j == 0:
                if matrix[i][j] != 0 and matrix[i][j + 1] != 0 and matrix[i][j] != matrix[i][
                            j + 1]:
                    k += 1
            elif i == 0 and 0<j<3:
                if matrix[i][j] != 0 and matrix[i + 1][j] != 0 and matrix[i][j + 1] != 0 and matrix[i][j] != \
                        matrix[i + 1][j] and matrix[i][j] != matrix[i][j + 1]:
                    k += 1
            elif j == 0 and 0<i<3:
                if matrix[i][j] != 0 and matrix[i + 1][j] != 0 and matrix[i][j + 1] != 0 and matrix[i][j] != \
                        matrix[i + 1][j] and matrix[i][j] != matrix[i][j + 1]:
                    k += 1
            elif i == 3 and 0<j<3:
                if matrix[i][j] != 0  and matrix[i][j + 1] != 0 and matrix[i][j] != \
                        matrix[i][j+1] :
                    k += 1
            elif j == 3 and 0<i<3:
                if matrix[i][j] != 0 and matrix[i + 1][j] != 0  and matrix[i][j] != \
                        matrix[i + 1][j] :
                    k += 1
            elif  0<i<3 and  0<j<3:
                if matrix[i][j] != 0 and matrix[i + 1][j] != 0 and matrix[i][j + 1] != 0 and matrix[i][j] != \
                        matrix[i + 1][j] and matrix[i][j] != matrix[i][j + 1]:
                    k += 1

    return k


#


# def compare_down(matrix, one, line):
#     if matrix[one + 1][col] == 0:
#         pass
#     elif matrix[one][col] == 0:
#         matrix[one][col] = matrix[one + 1][col]
#         matrix[one + 1][col] = 0
#     elif matrix[one + 1][col] == matrix[one][col]:
#         matrix[one + 1][col] = 0
#         matrix[one][col] = 2 * matrix[one + 1][col]
#     else:
#         pass
#
#
# def compare_left(matrix, one, col):
#     if matrix[col][one+1] == 0:
#         pass
#     elif matrix[col][one] == 0:
#         matrix[col][one]= matrix[col][one+1]
#         matrix[col][one + 1] = 0
#     elif matrix[col][one]== matrix[col][one+1]:
#         matrix[col][one] = 2 * matrix[col][one+1]
#         matrix[col][one+1]=0
#     else:
#         pass


# 函数参数：上移前的矩阵matrix
# 函数返回值:上移后的矩阵result_matrix
# 函数功能：上移
def MOVE_UP(matrix):
    for j in range(4):
        compare_up(matrix, 0, j)
        compare_up(matrix, 1, j)
        compare_up(matrix, 0, j)
        compare_up(matrix, 2, j)
        compare_up(matrix, 1, j)
        compare_up(matrix, 0, j)

    generate_random(matrix)
    return matrix


def MOVE_LEFT(matrix):
    for j in range(4):
        compare_left(matrix, 0, j)
        compare_left(matrix, 1, j)
        compare_left(matrix, 0, j)
        compare_left(matrix, 2, j)
        compare_left(matrix, 1, j)
        compare_left(matrix, 0, j)

    generate_random(matrix)
    return matrix


def MOVE_DOWN(matrix):
    for j in range(4):
        compare_down(matrix, 3, j)
        compare_down(matrix, 2, j)
        compare_down(matrix, 3, j)
        compare_down(matrix, 1, j)
        compare_down(matrix, 2, j)
        compare_down(matrix, 3, j)
    generate_random(matrix)
    return matrix


def MOVE_RIGHT(matrix):
    for i in range(4):
        compare_right(matrix, i, 3)
        compare_right(matrix, i, 2)
        compare_right(matrix, i, 3)
        compare_right(matrix, i, 1)
        compare_right(matrix, i, 2)
        compare_right(matrix, i, 3)
    generate_random(matrix)
    return matrix
