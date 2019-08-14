#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 9:55
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00073_矩阵置零.py
# @Software: PyCharm

"""
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-matrix-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :188 ms, 在所有 Python3 提交中击败了32.23%的用户
内存消耗 :14.5 MB, 在所有 Python3 提交中击败了5.11%的用户
"""
import pprint
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        时间复杂度 O(mn)
        空间复杂度 O(1)
        """
        if len(matrix) == 0:
            return

        first_row_flag = False
        first_col_flag = False

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0 and matrix[r][c] == 0:
                    # 第一行有元素为0，记录当前行需要全部更新为0
                    first_row_flag = True

                if c == 0 and matrix[r][c] == 0:
                    # 第一列有元素为0，记录当前列需要全部更新为0
                    first_col_flag = True

                if matrix[r][c] == 0:
                    # 若当前位置为 0，则把当前行首、列首的元素置为 0
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # 从第二行第二列开始检查，
        # 将所有 第一行标记为 0 的列 所有元素置为 0，
        # 将所有 第一列标记为 0 的行 所有元素置为 0
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # 再检查第一行，第一列，是否置为 0
        if first_row_flag:
            # 第一行全置为0
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        if first_col_flag:
            # 第一列全置为0
            for r in range(len(matrix)):
                matrix[r][0] = 0


if __name__ == '__main__':
    mat = [
        [1, 1, 2, 1, 1, 2],
        [0, 4, 5, 2, 2, 3],
        [1, 3, 1, 5, 3, 4],
        [1, 3, 1, 5, 3, 4],
        [1, 3, 1, 5, 3, 4]
    ]

    s = Solution()
    pprint.pprint(mat)
    s.setZeroes(mat)
    pprint.pprint(mat)
