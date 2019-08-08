#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 11:54
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00065_有效数字.py
# @Software: PyCharm

"""
验证给定的字符串是否可以解释为十进制数字。

例如:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：

数字 0-9
指数 - "e"
正/负号 - "+"/"-"
小数点 - "."
当然，在输入中，这些字符的上下文也很重要。

更新于 2015-02-10:
C++函数的形式已经更新了。如果你仍然看见你的函数接收 const char * 类型的参数，请点击重载按钮重置你的代码。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 困难

执行用时 :40 ms, 在所有 Python3 提交中击败了100.00%的用户
内存消耗 :14 MB, 在所有 Python3 提交中击败了5.97%的用户
"""
import re


class Solution:
    def isNumber(self, s: str) -> bool:
        """
        正则匹配
        :param s:
        :return:
        """
        # # 类型强转法
        # try:
        #     float(s.strip())
        #     return True
        # except ValueError:
        #     return False

        # 正整数模式串
        p_int = r'[0-9]+'
        # 正小数模式串
        p_float = r'([0-9]+\.[0-9]*)|([0-9]*\.[0-9]+)'
        # 正科学计数模式串
        p_e = rf'(({p_float})|({p_int}))e[+-]?{p_int}'
        # 总模式串
        p = rf'^[+-]?(({p_int})|({p_float})|({p_e}))$'
        return bool(re.match(p, s.strip()))


if __name__ == '__main__':
    text = ' e   '
    s = Solution()
    res = s.isNumber(text)
    print(res)
