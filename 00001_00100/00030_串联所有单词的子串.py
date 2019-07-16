#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 10:07
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00030_串联所有单词的子串.py
# @Software: PyCharm


"""
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。



示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]

难度： 困难

执行用时 : 1608 ms, 在Substring with Concatenation of All Words的Python3提交中击败了33.55% 的用户
内存消耗 : 13 MB, 在Substring with Concatenation of All Words的Python3提交中击败了100.00% 的用户
"""
from typing import List
import collections


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 滑窗法（分段检验，时间较快）
        len_s = len(s)
        len_words = len(words)

        if len_s == 0 or len_words == 0:
            return []

        len_word = len(words[0])
        len_substring = len_words * len_word

        if len_s < len_substring:
            return []

        res_list = list()

        # 模式字符串统计字典
        words_dict = collections.Counter(words)

        # 获取最长模式串的长度
        # max_len_word_len = max((len(k) for k in words_dict))

        # 窗口首尾指针（前开后闭）
        p_s = 0
        p_e = p_s + len_substring

        while p_e <= len_s:
            # 滑动窗口截取子串
            sub_s = s[p_s: p_e]

            # 复制字母列表
            words_dict_copy = words_dict.copy()

            # 子串指针
            sub_s_point = 0
            while sub_s_point < len_substring:

                # 匹配字符串复制列表临时变量
                temp_item = None
                for item in words_dict_copy:
                    # 当前子串指针指向位置是以模式字符串开头
                    if sub_s.startswith(item, sub_s_point):
                        temp_item = item
                        break
                if temp_item is not None:
                    # 若匹配到匹配字符串，则移除匹配的匹配字符串，指针后移，继续匹配
                    temp_item_count = words_dict_copy[temp_item]
                    # 模式字符串统计字典计数减1，为0则删除
                    if temp_item_count > 1:
                        words_dict_copy[temp_item] -= 1
                    elif temp_item_count == 1:
                        del words_dict_copy[temp_item]

                    sub_s_point += len(temp_item)
                else:
                    # 没匹配到，跳出循环，从新选取子串匹配
                    break

            if len(words_dict_copy) == 0:
                res_list.append(p_s)

            p_s += 1
            p_e += 1

        return res_list

    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        # 滑窗法（全排列组合匹配，耗时较长）

        len_s = len(s)
        len_words = len(words)

        if len_s == 0 or len_words == 0:
            return []

        len_word = len(words[0])
        len_substring = len_words * len_word

        if len_s < len_substring:
            return []

        res_list = list()

        # 子串所有组合
        substring_set = self.get_all_substring_set(words)

        for item_substring in substring_set:
            # 比对所有匹配情况

            # 窗口首尾指针（前开后闭）
            p_s = 0
            p_e = p_s + len_substring

            while p_e <= len_s:
                # 滑动窗口截取子串
                sub_s = s[p_s: p_e]

                if sub_s == item_substring:
                    res_list.append(p_s)

                p_s += 1
                p_e += 1

        return res_list

    def get_all_substring_set(self, words):
        """
        获取所有子串组合
        :param words: 单词列表
        :return:
        """
        # 缓存字典
        temp_dict = dict()

        def get_all_group(lst: List, d=0):
            """
            获取lst元素所有组合
            :param lst: 列表
            :param d: 递归深度
            :return:
            """
            d += 1
            group_set = set()

            len_lst = len(lst)

            for i in range(len_lst):
                # 取出一个元素
                item = lst[i]

                # 剩下元素列表
                remain_list = lst.copy()
                remain_list.pop(i)

                if len(remain_list) != 0:
                    # 剩下元素的组合列表
                    sort_tuple = tuple(sorted(remain_list))
                    if sort_tuple in temp_dict:
                        _list = temp_dict[sort_tuple]
                    else:
                        _list = get_all_group(remain_list, d)
                        temp_dict[sort_tuple] = _list

                    # 拼接成新的组合列表
                    group_set.update(set([item + _item for _item in _list]))
                else:
                    # 拼接成新的组合列表
                    group_set.add(item)

            return list(group_set)

        return get_all_group(words)


if __name__ == '__main__':
    string = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab"
    words = ["ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab",
     "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba",
     "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab",
     "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba",
     "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab",
     "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba",
     "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab",
     "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba",
     "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab",
     "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba",
     "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba", "ab", "ba"]


    # string = "barfoothefoobarman"
    # words = ["foo", "bar"]

    s = Solution()
    res = s.findSubstring(string, words)
    # res = s.get_all_substring_set(words)
    print(res)
