#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 10:17
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00014_最长公共前缀.py
# @Software: PyCharm

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

难度： 简单

执行用时 : 40 ms, 在Longest Common Prefix的Python3提交中击败了99.64% 的用户
内存消耗 : 12.9 MB, 在Longest Common Prefix的Python3提交中击败了99.21% 的用户
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res_list = list()
        # 逐位取值
        for i in zip(*strs):
            if len(set(i)) == 1:
                # 都相等
                res_list.append(i[0])
            else:
                break
        return ''.join(res_list)


if __name__ == '__main__':
    lst = ["flower", "flow", "flight"]
    # lst = ["dog", "racecar", "car"]

    s = Solution()
    res = s.longestCommonPrefix(lst)
    print(res)
