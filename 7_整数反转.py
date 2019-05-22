#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 9:57
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 7_整数反转.py
# @Software: PyCharm

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

难度： 简单

执行用时 : 48 ms, 在Reverse Integer的Python3提交中击败了98.85% 的用户
内存消耗 : 12.9 MB, 在Reverse Integer的Python3提交中击败了99.84% 的用户
"""


class Solution:
    def reverse(self, x: int) -> int:
        min_n = - (2 << 30)
        max_n = (2 << 30) - 1
        symbol = -1

        if x >= 0:
            symbol = 1

        x_str = str(abs(x))

        x_str = ''.join((x_str[i - 1] for i in range(len(x_str), 0, -1)))
        x = int(x_str) * symbol

        if x > max_n or x < min_n:
            return 0
        else:
            return x


if __name__ == '__main__':
    a = -1563847412

    s = Solution()
    b = s.reverse(a)
    print(b)
