#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 13:43
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00018_四数之和.py
# @Software: PyCharm

"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

难度： 中等

执行用时 : 1016 ms, 在4Sum的Python3提交中击败了62.26% 的用户
内存消耗 : 13 MB, 在4Sum的Python3提交中击败了94.54% 的用户
"""
from typing import List
from collections import Counter


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 值-索引 映射表
        temp = dict()
        # 收集数据集合
        res_set = set()

        # 优化新列表（相同的数字最多留四个）
        new_nums = list()

        # 计数
        count_dict = Counter(nums)

        del nums

        # 相同的数字最多留四个
        for p in count_dict.keys():
            times = min(count_dict[p], 4)
            for _ in range(times):
                new_nums.append(p)

        del count_dict

        for i in range(len(new_nums)):
            if i != 0:
                for j in range(i + 1, len(new_nums)):
                    for k in range(j + 1, len(new_nums)):
                        # 计算出第四个数应该是多少
                        four = target - new_nums[i] - new_nums[j] - new_nums[k]

                        # 第四个数是否以前加入映射表，如果加入则读取
                        if four in temp:
                            # 读取四个数所在索引位置
                            m = temp[four]
                            if m != i and m != j and m != k:
                                # 四个数两两不同位置
                                # （i,j,k在循环range中已经限制不能为同位置，i/j/k此时还未加入映射表，所以四数两两位置不同）

                                # 结果集去重
                                res_set.add(tuple(sorted([new_nums[i], new_nums[j], new_nums[k], four])))
            # 加入映射表
            temp[new_nums[i]] = i
        return list(res_set)


if __name__ == '__main__':
    lst = [-1, 0, 1, 0, -2, 2]
    target = 0
    # lst = [0, 0]

    s = Solution()
    res = s.fourSum(lst, target)
    print(res)

