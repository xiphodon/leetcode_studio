#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 15:02
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00074_搜索二维矩阵.py
# @Software: PyCharm

"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :104 ms, 在所有 Python3 提交中击败了25.31%的用户
内存消耗 :15.7 MB, 在所有 Python3 提交中击败了5.41%的用户
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        二分法
        :param matrix:
        :param target:
        :return:
        """
        # 矩阵行数
        rows = len(matrix)
        if rows == 0:
            return False

        # 矩阵列数
        cols = len(matrix[0])
        if cols == 0:
            return False

        # 矩阵降维为一维数组
        # 小值指针
        v_min = 0
        # 大值指针
        v_max = rows * cols - 1

        while True:
            # 计算中间值指针
            v_middle = (v_min + v_max) // 2

            if v_min == v_middle:
                # 小值指针与中间值指针重合，说明小值指针已于大值指针相邻（相遇）
                if matrix[v_max // cols][v_max % cols] == target or matrix[v_min // cols][v_min % cols] == target:
                    # 若大值指针或小值指针指向数值等于目标值，返回True
                    return True
                else:
                    # 目标值不存在，返回False
                    return False

            # 中间值指针指向的数值
            middle_value = matrix[v_middle // cols][v_middle % cols]
            if middle_value == target:
                # 中间值指针指向的数值为目标值，返回True
                return True
            elif middle_value > target:
                # 中间值指针指向的数值大于目标值，将大值指针移动到中间值指针位置，将目标值圈在大值指针与小值指针之间
                v_max = v_middle
            else:
                # 中间值指针指向的数值小于目标值，将小值指针移动到中间值指针位置，将目标值圈在大值指针与小值指针之间
                v_min = v_middle


if __name__ == '__main__':
    mat = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target_num = 23

    s = Solution()
    res = s.searchMatrix(mat, target_num)
    print(res)
