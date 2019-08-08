#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 17:36
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00062_不同路径.py
# @Software: PyCharm

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

s: start
f: finish

s   *   *   *   *   *   *
*   *   *   *   *   *   *
*   *   *   *   *   *   f


例如，上图是一个7 x 3 的网格。有多少可能的路径？

说明：m 和 n 的值均不超过 100。

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度：中等

执行用时 :40 ms, 在所有 Python3 提交中击败了96.11%的用户
内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.14%的用户
"""
import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        排列组合问题
        :param m:
        :param n:
        :return:
        """
        # 可向右步数
        right_steps = m - 1
        # 可向下步数
        down_steps = n - 1
        # 共移动步数
        all_steps = right_steps + down_steps

        # 算法1
        # result = math.factorial(all_steps) // math.factorial(right_steps) // math.factorial(down_steps)

        # 算法2
        # 将两种方向分为大数、小数，大数阶乘可与总步数阶乘约分，化简计算次数
        if right_steps >= down_steps:
            big_steps = right_steps
            small_steps = down_steps
        else:
            big_steps = down_steps
            small_steps = right_steps

        result = 1

        for i in range(big_steps + 1, all_steps + 1):
            result *= i

        result //= math.factorial(small_steps)

        return result


if __name__ == '__main__':
    m = 7
    n = 3
    s = Solution()
    res = s.uniquePaths(m, n)
    print(res)
