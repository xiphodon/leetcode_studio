#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 10:04
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00035_搜索插入位置.py
# @Software: PyCharm

"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 简单

执行用时 :44 ms, 在所有Python3提交中击败了97.67%的用户
内存消耗 :13.6 MB, 在所有Python3提交中击败了91.34%的用户
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        二分法
        :param nums:
        :param target:
        :return:
        """
        len_nums = len(nums)

        if len_nums == 0:
            return 0

        # 左右指针
        left_index = 0
        right_index = len_nums - 1

        while left_index < right_index:
            # 中间指针
            middle_index = (left_index + right_index) // 2
            if nums[middle_index] == target:
                # 直接找到则返回
                return middle_index
            elif nums[middle_index] > target:
                # 折半查找
                right_index = middle_index
            else:
                # 折半查找
                left_index = middle_index + 1

        # 判断最后左右指针相遇时，所指向的数值和目标值大小
        if nums[left_index] >= target:
            return left_index
        else:
            return left_index + 1


if __name__ == '__main__':
    n_list = [1, 3, 5, 6]
    # n_list = [1, 3]
    target = 7

    s = Solution()
    print(n_list, target)
    res = s.searchInsert(n_list, target)
    print(res)
