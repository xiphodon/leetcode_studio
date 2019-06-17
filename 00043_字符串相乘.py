#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 9:25
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00043_字符串相乘.py
# @Software: PyCharm

"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

1、num1 和 num2 的长度小于110。
2、num1 和 num2 只包含数字 0-9。
3、num1 和 num2 均不以零开头，除非是数字 0 本身。
4、不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multiply-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :216 ms, 在所有Python3提交中击败了46.64%的用户
内存消耗 :13 MB, 在所有Python3提交中击败了91.42%的用户
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        len_num1 = len(num1)
        len_num2 = len(num2)
        len_res = len_num1 + len_num2

        # 竖式计算中带求和的中间值列表的列表
        sum_temp_value_list = list()
        # 结果值列表
        result_value_list = list()
        # 竖式计算
        # 低位到高位计算
        for i in range(len_num1 - 1, -1, -1):
            # 中间值列表
            temp_value_list = list()
            # 高位乘积计算时，低位需要补零
            temp_value_list.extend([0] * (len_num1 - 1 - i))
            # 进位
            temp_carry = 0
            for j in range(len_num2 - 1, -1, -1):
                # 逐个数相乘
                temp_value = int(num1[i]) * int(num2[j]) + temp_carry
                # 十位（进位）
                tens_digit_value = temp_value // 10
                # 个位
                units_digit_value = temp_value % 10

                # 记录到当前中间值列表
                temp_value_list.append(units_digit_value)
                # 更新进位
                temp_carry = tens_digit_value
            # 中间值列表最高位是否有进位，有则追加，无则追加零，最终保证长度一致
            # 保证最终长度均为 len(num1) + len(num2)
            temp_value_list.append(temp_carry)
            temp_value_list.extend([0] * (len_res - len(temp_value_list)))
            # 带求和的中间值列表记录在带求和列表的列表中
            sum_temp_value_list.append(temp_value_list)

        # 求和中间值列表的列表
        temp_carry = 0
        for item_digit_tuple in zip(*sum_temp_value_list):
            # 逐位求和
            temp_value = sum(item_digit_tuple) + temp_carry
            # 十位（进位）
            tens_digit_value = temp_value // 10
            # 个位
            units_digit_value = temp_value % 10

            # 个位记录在结果列表中（倒序）
            result_value_list.append(units_digit_value)
            # 更新进位
            temp_carry = tens_digit_value
        # 最高位是否有进位，有则追加，无则追加零
        result_value_list.append(temp_carry)
        # 结果列表转为数字（索引位置即为进制权重）
        return str(sum(v * 10 ** i for i, v in enumerate(result_value_list)))


if __name__ == '__main__':
    n1 = '123'
    n2 = '456'

    s = Solution()
    res = s.multiply(n1, n2)
    print(res)
    print(int(n1) * int(n2))
