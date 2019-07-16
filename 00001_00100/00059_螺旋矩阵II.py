#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 10:13
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00059_螺旋矩阵II.py
# @Software: PyCharm

"""
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :52 ms, 在所有 Python3 提交中击败了79.92%的用户
内存消耗 :13.1 MB, 在所有 Python3 提交中击败了71.21%的用户
"""
import pprint
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 空矩阵
        array_list = [[-1 for _ in range(n)] for _ in range(n)]
        # 层数
        lay_num = (n + 1) // 2
        # 按层遍历，从最外层到最内层
        for i in range(lay_num):
            # 当前回字层边长
            this_w = n - 2 * i
            # 内层回字边长
            inner_w = n - 2 * (i + 1)
            if inner_w > 0:
                # 有内层
                lay_size = this_w ** 2 - inner_w ** 2
            else:
                # 无内层，已是最内层
                lay_size = this_w ** 2
            # 当前层遍历所有数字，从左上角开始
            for j in range(lay_size):
                if 0 <= j <= this_w - 1:
                    # 为回字上边
                    r = i
                    c = i + j
                elif this_w - 1 < j <= 2 * (this_w - 1):
                    # 为回字右边
                    r = i + j - (this_w - 1)
                    c = i + this_w - 1
                elif 2 * (this_w - 1) < j <= 3 * (this_w - 1):
                    # 为回字下边
                    r = i + this_w - 1
                    c = i + this_w - 1 - (j - 2 * (this_w - 1))
                elif 3 * (this_w - 1) < j < 4 * (this_w - 1):
                    # 为回字左边
                    r = i + this_w - 1 - (j - 3 * (this_w - 1))
                    c = i
                else:
                    print(i, j)
                    raise ValueError('unknown error')

                # 当前位置数值 （当前层数位置数值 + 当前层数起始基数[外环囊括的所有数字 - 内环囊括的所有数字]）
                array_list[r][c] = j + 1 + (n ** 2 - (n - 2 * i) ** 2)
        return array_list


if __name__ == '__main__':
    n = 5
    s = Solution()
    res = s.generateMatrix(n)
    pprint.pprint(res)
