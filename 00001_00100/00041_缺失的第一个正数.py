#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 11:44
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00041_缺失的第一个正数.py
# @Software: PyCharm

"""
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 困难

执行用时 :52 ms, 在所有Python3提交中击败了89.37%的用户
内存消耗 :13 MB, 在所有Python3提交中击败了96.55%的用户
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 缺失的第一个正数，必 小于等于 len(nums) + 1

        # 缓存集合，记录出现过的正整数
        temp_set = set()
        for n in nums:
            # 正整数直接加入集合，负数和零变为0加入集合
            temp_set.add(max(n, 0))

        # 从小到大遍历正整数，区间[1, len(nums) + 1]，发现第一个缺少的，直接返回
        for i in range(1, len(nums) + 2):
            if i not in temp_set:
                return i

        # 异常分支（逻辑上永远不会执行到这里）
        raise Exception('error')


if __name__ == '__main__':
    n_list = [3, 4, 2, 1]

    s = Solution()
    res = s.firstMissingPositive(n_list)
    print(res)
