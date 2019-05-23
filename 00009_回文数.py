#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 13:20
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00009_回文数.py
# @Software: PyCharm

"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？

难度： 简单

执行用时 : 80 ms, 在Palindrome Number的Python3提交中击败了99.61% 的用户
内存消耗 : 13.1 MB, 在Palindrome Number的Python3提交中击败了95.55% 的用户
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            # 负数恒不为回文数
            return False

        if 0 <= x < 10:
            # 正个位数恒为回文数
            return True

        # 转为字符串
        s = str(x)
        s_len = len(s)

        # 首尾对比是否为回文数
        for i in range((s_len + 1) // 2):
            if s[i] != s[s_len - 1 - i]:
                return False

        return True


if __name__ == '__main__':
    n = 12121

    s = Solution()
    res = s.isPalindrome(n)
    print(res)
