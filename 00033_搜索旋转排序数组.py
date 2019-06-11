#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 10:08
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00033_搜索旋转排序数组.py
# @Software: PyCharm

"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :44 ms, 在所有Python3提交中击败了97.69%的用户
内存消耗 :13.1 MB, 在所有Python3提交中击败了90.81%的用户
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        二分法查找
        :param nums:
        :param target:
        :return:
        """
        len_nums = len(nums)

        if len_nums == 0:
            return -1

        # 先升序排列，并返回旋转的点
        nums, start_index = self.asc_sort(nums)

        left_index = 0
        middle_index = (len_nums - 1) // 2
        right_index = len_nums - 1

        # 二分法查找目标值位置，并根据旋转点推算出原始位置
        while True:
            if left_index + 1 == right_index or left_index == right_index:
                if nums[left_index] == target:
                    return (left_index + start_index) % len_nums
                elif nums[right_index] == target:
                    return (right_index + start_index) % len_nums
                else:
                    return -1

            if nums[middle_index] == target:
                return (middle_index + start_index) % len_nums
            elif nums[left_index] <= target < nums[middle_index]:
                right_index = middle_index
                middle_index = (left_index + right_index) // 2
            elif nums[middle_index] < target <= nums[right_index]:
                left_index = middle_index
                middle_index = (left_index + right_index) // 2
            else:
                return -1

    def asc_sort(self, nums):
        """
        升序排序（二分法）
        :param nums:
        :return: 升序数组，旋转点位置
        """
        len_nums = len(nums)

        left_index = 0
        middle_index = (len_nums - 1) // 2
        right_index = len_nums - 1

        if nums[left_index] <= nums[right_index]:
            # 若原始即为升序排列，则直接返回
            return nums, 0

        # 二分法查找旋转位置，并根据旋转点位置返回升序数组
        while True:
            if left_index + 1 == right_index or left_index == right_index:
                if nums[left_index] > nums[right_index]:
                    middle_index = right_index
                else:
                    middle_index = left_index
                break

            if nums[left_index] > nums[right_index]:
                if nums[left_index] <= nums[middle_index]:
                    left_index = middle_index
                    middle_index = (left_index + right_index) // 2
                elif nums[middle_index] < nums[right_index]:
                    right_index = middle_index
                    middle_index = (left_index + right_index) // 2

        return nums[middle_index:] + nums[:middle_index], middle_index


if __name__ == '__main__':
    n_list = [4, 5, 6, 7, 0, 1, 2]
    n_list = [1]
    target = 3
    target = 1
    print(n_list, target)

    s = Solution()
    res = s.search(n_list, target)
    print(res)
