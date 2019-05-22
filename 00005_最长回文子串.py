#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 16:02
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00005_最长回文子串.py
# @Software: PyCharm

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

难度： 中等

执行用时 : 796 ms, 在Longest Palindromic Substring的Python3提交中击败了74.20% 的用户
内存消耗 : 13 MB, 在Longest Palindromic Substring的Python3提交中击败了93.94% 的用户
"""


class Solution:
    def longestPalindrome_1(self, s: str) -> str:
        # 规划法，性能略低低，LeetCode提交超时
        if len(s) > 0:
            # 指针起始
            ps = 0
            # 指针末尾
            pe = 1
            # 最长子串
            longest_str = None
            # 最长子串长度
            longest_str_len = 0
            while True:
                if pe > len(s):
                    # 尾指针超出范围，则重置起始指针，起始指针+1，尾指针+最长子串长度
                    ps += 1
                    pe = ps + longest_str_len

                    if ps == len(s) or pe > len(s):
                        # 首尾指针达到边界，输出结果
                        return longest_str

                # 首尾指针标记出的字符串
                sub_str = s[ps: pe]
                if self.is_palindrome(sub_str):
                    # 子串为回文数
                    if len(sub_str) > longest_str_len:
                        # 新子串更长则更新
                        longest_str = sub_str
                        longest_str_len = len(sub_str)
                # 尾指针后移
                pe += 1
        else:
            return ''

    def longestPalindrome_2(self, s: str) -> str:
        # 中心扩展法
        if len(s) > 0:
            sub_start_index = 0
            sub_end_index = 0
            for i in range(len(s)):
                # 奇数长度扩展（已i为中心扩展，返回的回文子串为奇数长度）
                len_1 = self.expand_around_center(s, i, i)
                # 偶数长度扩展（已i,i+1为中心扩展，返回的回文子串为偶数长度）
                len_2 = self.expand_around_center(s, i, i + 1)
                # 获取已i为中心扩展的最长长度
                len_0 = max(len_1, len_2)

                if len_0 > sub_end_index - sub_start_index:
                    # 新子串比老子串更长，获取新子串的头尾索引
                    sub_start_index = i - (len_0 - 1) // 2
                    sub_end_index = sub_start_index + len_0

                if len_0 > 2 * (len(s) - (i + 1)):
                    # 当字符串余下长度小于最长回文子串的一半，直接结束
                    break

            return s[sub_start_index: sub_end_index]
        else:
            return ''

    @staticmethod
    def is_palindrome(s: str) -> bool:
        """
        是否为回文数
        :param s:
        :return:
        """
        if len(s) == 0:
            return False

        if len(s) == 1:
            return True

        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False

        return True

    @staticmethod
    def expand_around_center(s: str, left: int, right: int):
        """
        中心扩展
        :param s:
        :param left:
        :param right:
        :return:
        """
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            # 向左右扩展
            left -= 1
            right += 1
        return (right - 1) - (left + 1) + 1


if __name__ == '__main__':
    # string = 'cbbd'
    # string = "esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq"
    string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    s = Solution()
    res = s.longestPalindrome_2(string)
    print(res)
