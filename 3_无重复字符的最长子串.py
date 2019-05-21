#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 11:28
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 3_无重复字符的最长子串.py
# @Software: PyCharm

"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

难度： 中等

执行用时 : 108 ms, 在Longest Substring Without Repeating Characters的Python3提交中击败了71.04% 的用户
内存消耗 : 13.1 MB, 在Longest Substring Without Repeating Characters的Python3提交中击败了96.90% 的用户
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        if s_len >= 0:
            # 起始指针指向索引
            ps = 0
            # 末尾指针指向索引
            pe = 1
            sub_max_len = 0

            while True:
                if pe > s_len:
                    # 末尾指针超出字符串长度，结束循环
                    break

                if sub_max_len >= s_len - ps:
                    # 起始指针位置已进入最后一定区域中，无论末尾指针在哪，长度均小于已有最大长度，结束循环
                    break

                sub_str = s[ps: pe]
                sub_str_len = len(sub_str)

                if sub_str_len > 1:
                    # 子串中是否有与最后一位重复的字符
                    repeat_index = sub_str[: -1].find(sub_str[-1])
                    if repeat_index >= 0:
                        # 有重复的

                        # 重复位置前的部分舍弃，更新起始指针位置
                        ps = ps + repeat_index + 1
                        # 末尾指针后移
                        pe += 1
                    else:
                        # 无重复的
                        sub_max_len = max(sub_max_len, len(sub_str))
                        # 末尾指针后移
                        pe += 1
                else:
                    # 子串长度为1
                    sub_max_len = max(sub_max_len, sub_str_len)
                    # 末尾指针后移
                    pe += 1

            return sub_max_len

        else:
            raise ValueError('字符串长度为0')


if __name__ == '__main__':
    str1 = 'abcabcbb'
    str2 = 'bbbbb'
    str3 = 'pwwkew'

    s = Solution()
    res_len = s.lengthOfLongestSubstring(str3)
    print(res_len)
