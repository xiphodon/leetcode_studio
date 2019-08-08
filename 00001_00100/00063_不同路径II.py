#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 10:44
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00063_不同路径II.py
# @Software: PyCharm

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？


s: start
f: finish

s   *   *   *   *   *   *
*   *   *   *   *   *   *
*   *   *   *   *   *   f


网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度：中等

执行用时 :68 ms, 在所有 Python3 提交中击败了39.81%的用户
内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.19%的用户
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        动态规划
        :param obstacleGrid:
        :return:
        """
        # dp 内每个值为当前位置上有多少条路径
        dp = obstacleGrid
        for r in range(len(dp)):
            for c in range(len(dp[0])):
                # 扫描到当前位置，1 为有障碍，0 为无障碍，检查完毕后，赋值为路径条数
                if dp[r][c] == 0:
                    # 无障碍
                    if r == 0 and c == 0:
                        # 无障碍情况下，左上角格子路径条数初始化为 1
                        dp[r][c] = 1
                    else:
                        # 非左上角格子，根据位置情况赋值路径条数
                        if r == 0:
                            # 第一行，与左侧格子路径条数相同
                            dp[r][c] = dp[r][c - 1]
                        elif c == 0:
                            # 第一列，与上方格子路径条数相同
                            dp[r][c] = dp[r - 1][c]
                        else:
                            # 非第一行，非第一列
                            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
                else:
                    # 有障碍，路径条数为0
                    dp[r][c] = 0
        # print(dp)
        # 返回最后一个位置的路径数
        return dp[-1][-1]


if __name__ == '__main__':
    map_list = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    s = Solution()
    res = s.uniquePathsWithObstacles(map_list)
    print(res)
