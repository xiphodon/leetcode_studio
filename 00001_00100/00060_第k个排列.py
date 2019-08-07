#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 14:08
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00060_第k个排列.py
# @Software: PyCharm

"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :44 ms, 在所有 Python3 提交中击败了92.37%的用户
内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.61%的用户
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        # 可选数字数组
        number_array = [str(i + 1) for i in range(n)]
        # 已选结果集数组
        result_array = list()

        # 0 ~ 9 阶乘值
        cache_factorial_list = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

        def choice_number(number_arr: list, res_arr: list, kk: int) -> None:
            """
            选择排列的数字
            :param number_arr: 可选数字
            :param res_arr: 数字结果集
            :param kk: 当前可选数字顺序排列第kk个排列，kk从0开始
            :return:
            """
            # 可选数字数量
            number_arr_len = len(number_arr)
            if number_arr_len == 0:
                return

            # 选择后的剩余数字的排列数量（对于当前状态来看是 number_arr_len 个小周期中的一个）
            next_status_n = cache_factorial_list[number_arr_len - 1]

            # 小周期数量
            times = kk // next_status_n
            # 小周期中的顺序索引位置 (kk = kk % next_status_n)
            kk = kk - times * next_status_n

            # 原索引落在第几个小周期内，则取当前索引指向的数为当前选出的数字
            res_number = number_arr.pop(times)
            # 收集选出的数字
            res_arr.append(res_number)

            # 继续选择，递归
            choice_number(number_arr, res_arr, kk)

        choice_number(number_array, result_array, k - 1)
        return ''.join(result_array)


if __name__ == '__main__':
    n_num = 4
    k_num = 9

    s = Solution()
    res = s.getPermutation(n_num, k_num)
    print(res)
