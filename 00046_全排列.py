#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 8:59
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00046_全排列.py
# @Software: PyCharm

"""
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :56 ms, 在所有 Python3 提交中击败了98.76%的用户
内存消耗 :13.3 MB, 在所有 Python3 提交中击败了24.79%的用户
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        回溯法
        :param nums:
        :return:
        """
        # 结果集列表
        res_list = list()

        def _permute(sub_nums: List[int], item_res: List[int]):
            """
            回溯体
            :param sub_nums: 待挑选出全排列元素的数组
            :param item_res: 当前分支已挑选出的元素列表
            :return:
            """
            if len(sub_nums) == 0:
                # 待挑选全排列的数组已为空，此分支遍历结束，记录分支结果
                res_list.append(item_res.copy())
            else:
                # 遍历待挑选全排列的数组
                for i, num in enumerate(sub_nums):
                    item_res.append(num)
                    # 子问题继续递归遍历
                    _permute(sub_nums[:i] + sub_nums[i + 1:], item_res)
                    item_res.pop()

        _permute(nums, [])
        return res_list


if __name__ == '__main__':

    nums = [1, 2, 3]

    s = Solution()
    res = s.permute(nums)
    print(res)
