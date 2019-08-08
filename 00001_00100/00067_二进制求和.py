#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 14:58
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00067_二进制求和.py
# @Software: PyCharm

"""
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度：简单

执行用时 :56 ms, 在所有 Python3 提交中击败了63.42%的用户
内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.24%的用户
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        双指针法
        :param a:
        :param b:
        :return:
        """
        # a字符串指针
        p_a = len(a) - 1
        # b字符串指针
        p_b = len(b) - 1
        # 结果集
        res_list = list()
        # 进位
        flag = 0
        while True:
            if p_a >= 0 and p_b >= 0:
                # 两字符串均未遍历结束
                value = int(a[p_a]) + int(b[p_b]) + flag
                if value > 1:
                    value -= 2
                    flag = 1
                else:
                    flag = 0
                res_list.append(str(value))

                p_a -= 1
                p_b -= 1
            elif p_a >= 0 > p_b:
                # a 字符串未遍历完，b 字符串已遍历完
                value = int(a[p_a]) + flag
                if value > 1:
                    value -= 2
                    flag = 1
                else:
                    flag = 0
                res_list.append(str(value))

                p_a -= 1
            elif p_b >= 0 > p_a:
                # b 字符串未遍历完，a 字符串已遍历完
                value = int(b[p_b]) + flag
                if value > 1:
                    value -= 2
                    flag = 1
                else:
                    flag = 0
                res_list.append(str(value))

                p_b -= 1
            else:
                # ab 字符串均已遍历完
                if flag > 0:
                    res_list.append('1')
                    flag = 0
                else:
                    break

        return ''.join(reversed(res_list))


if __name__ == '__main__':
    str_1 = '1010'
    str_2 = '1011'

    s = Solution()
    res = s.addBinary(str_1, str_2)
    print(res)
