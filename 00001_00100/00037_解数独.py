#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 11:26
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00037_解数独.py
# @Software: PyCharm

"""
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

1、数字 1-9 在每一行只能出现一次。
2、数字 1-9 在每一列只能出现一次。
3、数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

Note:

1、给定的数独序列只包含数字 1-9 和字符 '.' 。
2、你可以假设给定的数独只有唯一解。
3、给定数独永远是 9x9 形式的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sudoku-solver
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 困难

执行用时 :136 ms, 在所有Python3提交中击败了83.62%的用户
内存消耗 :12.9 MB, 在所有Python3提交中击败了96.96%的用户
"""
from typing import List


class Solution:
    def __init__(self):
        # 每行数字集合列表
        self.row_set_list = [set() for _ in range(9)]
        # 每列数字集合列表
        self.col_set_list = [set() for _ in range(9)]
        # 每小九宫数字集合列表
        self.grid_set_list = [set() for _ in range(9)]
        # 空格子列表（存储空位置索引的元组）
        self.empty_list = list()
        # 可选数字全集
        self.all_number_set = set(str(i) for i in range(1, 10))

    def get_grid_index(self, i, j) -> int:
        """
        获取小九宫索引
        :param i: 行
        :param j: 列
        :return:
        """
        return (i // 3) * 3 + (j // 3)

    def solveSudoku(self, board: List[List[str]]) -> None:
        # 初始化每行、每列、每小九宫已填数字
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == '.':
                    self.empty_list.append((i, j))
                else:
                    self.row_set_list[i].add(v)
                    self.col_set_list[j].add(v)
                    self.grid_set_list[self.get_grid_index(i, j)].add(v)
        # 填格子
        self.fill_board(board)

    def fill_board(self, board) -> bool:
        """
        填格子
        :return: 此步是否可填
        """
        if len(self.empty_list) == 0:
            return True

        # 查看准备要填的位置
        i, j = self.empty_list[0]

        # 获取当前位置行、列、小九宫已填入的数字
        row_nums_set = self.row_set_list[i]
        col_nums_set = self.col_set_list[j]
        grid_nums_set = self.grid_set_list[self.get_grid_index(i, j)]

        # 该位置可填的数字
        can_fill_nums_set = self.all_number_set - row_nums_set - col_nums_set - grid_nums_set

        if len(can_fill_nums_set) == 0:
            # 无数可填，此步填数失败
            return False

        # 准备填数
        for n in can_fill_nums_set:
            # 填数
            self.row_set_list[i].add(n)
            self.col_set_list[j].add(n)
            self.grid_set_list[self.get_grid_index(i, j)].add(n)
            self.empty_list.pop(0)
            board[i][j] = n
            # 准备填下一步
            if self.fill_board(board):
                # 下一步可填
                # 这一步也可填
                return True
            else:
                # 下一步不可填
                # 回退
                self.row_set_list[i].remove(n)
                self.col_set_list[j].remove(n)
                self.grid_set_list[self.get_grid_index(i, j)].remove(n)
                self.empty_list.insert(0, (i, j))
                board[i][j] = '.'

        # 已全试填完毕，仍没成功，返回此步失败
        return False


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    s = Solution()
    print(board)
    s.solveSudoku(board)
    print(board)
