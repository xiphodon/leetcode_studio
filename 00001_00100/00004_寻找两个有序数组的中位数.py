#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 13:13
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00004_寻找两个有序数组的中位数.py
# @Software: PyCharm

"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

难度： 困难

执行用时 : 104 ms, 在Median of Two Sorted Arrays的Python3提交中击败了66.22% 的用户
内存消耗 : 13.2 MB, 在Median of Two Sorted Arrays的Python3提交中击败了93.25% 的用户
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 时间复杂度为 O(m + n)
        new_list = list()
        l1_len = len(nums1)
        l2_len = len(nums2)
        total_len = l1_len + l2_len
        middle = total_len // 2
        # 是否为偶数
        is_even = False

        if total_len & 1 == 0:
            # 偶数
            is_even = True

        # 列表nums1的指针
        p1 = 0
        # 列表nums2的指针
        p2 = 0
        while True:
            if len(new_list) >= middle + 1:
                # 新列表收集数字已过半数，提前结束循环
                break

            if p1 < l1_len and p2 < l2_len:
                # nums1 nums2 遍历未完
                if nums1[p1] <= nums2[p2]:
                    new_list.append(nums1[p1])
                    p1 += 1
                else:
                    new_list.append(nums2[p2])
                    p2 += 1
            elif p1 >= l1_len and p2 < l2_len:
                # nums1 遍历完毕， nums2 遍历未完
                new_list.append(nums2[p2])
                p2 += 1
            elif p1 < l1_len and p2 >= l2_len:
                # nums2 遍历完毕， nums1 遍历未完
                new_list.append(nums1[p1])
                p1 += 1
            else:
                # nums1 nums2 遍历完毕
                break

        if is_even:
            return (new_list[middle - 1] + new_list[middle]) / 2
        else:
            return new_list[middle]


if __name__ == '__main__':
    l1 = [1, 3, 4, 5]
    l2 = [2, 4, 6, 7, 9]

    s = Solution()
    res = s.findMedianSortedArrays(l1, l2)
    print(res)
