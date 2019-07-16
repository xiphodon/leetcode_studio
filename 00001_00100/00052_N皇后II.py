#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 18:45
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00052_N皇后II.py
# @Software: PyCharm


"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 困难

执行用时 :1844 ms, 在所有 Python3 提交中击败了5.21%的用户
内存消耗 :12.9 MB, 在所有 Python3 提交中击败了96.55%的用户
"""

from pprint import pprint
import time


class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        皇后回溯法
        :param n:
        :return:
        """
        res_count = 0

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
                nonlocal res_count
                if q_list[0][1] == q_list[0][2]:
                    res_count += 1
                else:
                    res_count += 2
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
        return res_count


if __name__ == '__main__':
    n = 9

    s = Solution()
    start_time = time.time()
    res = s.totalNQueens(n)
    pprint(res)
    print(time.time() - start_time)
