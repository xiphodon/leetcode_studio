#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 15:44
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00031_下一个排列.py
# @Software: PyCharm

"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

难度： 中等

执行用时 : 60 ms, 在Next Permutation的Python3提交中击败了88.14% 的用户
内存消耗 : 13 MB, 在Next Permutation的Python3提交中击败了96.96% 的用户
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return

        len_nums = len(nums)
        p = len_nums - 2

        # 从后向前遍历
        while p >= 0:
            if self.is_desc_order(nums, start=p):
                # 借位
                if p - 1 >= 0:
                    # 有位可借
                    p -= 1
                    continue
                else:
                    # 无位可借
                    self.asc_sort(nums)
                    break
            else:
                # 从当前p指针指向的数值后选取一个仅大于p指针指向数值的数，作为当前位置新数，剩下数字升序排列
                self.next_permutation(nums, p)
                break

    def is_desc_order(self, nums: List, start: int=0) -> bool:
        """
        从起始位置检查，是否为倒序排列
        :param nums:
        :param start: 起始位置（包含起始位置）
        :return:
        """
        len_nums = len(nums) - start
        if len_nums <= 1:
            return True

        for i in range(len_nums - 1):
            if nums[start+i] < nums[start+i+1]:
                return False
        return True

    def asc_sort(self, nums: list, start: int=0) -> None:
        """
        升序排列
        支持部分排序
        :param nums:
        :param start: 排序的起始位置（包含此位置）
        :return:
        """
        len_nums = len(nums)
        if len_nums <= 1:
            return

        for i in range(start, len_nums - 1):
            for j in range(i+1, len_nums):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

    def next_permutation(self, nums: list, p: int) -> None:
        """
        从当前p指针指向的数值后选取一个仅大于p指针指向数值的数，作为当前位置新数，剩下数字升序排列
        :param nums:
        :param p:
        :return:
        """
        len_nums = len(nums)
        if len_nums <= 1:
            return

        # 目标数：仅大于p指针指向数值的数的索引和值
        target_num_index = None
        target_num_value = None

        # 指针此时指向的数
        p_value = nums[p]

        # 找到目标数
        for i in range(p, len_nums):
            if nums[i] > p_value:
                if target_num_index is None or nums[i] < target_num_value:
                    target_num_index = i
                    target_num_value = nums[i]

                    if target_num_value == p_value + 1:
                        # 已找到最接近的目标数数，可以提前结束查找
                        break

        # 目标数放置在p指针指向的位置
        nums[p], nums[target_num_index] = target_num_value, p_value

        # 剩下数字升序排列
        self.asc_sort(nums, start=p+1)


if __name__ == '__main__':
    n_list = [1, 3, 2]
    # n_list = [3, 2, 1]
    print(n_list)

    s = Solution()
    s.nextPermutation(n_list)
    # res = s.is_desc_order(n_list)
    print(n_list)
