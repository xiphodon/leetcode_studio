#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 9:35
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00048_旋转图像.py
# @Software: PyCharm

"""
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-image
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :48 ms, 在所有 Python3 提交中击败了93.17%的用户
内存消耗 :13 MB, 在所有 Python3 提交中击败了93.40%的用户
"""

# 顺时针旋转
# 维度为偶数，只需迭代1/4矩阵左上正方形角块即可
# 维度为奇数，只需迭代1/4矩阵左上矩形方形角块即可，一边向下取整，一边向上取整，仅中心元素不在四个角块中（中心元素无需移动位置）
# [图示角块编号(0,1,2,3,4)]
# 例：维度为偶数
# 0 0 1 1
# 0 0 1 1
# 2 2 3 3
# 2 2 3 3
#
# 例：维度为奇数
# 0 0 0 1 1
# 0 0 0 1 1
# 3 3 * 1 1
# 3 3 2 2 2
# 3 3 2 2 2
#

# 获取左上角角块的高度（high）和宽度(width)
# 仅遍历左上角块
# 矩阵四角块对应元素同时旋转

# 左上角块某元素 (i, j)
# 右上角块旋转对应元素 (j, n-1-i)
# 右下角块旋转对应元素 (n-1-i, n-1-j)
# 左下角块旋转对应元素 (n-1-j, i)

# 顺时针方向交换元素值
# 右上元素，右下元素，左下元素，左上元素 = 左上元素，右上元素，右下元素，左下元素

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 矩阵维度
        n = len(matrix)

        if n & 1 == 0:
            # 维度为偶数，获取左上角角块的高度（high）和宽度(width)
            high = width = n // 2
        else:
            # 维度为奇数，获取左上角角块的高度（high）和宽度(width)
            high, width = n // 2, (n + 1) // 2

        # 仅遍历左上角块，矩阵四角块对应元素同时旋转交换元素值
        for i in range(high):
            for j in range(width):
                matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i], matrix[i][j] = matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i]


if __name__ == '__main__':
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]

    # matrix = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]

    print(matrix)
    s = Solution()
    s.rotate(matrix)
    print(matrix)
