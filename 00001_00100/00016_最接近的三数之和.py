#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 12:01
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00016_最接近的三数之和.py
# @Software: PyCharm

"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

难度： 中等

执行用时 : 216 ms, 在3Sum Closest的Python3提交中击败了36.05% 的用户
内存消耗 : 13 MB, 在3Sum Closest的Python3提交中击败了92.12% 的用户
"""
from typing import List


class Solution:
    def threeSumClosest_1(self, nums: List[int], target: int) -> int:
        # 最小差值
        min_value = None
        sum_value = None
        # 三循环遍历所有值
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # 两数之和
                sum_2 = nums[i] + nums[j]
                for k in range(j + 1, len(nums)):
                    # 三数之和
                    sum_3 = sum_2 + nums[k]
                    # 三数之和与目标值差值
                    abs_value = abs(target - sum_3)
                    if (min_value is None) or (abs_value < min_value):
                        if abs_value == 0:
                            return sum_3
                        # 更新最小差值
                        min_value = abs_value
                        sum_value = sum_3

        return sum_value

    def threeSumClosest_2(self, nums: List[int], target: int) -> int:
        # 排序
        nums = sorted(nums)

        # 最小差值
        min_value = None
        # 最小差值的三数和
        sum_value = None

        # 选定中间数
        for i in range(1, len(nums) - 1):
            # 左右两数指针
            p_l = 0
            p_r = len(nums) - 1

            # 左右两数指针往中间移动，直到找到最小差值的三数和
            while p_l < i < p_r:
                # 三数和
                sum_3 = sum((nums[p_l], nums[i], nums[p_r]))
                # 偏差
                bias = sum_3 - target
                # 绝对偏差
                abs_value = abs(bias)

                if abs_value == 0:
                    return sum_3

                if (min_value is None) or (abs_value < min_value):
                    min_value = abs_value
                    sum_value = sum_3

                if bias < 0:
                    # 三数和小于目标值，左指针右移，左数变大
                    p_l += 1
                else:
                    # 三数和大于目标值，右指针左移，右数变小
                    p_r -= 1

        return sum_value


if __name__ == '__main__':
    lst = [-1, 2, 1, -4]
    target_int = 1

    s = Solution()
    res = s.threeSumClosest_2(lst, target_int)
    print(res)
