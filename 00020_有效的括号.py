#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 17:30
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00020_有效的括号.py
# @Software: PyCharm

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

难度： 简单

执行用时 : 48 ms, 在Valid Parentheses的Python3提交中击败了92.95% 的用户
内存消耗 : 13 MB, 在Valid Parentheses的Python3提交中击败了95.11% 的用户
"""
mapping = {
    '(': ')',
    '[': ']',
    '{': '}'
}


class Solution:
    def isValid(self, s: str) -> bool:
        # 收集栈
        stack = list()
        for char in s:
            # 遍历字符串
            if len(stack) > 0:
                # 若栈不为空

                # 取出栈顶元素
                list_last_char = stack[-1]
                if mapping.get(list_last_char) == char:
                    # 若栈顶元素与当前字符配对，则栈顶元素弹出
                    stack.pop(-1)
                else:
                    # 若栈顶元素与当前字符不配对，压入新元素
                    stack.append(char)
            elif len(stack) == 0:
                # 若栈为空，压入新元素
                stack.append(char)
            else:
                pass

        # 栈为空时，表示全部配对
        return len(stack) == 0


if __name__ == '__main__':
    string = '()[]{}'

    s = Solution()
    res = s.isValid(string)
    print(res)
