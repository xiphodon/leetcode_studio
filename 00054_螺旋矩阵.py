#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 10:18
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00054_螺旋矩阵.py
# @Software: PyCharm

"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :40 ms, 在所有 Python3 提交中击败了97.56%的用户
内存消耗 :13 MB, 在所有 Python3 提交中击败了97.34%的用户
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        i = j = 0
        direction = 'r'
        res_list = list()
        while True:
            # 记录当前位置数值，记录完毕置为None
            res_list.append(matrix[i][j])
            matrix[i][j] = None
            # 判断指针是否可以移动到新位置
            if direction == 'r':
                if self.is_valid(matrix, i, j + 1):
                    # 可以向右
                    direction = 'r'
                    j += 1
                    continue
                if self.is_valid(matrix, i + 1, j):
                    # 可以向下
                    direction = 'd'
                    i += 1
                    continue
            if direction == 'd':
                if self.is_valid(matrix, i + 1, j):
                    # 可以向下
                    direction = 'd'
                    i += 1
                    continue
                if self.is_valid(matrix, i, j - 1):
                    # 可以向左
                    direction = 'l'
                    j -= 1
                    continue
            if direction == 'l':
                if self.is_valid(matrix, i, j - 1):
                    # 可以向左
                    direction = 'l'
                    j -= 1
                    continue
                if self.is_valid(matrix, i - 1, j):
                    # 可以向上
                    direction = 'u'
                    i -= 1
                    continue
            if direction == 'u':
                if self.is_valid(matrix, i - 1, j):
                    # 可以向上
                    direction = 'u'
                    i -= 1
                    continue
                if self.is_valid(matrix, i, j + 1):
                    # 可以向右
                    direction = 'r'
                    j += 1
                    continue
            # 四个方向均不可移动时，退出循环
            break
        return res_list

    def is_valid(self, matrix, x, y):
        """
        该位置是否为有效位置
        :param matrix:
        :param x:
        :param y:
        :return:
        """
        h = len(matrix)
        w = len(matrix[0])

        if y == w or x == h:
            return False
        if matrix[x][y] is not None:
            return True
        return False


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    s = Solution()
    res = s.spiralOrder(matrix)
    print(res)
