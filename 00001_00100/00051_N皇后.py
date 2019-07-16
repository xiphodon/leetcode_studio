#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 14:38
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00051_N皇后.py
# @Software: PyCharm

"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 困难

执行用时 :1920 ms, 在所有 Python3 提交中击败了5.05%的用户
内存消耗 :13.6 MB, 在所有 Python3 提交中击败了20.00%的用户
"""
import copy
from pprint import pprint
from typing import List

import time


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        皇后回溯法
        :param n:
        :return:
        """
        res_list = list()

        n_square = n * n

        def back_track(q_list, start_index=0):
            """
            回溯体
            :param q_list: 皇后坐标列表
            :param start_index: 检查落子位置起始索引
            :return:
            """

            if len(q_list) == n:
                # 落子完毕，收集结果集
                res_list.append(q_list[:])
                return

            # 一维数组中的落子位置，可落子区间
            for loc in range(start_index, n_square):
                # 一维位置转换为二维位置（行列表示）
                i = loc // n
                j = loc % n

                if len(q_list) == 0 and j > (n - 1) / 2:
                    # 第一步落子 且 第一步落子尝试在第一行的空间中已尝试过半，可通过前半部分结果左右镜像出全部结果
                    return

                # 检查临时皇后落子结果集中是否与当前落子位置有冲突
                # 是否跳过
                is_pass = False
                for r, c, _ in q_list:
                    # 遍历所有已落子的皇后位置
                    if r == i or c == j or abs(r - i) == abs(c - j):
                        # 同行、同列、同斜线
                        # 不可填，跳过
                        is_pass = True
                        break
                if is_pass:
                    continue
                # 当前位置可尝试，填入，(i, j),与其左右镜像(i, n - 1 - j)
                q_list.append((i, j, n - 1 - j))
                # 深度遍历(从下一行开始)
                back_track(q_list, start_index=(i + 1) * n)
                # 回溯
                q_list.pop()

        back_track([])
        print(res_list)
        return self.fmt_res(res_list, n)

    @staticmethod
    def fmt_res(res_list, n):
        """
        格式化结果集
        :param res_list:
        :param n:
        :return:
        """
        fmt_res_list = list()
        for item_list in res_list:
            fmt_item_list = None
            fmt_item_list_mirror = None
            for i, j, mirror_j in item_list:
                if i == 0:
                    fmt_item_list = [['.' for __ in range(n)] for _ in range(n)]
                    if j != mirror_j:
                        fmt_item_list_mirror = copy.deepcopy(fmt_item_list)
                fmt_item_list[i][j] = 'Q'
                fmt_item_list[i] = ''.join(fmt_item_list[i])
                if fmt_item_list_mirror:
                    fmt_item_list_mirror[i][mirror_j] = 'Q'
                    fmt_item_list_mirror[i] = ''.join(fmt_item_list_mirror[i])
            fmt_res_list.append(fmt_item_list)
            if fmt_item_list_mirror:
                fmt_res_list.append(fmt_item_list_mirror)
        return fmt_res_list


if __name__ == '__main__':
    n = 4

    s = Solution()
    start_time = time.time()
    res = s.solveNQueens(n)
    pprint(res)
    print(time.time() - start_time)



