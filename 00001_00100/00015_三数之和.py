#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 10:27
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00015_三数之和.py
# @Software: PyCharm

"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]


难度： 中等

执行用时 : 968 ms, 在3Sum的Python3提交中击败了84.14% 的用户
内存消耗 : 16.9 MB, 在3Sum的Python3提交中击败了41.17% 的用户
"""
from typing import List
from collections import Counter


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 值-索引 映射表
        temp = dict()
        # 收集数据集合
        res_set = set()

        # 优化新列表（相同的数字最多留三个）
        new_nums = list()

        # 计数
        count_dict = Counter(nums)

        del nums

        # 相同的数字最多留三个
        for p in count_dict.keys():
            times = min(count_dict[p], 3)
            for _ in range(times):
                new_nums.append(p)

        del count_dict

        for i in range(len(new_nums)):
            if i != 0:
                for j in range(i + 1, len(new_nums)):
                    # 计算出第三个数应该是多少
                    target = -new_nums[i] - new_nums[j]
                    # 第三个数是否以前加入映射表，如果加入则读取
                    if target in temp:
                        # 读取三个数所在索引位置
                        k = temp[target]
                        if k != i and k != j:
                            # 三个数两两不同位置
                            # （i,j在循环range中已经限制不能为同位置，i/j此时还未加入映射表，所以三数两两位置不同）

                            # 结果集去重
                            res_set.add(tuple(sorted([new_nums[i], new_nums[j], target])))
            # 加入映射表
            temp[new_nums[i]] = i
        return list(res_set)


if __name__ == '__main__':
    lst = [-1, 0, 1, 2, -1, -4]
    # lst = [0, 0]

    s = Solution()
    res = s.threeSum(lst)
    print(res)

