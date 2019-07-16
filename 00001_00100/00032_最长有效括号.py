#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 8:56
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00032_最长有效括号.py
# @Software: PyCharm

"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 困难

执行用时 :68 ms, 在所有Python3提交中击败了93.42%的用户
内存消耗 :13.3 MB, 在所有Python3提交中击败了84.09%的用户
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 时间复杂度 O(n)，空间复杂度 O(n)

        if s == '':
            return 0

        # 检查有效括号串的栈（遇左括号则压入，遇右括号且能与栈顶元素匹配，则弹出匹配的左括号）
        stack = list()
        # 有效成对括号计数列表（能记录成对出现的括号）
        count_list = list()
        # 上一次操作是否弹出括号
        is_last_pop = False
        # 最大计数
        max_count = 0

        # 遍历括号串
        for char in s:
            if len(stack) == 0:
                # 栈空
                stack.append(char)
                count_list.append(0)
                is_last_pop = False
            else:
                # 栈非空
                if stack[-1] == '(' and char == ')':
                    # 左右括号匹配

                    # 弹出左括号
                    stack.pop()

                    if is_last_pop:
                        # 上一次是否弹出
                        # (连续消除成对括号，eg："(())")
                        pop_count = count_list.pop()
                        count_list[-1] += pop_count
                    # 累计此次成对括号数
                    count_list[-1] += 2

                    # 上次计数成对括号是否与此次计数成对括号相邻
                    # (合并消除连续的有效括号的计数，eg："()()")
                    if len(count_list) >= 2 and count_list[-2] > 0:
                        pop_count = count_list.pop()
                        count_list[-1] += pop_count

                    is_last_pop = True
                else:
                    # 左右括号不能匹配
                    stack.append(char)
                    count_list.append(0)
                    is_last_pop = False

            # 每次记录最后计数的大小，并更新最大计数变量
            if len(count_list) > 0:
                if count_list[-1] > max_count:
                    max_count = count_list[-1]

        # print(count_list)
        return max_count


if __name__ == '__main__':
    # str = "(()((())"
    str = "(())()(()"

    s = Solution()
    res = s.longestValidParentheses(str)
    print(res)

