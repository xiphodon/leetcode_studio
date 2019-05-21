#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 10:43
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 1_两数之和.py
# @Software: PyCharm

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

难度： 简单

执行用时 : 48 ms, 在Two Sum的Python3提交中击败了95.99% 的用户
内存消耗 : 14 MB, 在Two Sum的Python3提交中击败了56.54% 的用户
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        list转dict
        值为key，索引为value
        通过散列快速查出所需数字的索引值
        :param nums:
        :param target:
        :return:
        """
        nums_len = len(nums)
        _map = dict()
        if nums_len >= 2:
            for i in range(nums_len):
                # 遍历列表当前值
                cr = nums[i]
                # 求出满足target的所需值
                re = target - cr
                # 在字典中查出所需值的索引
                re_i = _map.get(re)
                if re_i is not None:
                    # 查出则直接返回两数索引
                    return [i, re_i]
                else:
                    # 未查出则把当前值和索引记录在字典中，以便后面所需数查找
                    _map[cr] = i
        else:
            raise ValueError('列表长度不足2')


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    s = Solution()
    l_i = s.twoSum(nums=nums, target=target)
    print(l_i)
