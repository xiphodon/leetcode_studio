#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 11:22
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00028_实现strStr方法.py
# @Software: PyCharm

"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

难度： 简单

执行用时 : 60 ms, 在Implement strStr()的Python3提交中击败了52.34% 的用户
内存消耗 : 13 MB, 在Implement strStr()的Python3提交中击败了99.05% 的用户
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 模式串为空串，返回0
        if needle == '':
            return 0

        len_haystack = len(haystack)
        len_needle = len(needle)

        # 模式串长度大于字符串，返回0
        if len_needle > len_haystack:
            return -1

        # 字符串指针
        p_haystack = 0
        # 模式串指针
        p_needle = 0

        while p_haystack < len_haystack:
            # 字符串指针小于字符串长度

            if haystack[p_haystack] == needle[p_needle]:
                # 对应字符相等

                # 双指针右移
                p_haystack += 1
                p_needle += 1
            else:
                # 对应字符不相等

                # 字符串指针回退，模式串指针归0
                p_haystack = p_haystack - p_needle + 1
                p_needle = 0

            if p_needle == len_needle:
                # 模式串匹配结束
                return p_haystack - p_needle
        return -1


if __name__ == '__main__':
    h = 'hello'
    n = 'll'

    s = Solution()
    res = s.strStr(h, n)
    print(res)
