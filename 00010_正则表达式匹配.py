#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 13:31
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00010_正则表达式匹配.py
# @Software: PyCharm

"""
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

难度： 困难

执行用时 : 156 ms, 在Regular Expression Matching的Python3提交中击败了35.94% 的用户
内存消耗 : 15.5 MB, 在Regular Expression Matching的Python3提交中击败了5.04% 的用户
"""
# 递归结果缓存
cache_dict = dict()


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        """
        动态规划匹配
        :param s:
        :param p:
        :return:
        """
        if (s, p) in cache_dict:
            return cache_dict.get((s, p))

        s_len = len(s)
        p_len = len(p)

        if s_len > 0 and p_len == 0:
            # 字符串不为空串，模式串为空串，
            cache_dict[(s, p)] = False
            return False

        elif s_len == 0 and p_len == 0:
            # 字符串、模式串均为空串
            cache_dict[(s, p)] = True
            return True

        elif s_len == 0 and p_len > 0:
            # 字符串为空串，模式串不为空串

            if p_len & 1 == 1:
                # 模式串长度为奇数
                cache_dict[(s, p)] = False
                return False

            # p字符串偶数位均为'*'，奇数位均不为'*', 则返回True
            for i in range(p_len):
                if i & 1 == 0 and p[i] == '*':
                    # i为偶数，即奇数位出现*字符
                    cache_dict[(s, p)] = False
                    return False
                if i & 1 == 1 and p[i] != '*':
                    # i为奇数，即偶数位出现非*字符
                    cache_dict[(s, p)] = False
                    return False

            cache_dict[(s, p)] = True
            return True

        else:
            # 字符串、模式串均不为空串

            if s[0] == p[0] or p[0] == '.':
                # 字符串第一位匹配

                if p_len > 1 and p[1] == '*':
                    # 模式串有第二位且第二位为*
                    for i in range(len(s) + 1):
                        # 用i个模式串第一位替换模式串前两位

                        if self.isMatch(s, p[0] * i + p[2:]):
                            cache_dict[(s, p)] = True
                            return True

                    cache_dict[(s, p)] = False
                    return False

                return self.isMatch(s[1:], p[1:])

            elif p[0] == '*':
                # 字符串第一位不匹配 且 模式串第一位为*
                cache_dict[(s, p)] = False
                return False
            else:
                # 字符串第一位不匹配 且 模式串第一位不为*

                if p_len > 1 and p[1] == '*':
                    # 模式串有第二位且第二位为*
                    # 此时算匹配上，*表示0
                    return self.isMatch(s, p[2:])
                else:
                    # 模式串匹配失败
                    cache_dict[(s, p)] = False
                    return False


if __name__ == '__main__':
    string = 'aaaaaa'
    p = 'a*a'

    s = Solution()
    res = s.isMatch(string, p)
    print(res)

