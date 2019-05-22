#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 8:56
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 6_Z字变换.py
# @Software: PyCharm

"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G

难度： 中等

执行用时 : 92 ms, 在ZigZag Conversion的Python3提交中击败了88.34% 的用户
内存消耗 : 13 MB, 在ZigZag Conversion的Python3提交中击败了97.64% 的用户
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 输出接收列表
        if numRows > 0:

            if numRows == 1:
                # 只有一行
                return s

            res_list = list()
            for r in range(numRows):
                # 字符串指针（起始位置为行号位置）
                p = r
                # 指针移动次数是否是偶数次
                is_even_times = False
                while p < len(s):
                    res_list.append(s[p])

                    if r == 0:
                        # 第一行
                        p = p + (numRows - 1) * 2
                    elif r == numRows - 1:
                        # 最后一行
                        p = p + r * 2
                    else:
                        # 中间行
                        if is_even_times:
                            # 偶数次
                            p = p + r * 2
                        else:
                            # 奇数次
                            p = p + (numRows - 1 - r) * 2
                        # 每执行一次，奇偶转换
                        is_even_times = not is_even_times

            return ''.join(res_list)
        else:
            raise ValueError('输出行数不能为0')


if __name__ == '__main__':
    string = 'A'
    rows = 1

    s = Solution()
    res_str = s.convert(string, rows)
    print(res_str)
