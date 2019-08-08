#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 14:40
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00066_加一.py
# @Software: PyCharm

"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度：简单

执行用时 :48 ms, 在所有 Python3 提交中击败了81.54%的用户
内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.64%的用户
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 先尾数加一
        digits[-1] += 1
        # 从最后一位往前遍历索引
        for i in range(len(digits) - 1, -1, -1):
            value = digits[i]
            if value > 9:
                # 进位
                digits[i] = value - 10
                if i != 0:
                    # 前一位存在
                    digits[i - 1] += 1
                else:
                    # 前一位不存在，插入最高位，并返回结果列表
                    digits.insert(0, 1)
                    break
            else:
                # 无进位，早停
                break
        return digits


if __name__ == '__main__':
    d = [9, 9, 9, 9]

    s = Solution()
    res = s.plusOne(d)
    print(res)
