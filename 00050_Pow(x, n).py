#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 14:29
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00050_Pow(x, n).py
# @Software: PyCharm

"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

1、-100.0 < x < 100.0
2、n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/powx-n
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :48 ms, 在所有 Python3 提交中击败了89.38%的用户
内存消耗 :13 MB, 在所有 Python3 提交中击败了98.85%的用户
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:

        def pow_positive(x: float, n: int) -> float:
            """
            pow(x,n)
            x^n
            n 为正数
            :param x:
            :param n:
            :return:
            """
            if n == 0:
                return 1.0
            # 二分法递归调用
            value = pow_positive(x, n // 2)

            if n & 1 == 0:
                # n 为偶数
                return value * value
            else:
                # n 为奇数
                return value * value * x

        if n >= 0:
            return pow_positive(x, n)
        else:
            return 1.0 / pow_positive(x, -n)


if __name__ == '__main__':
    f_num = 2.1
    power = 3

    s = Solution()
    res = s.myPow(f_num, power)
    print(res)



