#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 16:08
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00075_颜色分类.py
# @Software: PyCharm

"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :40 ms, 在所有 Python3 提交中击败了97.96%的用户
内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.21%的用户
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        三指针

        头指针（跟踪排序好的0的尾，所指向元素为已排序好的最后一个0的后一个位置）
        尾指针（跟踪排序好的2的头，所指向元素为已排序好的第一个2的前一个位置）
        遍历指针（待排序的序列头）
        遍历指针恒在头指针与尾指针之间
        """
        nums_len = len(nums)
        if nums_len == 0:
            return

        start_p = 0
        current_p = 0
        end_p = nums_len - 1

        while current_p <= end_p:

            if nums[current_p] == 0:
                # 当前元素为0，与头指针元素交换
                nums[start_p], nums[current_p] = nums[current_p], nums[start_p]
                # 交换后头指针右移
                start_p += 1
                # 遍历指针右移，保证遍历指针在头尾指针之间
                current_p += 1
            elif nums[current_p] == 2:
                # 当前元素为2，与尾指针元素交换
                nums[current_p], nums[end_p] = nums[end_p], nums[current_p]
                # 交换后尾指针左移
                end_p -= 1
            else:
                # 当前元素为1，当前指针右移
                current_p += 1


if __name__ == '__main__':
    num_list = [2, 0, 1]

    s = Solution()
    print(num_list)
    s.sortColors(num_list)
    print(num_list)

