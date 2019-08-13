#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 17:33
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00069_x的平方根.py
# @Software: PyCharm


"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度：简单

执行用时 :56 ms, 在所有 Python3 提交中击败了74.85%的用户
内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.22%的用户
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        二分法求平方根
        :param x:
        :return:
        """
        if x == 0:
            return 0

        # 数字平方根下限
        start_root_int = 0
        # 数字平方根上限
        end_root_int = x // 2 + 1

        while True:
            # 二分法，平方根中间值
            middle_root_int = (start_root_int + end_root_int) // 2
            if start_root_int == middle_root_int:
                # 若平方根中间值 与 平方根起始值相等，返回平方根起始值
                return middle_root_int
            # 计算平方根中间值的平方
            value = middle_root_int ** 2
            if value == x:
                # 计算值相等，直接返回平方根
                return middle_root_int
            if value < x:
                # 平方根中间值偏小，将起始值更新为中心值数值
                start_root_int = middle_root_int
            if value > x:
                # 平方根中间值偏大，将终点值更新为中心值数值
                end_root_int = middle_root_int


if __name__ == '__main__':
    num = 917323718

    s = Solution()
    res = s.mySqrt(num)
    print(res)
