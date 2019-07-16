#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 11:41
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00022_括号生成.py
# @Software: PyCharm

"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

难度： 中等

执行用时 : 104 ms, 在Generate Parentheses的Python3提交中击败了14.78% 的用户
内存消耗 : 13.9 MB, 在Generate Parentheses的Python3提交中击败了5.03% 的用户
"""
from typing import List, Set, Tuple

import time

temp_dict = {}


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        assert n >= 0, 'n must be a positive integer number'
        if n == 0:
            return []

        def generate_parenthesis(num: int) -> Set[Tuple]:
            """
            生成num对有效的括号组合
            :param num:
            :return:
            """
            if num == 1:
                return {('(', ')')}

            _list = generate_parenthesis(num - 1)
            new_set = set()
            for item in _list:
                # 将一对()有效的插入每个有效的item括号串中
                # 这对()要插入后依然有效，需要保证插入后括号中间的括号串依然为有效括号串，且直接括号串长度为偶数
                item_len = len(item)
                for i in range(0, item_len + 1, 2):
                    # 这对()插入时，要保证之间的有效括号串长度为i
                    # 即：在item中找出所有长度为i的有效括号子串
                    if i == 0:
                        # 这对()中无别的括号串
                        for j in range(item_len + 1):
                            # 这对括号要插入的位置
                            item_c = list(item)
                            item_c[j:j] = ['(', ')']
                            # 收集并缓存
                            t_item_c = tuple(item_c)
                            new_set.add(t_item_c)
                            temp_dict[t_item_c] = True

                    else:
                        # 这对()中有长度为i的括号串
                        p_left = 0
                        p_right = i - 1
                        # 这对括号要插入到p_left前 和 p_right后
                        while p_right < item_len:
                            item_c = list(item)
                            sub_item = item_c[0: i + 1]
                            if self.list_is_valid(sub_item):
                                # 是有效的括号子列表

                                # 插入新括号
                                item_c[p_left: p_left] = ['(']
                                item_c[p_right + 1: p_right + 1] = [')']
                                # 收集并缓存
                                t_item_c = tuple(item_c)
                                new_set.add(t_item_c)
                                temp_dict[t_item_c] = True

                                p_left += 2
                                p_right += 2
                            else:
                                p_left += 1
                                p_right += 1
            return new_set

        res_set = generate_parenthesis(n)
        return [''.join(i) for i in res_set]

    def list_is_valid(self, lst: list) -> bool:
        """
        是否是有效的括号列表
        :param lst:
        :return:
        """
        mapping = {
            '(': ')'
        }

        tup = tuple(lst)
        if tup in temp_dict:
            return temp_dict[tup]

        if lst[-1] == '(' or lst[0] == ')':
            return False

        stack = list()
        for i in tup:
            if len(stack) == 0:
                stack.append(i)
            else:
                if mapping[stack[-1]] == i:
                    stack.pop()
                else:
                    stack.append(i)

        res_bool = len(stack) == 0
        temp_dict[tup] = res_bool
        return res_bool


if __name__ == '__main__':
    s = Solution()

    # temp_list = ['(', '(', ')', '(', ')', ')']
    # res_bool = s.list_is_valid(temp_list)
    # print(res_bool)

    time_start = time.time()
    res = s.generateParenthesis(10)
    # print(res)
    print('res', time.time() - time_start)




