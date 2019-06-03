#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 11:54
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00029_两数相除.py
# @Software: PyCharm

"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

难度： 中等

执行用时 : 64 ms, 在Divide Two Integers的Python3提交中击败了58.54% 的用户
内存消耗 : 13.1 MB, 在Divide Two Integers的Python3提交中击败了93.49% 的用户
"""


class Solution:
    def divide2(self, dividend: int, divisor: int) -> int:
        # 除数翻倍减

        # -(1 << 31)
        min_n = -0x80000000
        # 1 << 31 - 1
        max_n = 0x7fffffff

        if divisor == 0:
            raise ZeroDivisionError()

        # 异或，是否异号。（同号为正,异号为负）
        symbol_positive = dividend ^ divisor >= 0

        # 被除数和除数转成自然数
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor != 1:
            # 除数不为±1

            # 除数翻倍减
            count = 0
            current_times = 1

            while True:

                # 预计算 被除数是否比位移后的新除数大
                temp = dividend - (divisor << current_times)

                if temp > 0:
                    # 被除数大

                    # 更新被除数
                    dividend = temp
                    # 更新商（原始除数的倍数计数）
                    count += 1 << current_times
                    # 除数位移增大
                    current_times <<= 1
                elif temp < 0:
                    # 新除数大
                    if current_times <= 0:
                        # 除数已无法位移右移
                        break
                    else:
                        # 缩小除数，位移右移
                        current_times >>= 1
                else:
                    # 一样大（正好除尽）
                    count += 1 << current_times
                    break

                if count > max_n:
                    break
        else:
            # 除数为±1
            count = dividend

        if not symbol_positive:
            return max(-count, min_n)
        return min(count, max_n)

    def divide(self, dividend: int, divisor: int) -> int:
        # 辗转相减法

        # -(1 << 31)
        min_n = -0x80000000
        # 1 << 31 - 1
        max_n = 0x7fffffff

        if divisor == 0:
            raise ZeroDivisionError()

        if (dividend >= 0 and divisor >= 0) or (dividend < 0 and divisor < 0):
            # 同号为正
            symbol_positive = True
        else:
            # 异号为负
            symbol_positive = False

        # 被除数和除数转成自然数
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor != 1:
            # 除数为±1

            # 循环减
            count = 0
            while True:
                if dividend >= divisor:
                    dividend -= divisor
                    count += 1
                else:
                    break

                if count > max_n:
                    break
        else:
            # 除数不为±1
            count = dividend

        if not symbol_positive:
            return max(-count, min_n)
        return min(count, max_n)


if __name__ == '__main__':
    dividend = 10
    divisor = 3

    s = Solution()
    res = s.divide2(dividend, divisor)
    print(res)
