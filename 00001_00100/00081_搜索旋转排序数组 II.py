#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 17:13
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00081_搜索旋转排序数组 II.py
# @Software: PyCharm

"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
进阶:

这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度：中等

执行用时：36 ms, 在所有 Python3 提交中击败了91.86%的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了84.64%的用户
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        二分法查找
        :param nums:
        :param target:
        :return:
        """
        len_nums = len(nums)
        if len_nums == 0:
            return False

        # 左右指针
        left_index = 0
        right_index = len_nums - 1

        while left_index <= right_index:
            # 中间指针
            middle_index = (left_index + right_index) // 2
            if nums[middle_index] == target or nums[left_index] == target or nums[right_index] == target:
                # 左中右指针已找到目标数字
                return True

            if nums[middle_index] == nums[left_index] == nums[right_index]:
                # 左中右指针指向数字一致，缩小左右指针间范围
                left_index += 1
                right_index -= 1
            elif nums[left_index] <= nums[middle_index]:
                # 中间指针在旋转点左侧，即左中指针间为单调递增
                if nums[left_index] < target < nums[middle_index]:
                    # 目标值在左中单调递增之间
                    right_index = middle_index
                else:
                    # 目标值在中间指针右侧
                    left_index = middle_index + 1
            else:
                # 中间指针在旋转点右侧，即中右指针间为单调递增
                if nums[middle_index] < target < nums[right_index]:
                    # 目标值在右中单调递增之间
                    left_index = middle_index + 1
                else:
                    # 目标值在中间指针左侧
                    right_index = middle_index
        return False


if __name__ == '__main__':
    nums = [2, 2, 2, 0, 0, 1]
    target = 0
    print(nums, target)
    s = Solution()
    print(s.search(nums, target))
