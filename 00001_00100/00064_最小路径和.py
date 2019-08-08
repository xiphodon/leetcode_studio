#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 11:26
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00064_最小路径和.py
# @Software: PyCharm

"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度：中等

执行用时 :140 ms, 在所有 Python3 提交中击败了28.46%的用户
内存消耗 :15.3 MB, 在所有 Python3 提交中击败了5.12%的用户
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        动态规划
        :param grid:
        :return:
        """
        # dp 内每个值为当前位置上最短路径
        dp = grid
        for r in range(len(dp)):
            for c in range(len(dp[0])):
                if r == 0 and c == 0:
                    # 左上角格子
                    continue
                elif r == 0:
                    # 第一行(不包括左上角格子)
                    dp[r][c] = dp[r][c] + dp[r][c - 1]
                elif c == 0:
                    # 第一列(不包括左上角格子)
                    dp[r][c] = dp[r][c] + dp[r - 1][c]
                else:
                    # 非第一行，非第一列
                    # 到当前位置最少路径
                    dp[r][c] = dp[r][c] + min(dp[r][c - 1], dp[r - 1][c])
        # 返回最后一个位置的路径数
        return dp[-1][-1]


if __name__ == '__main__':
    map_list = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

    s = Solution()
    res = s.minPathSum(map_list)
    print(res)
