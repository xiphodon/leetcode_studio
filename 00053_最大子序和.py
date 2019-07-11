#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 9:48
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00053_最大子序和.py
# @Software: PyCharm


"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 简单

执行用时 :84 ms, 在所有 Python3 提交中击败了25.14%的用户
内存消耗 :13.3 MB, 在所有 Python3 提交中击败了98.73%的用户
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            # 是否将前面的数字传递下去，判断“与前数连接累加和” 与 “以当前元素为开始”，哪种最优
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    res = s.maxSubArray(nums)
    print(res)
