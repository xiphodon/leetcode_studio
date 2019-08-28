#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 19:42
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00077_组合.py
# @Software: PyCharm


"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :260 ms, 在所有 Python3 提交中击败了73.14%的用户
内存消耗 :15.3 MB, 在所有 Python3 提交中击败了12.32%的用户
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        all_result_list = list()

        def recall(selectable_list: List[int], item_result_list: List[int]):
            """
            回溯法
            :param selectable_list: 可选择列表
            :param item_result_list: 已选择的列表
            :return:
            """
            if len(item_result_list) == k:
                # 位数已收集够，加入结果集
                all_result_list.append(item_result_list[:])
                return

            if len(selectable_list) + len(item_result_list) < k:
                # 可选数字不足，该分支早停
                return

            for i, num in enumerate(selectable_list):
                item_result_list.append(num)
                recall(selectable_list[i + 1:], item_result_list)
                item_result_list.pop()

        recall([i + 1 for i in range(n)], [])

        return all_result_list


if __name__ == '__main__':
    n = 4
    k = 2

    s = Solution()
    res = s.combine(n, k)
    print(res)
