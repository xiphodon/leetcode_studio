#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 9:04
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00078_子集.py
# @Software: PyCharm


"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度：中等

执行用时 :44 ms, 在所有 Python3 提交中击败了98.16%的用户
内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.27%的用户
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # 结果集
        all_result_list = list()

        def recall(selectable_list: List[int], item_result_list: List[int], set_lenght: int):
            """
            回溯体
            :param selectable_list:
            :param item_result_list:
            :param set_lenght:
            :return:
            """
            if len(item_result_list) == set_lenght:
                # 满足集合长度，收集，分支停止
                all_result_list.append(item_result_list[:])
                return

            if len(item_result_list) >= set_lenght:
                # 边界检查，超出规定长度，分支停止
                return

            if len(selectable_list) + len(item_result_list) < set_lenght:
                # 可选数字不足，分支早停
                return

            for idx, item in enumerate(selectable_list):
                item_result_list.append(item)
                recall(selectable_list[idx + 1:], item_result_list, set_lenght)
                item_result_list.pop()

        # 尝试所有子集的长度
        for i in range(len(nums) + 1):
            recall(nums, [], i)

        return all_result_list


if __name__ == '__main__':
    nums = [1, 2, 3]

    s = Solution()
    res = s.subsets(nums)
    print(res)
