#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 9:27
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00034_在排序数组中查找元素的第一个和最后一个位置.py
# @Software: PyCharm

"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :44 ms, 在所有Python3提交中击败了99.08%的用户
内存消耗 :13.6 MB, 在所有Python3提交中击败了96.93%的用户
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        二分法
        :param nums:
        :param target:
        :return:
        """
        len_nums = len(nums)

        if len_nums == 0:
            return [-1, -1]

        # 左中右三个指针
        left_index = 0
        right_index = len_nums - 1
        middle_index = (left_index + right_index) // 2

        while True:
            if left_index == right_index:
                # 左右指针相遇
                if nums[left_index] == target:
                    # 左右指针指向的同一个数为目标数
                    return [left_index, right_index]
                else:
                    # 左右指针指向的同一个数不为目标数
                    return [-1, -1]
            elif left_index + 1 == right_index:
                # 左右指针相邻
                if nums[left_index] == nums[right_index] == target:
                    # 左右指针指向的数都等于目标数
                    return [left_index, right_index]
                elif nums[left_index] == target and nums[right_index] != target:
                    # 仅左指针指向的数等于目标数
                    return [left_index, left_index]
                elif nums[right_index] == target and nums[left_index] != target:
                    # 仅右指针指向的数等于目标数
                    return [right_index, right_index]
                else:
                    # 左右指针指向的数都不等于目标数
                    return [-1, -1]
            else:
                # 左右指针指不相邻
                if nums[middle_index] == target:
                    # 中指针指向数等于目标数
                    if nums[left_index] == nums[right_index] == target:
                        # 若此时左右指针已指向目标数，直接返回左右指针索引
                        return [left_index, right_index]
                    elif nums[left_index] == target and nums[right_index] != target:
                        # 左指针已找到起始的目标数，右指针递减查找
                        right_index -= 1
                        middle_index = (left_index + right_index) // 2
                    elif nums[right_index] == target and nums[left_index] != target:
                        # 右指针已找到结尾的目标数，左指针递增查找
                        left_index += 1
                        middle_index = (left_index + right_index) // 2
                    else:
                        # 左右指针均未找到目标数，同时向中间移动
                        left_index += 1
                        right_index -= 1
                        middle_index = (left_index + right_index) // 2
                elif nums[middle_index] > target:
                    # 中指针指向数大于目标数，检索范围折半
                    right_index = middle_index
                    middle_index = (left_index + right_index) // 2
                elif nums[middle_index] < target:
                    # 中指针指向数小于目标数，检索范围折半
                    left_index = middle_index
                    middle_index = (left_index + right_index) // 2
                else:
                    # 其他条件范围，无执行机会
                    raise Exception('error')


if __name__ == '__main__':
    n_list = [5, 7, 7, 8, 8, 10]
    target = 6

    s = Solution()
    print(n_list, target)
    res = s.searchRange(n_list, target)
    print(res)
