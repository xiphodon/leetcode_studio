#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 10:45
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00070_爬楼梯.py
# @Software: PyCharm


"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 简单

执行用时 :44 ms, 在所有 Python3 提交中击败了84.58%的用户
内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.14%的用户
"""
cache_dict = dict()


class Solution:
    def climbStairs1(self, n: int) -> int:
        """
        递归
        :param n:
        :return:
        """
        if n in cache_dict:
            # 读缓存
            return cache_dict[n]

        if 0 <= n <= 1:
            return 1
        if n > 1:
            total = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            if n not in cache_dict:
                # 加入缓存
                cache_dict[n] = total
            return total

    def climbStairs(self, n: int) -> int:
        """
        动态规划
        :param n:
        :return:
        """
        # 每一层台阶只跟前两层有关系
        # 到上一阶台阶步数（初始化为第二阶台阶）
        last_one_step = 2
        # 到上两阶台阶步数（初始化为第一阶台阶）
        last_two_step = 1

        if n == 1:
            return last_two_step
        if n == 2:
            return last_one_step

        this_step = None
        for i in range(3, n + 1):
            # 每层情况 = 前两层情况和
            this_step = last_one_step + last_two_step
            # 更新
            last_one_step, last_two_step = this_step, last_one_step
        return this_step


if __name__ == '__main__':
    num = 50

    s = Solution()
    res = s.climbStairs(num)
    print(res)
