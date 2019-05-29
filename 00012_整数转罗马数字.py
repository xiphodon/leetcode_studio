#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 8:55
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00012_整数转罗马数字.py
# @Software: PyCharm

"""
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:

输入: 3
输出: "III"
示例 2:

输入: 4
输出: "IV"
示例 3:

输入: 9
输出: "IX"
示例 4:

输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.
示例 5:

输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.

难度： 中等

执行用时 : 84 ms, 在Integer to Roman的Python3提交中击败了82.58% 的用户
内存消耗 : 13.1 MB, 在Integer to Roman的Python3提交中击败了94.85% 的用户
"""

from collections import OrderedDict

mapping = OrderedDict({
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
})


class Solution:
    def intToRoman(self, num: int) -> str:
        assert num >= 0, 'num must be natural number'
        assert num < 4000, 'num must be less than 4000'

        for k, v in mapping.items():
            if num >= k:
                return num // k * v + self.intToRoman(num % k)
        return ''

        # 相当于

        # if num >= 1000:
        #     return num // 1000 * mapping[1000] + self.intToRoman(num % 1000)
        # elif num >= 900:
        #     return mapping[900] + self.intToRoman(num - 900)
        # elif num >= 500:
        #     return mapping[500] + self.intToRoman(num - 500)
        # elif num >= 400:
        #     return mapping[400] + self.intToRoman(num - 400)
        # elif num >= 100:
        #     return num // 100 * mapping[100] + self.intToRoman(num % 100)
        # elif num >= 90:
        #     return mapping[90] + self.intToRoman(num - 90)
        # elif num >= 50:
        #     return mapping[50] + self.intToRoman(num - 50)
        # elif num >= 40:
        #     return mapping[40] + self.intToRoman(num - 40)
        # elif num >= 10:
        #     return num // 10 * mapping[10] + self.intToRoman(num % 10)
        # elif num >= 9:
        #     return mapping[9] + self.intToRoman(num - 9)
        # elif num >= 5:
        #     return mapping[5] + self.intToRoman(num - 5)
        # elif num >= 4:
        #     return mapping[4] + self.intToRoman(num - 4)
        # elif num >= 1:
        #     return num // 1 * mapping[1] + self.intToRoman(num % 1)
        # elif num == 0:
        #     return ''
        # else:
        #     pass


if __name__ == '__main__':
    n = 4

    s = Solution()
    res = s.intToRoman(n)

    print(res)
