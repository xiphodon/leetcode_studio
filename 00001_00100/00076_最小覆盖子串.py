#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 16:31
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00076_最小覆盖子串.py
# @Software: PyCharm

"""
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 困难

执行用时 :668 ms, 在所有 Python3 提交中击败了18.34%的用户
内存消耗 :24.5 MB, 在所有 Python3 提交中击败了6.43%的用户
"""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 模式串集合
        t_set = set(t)
        # 模式串长度
        t_len = len(t)
        # 字符串集合
        s_set = set(s)

        if len(s_set & t_set) != len(t_set):
            # 模式串中字符不全在字符串中出现
            return ''

        # 字符串中含有模式串中字符的索引列表
        index_char_list = list()
        for i, c in enumerate(s):
            if c in t_set:
                # 每个元素为 (索引，索引对应字符)
                index_char_list.append((i, c))

        if len(index_char_list) < t_len:
            # 模式串中有重复字符串，未出现指定次数
            return ''

        # print(index_char_list)

        # 统计计数模式串字符
        counter_t_dict = Counter(t)
        # print(counter_t_dict)

        # 满足的所有结果  [子串长度, [子串起始索引, 子串结尾索引]] 包含起始索引
        min_s_sub_list = [None, [None, None]]

        # 指针开始、截止，半开半闭 [p_s, p_e)
        p_s = 0
        p_e = p_s + t_len

        counter_s_sub_char_dict = None
        is_p_e_right_move = False
        is_p_s_right_move = False

        while True:

            if p_e > len(index_char_list):
                # 尾指针已到达尾部
                break

            if counter_s_sub_char_dict is None:
                # 字符串中，定长范围内，一定包含t长度个t串所有关键字符
                # s包含t字符的索引列表，取出当前可能包含t字符串的子列表
                s_sub_key_char_list = index_char_list[p_s: p_e]
                # 取出子列表中包含t字符的字符
                s_sub_char_list = (i for _, i in s_sub_key_char_list)
                # 统计计数当前子列表各个字符串数量
                counter_s_sub_char_dict = Counter(s_sub_char_list)
            else:
                if is_p_e_right_move:
                    # 上一步尾指针右移
                    # 上一步尾指针位置
                    last_p_e = p_e - 1
                    # 上一步尾指针所指向的关键字符
                    last_p_e_char = index_char_list[last_p_e][1]
                    # 统计计数对应字符自增
                    counter_s_sub_char_dict[last_p_e_char] += 1

                if is_p_s_right_move:
                    # 上一步头指针右移
                    # 上一步头指针右移
                    last_p_s = p_s - 1
                    # 上一步头指针所指向的关键字符
                    last_p_s_char = index_char_list[last_p_s][1]
                    # 统计计数对应字符自减
                    counter_s_sub_char_dict[last_p_s_char] -= 1

            # 跳过当前循环的标记
            while_continue_flag = False
            # 尾指针右移标记抹除
            is_p_e_right_move = False
            # 头指针右移标记抹除
            is_p_s_right_move = False

            for k, v in counter_t_dict.items():
                # 遍历模式串统计计数，k为字符，v为数量
                if counter_s_sub_char_dict.get(k, 0) < v:
                    # 子列表中包含的必须字符k的数量不足模式串应有的数量v
                    # 尾指针向后移动，扩大筛选范围
                    p_e += 1
                    # 尾指针右移标记
                    is_p_e_right_move = True
                    # 跳过后续步骤，直接进行下次while循环
                    while_continue_flag = True
                    break

            if while_continue_flag:
                # 跳过当前步，进行下个循环
                continue
            else:
                # 当前子列表已包含t模式串所有字符

                # 获取字符串s匹配的子串头尾指针（包含前指针所指元素、包含后指针所指元素）
                s_start_index = index_char_list[p_s][0]
                s_end_index = index_char_list[p_e - 1][0]
                # 保存当前匹配的子串  元素（子串长度，（起始索引，末尾索引）），包括前后指针所指元素
                if min_s_sub_list[0] is None or s_end_index - s_start_index < min_s_sub_list[0]:
                    # 最短子串不存在 或 新子串更短
                    # 更新最短子串
                    min_s_sub_list = [s_end_index - s_start_index, [s_start_index, s_end_index]]

                # 尝试缩短子串
                p_s += 1
                # 头指针位移操作
                is_p_s_right_move = True

        if min_s_sub_list[0] is None:
            # 空结果集
            return ''
        else:
            # 在结果集中取出最短的子串索引（包含前后指针所指的元素）
            s_s, s_e = min_s_sub_list[1]
            # print(result_index_list)
            # print(s)
            return s[s_s: s_e + 1]


if __name__ == '__main__':
    s1 = 'ADOBECODEBANC'
    s2 = 'ABC'

    s = Solution()
    res = s.minWindow(s1, s2)
    print(res)
