#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 9:42
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00045_跳跃游戏II.py
# @Software: PyCharm


"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 困难

执行用时 :80 ms, 在所有 Python3 提交中击败了58.02%的用户
内存消耗 :14.5 MB, 在所有 Python3 提交中击败了74.67%的用户
"""
from typing import List

cache_dict = dict()


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        贪心算法
        :param nums:
        :return:
        """

        len_nums = len(nums)
        if len_nums <= 1:
            return 0

        # 指针所指位置
        p = 0
        # 计步
        step = 0
        while p < len_nums:
            # 当前位置数字
            c_v = nums[p]

            temp_dict = dict()
            # 遍历当前数字可跳的所有步长
            for i in range(1, c_v + 1):
                # p + i 为本次步长跳至的索引位置
                if p + i < len_nums:
                    # nums[p + i] 为本次步长跳至的索引位置的数字
                    # p + i + nums[p + i] 为从 p + i 位置再跳跃 nums[p + i] 后到达的索引位置
                    # 数据缓存为 跳跃后位置（value）数字值能辐射到达最远的索引位置（key）
                    temp_dict[p + i + nums[p + i]] = p + i
                    if p + i == len_nums - 1:
                        # 索引到达边界，遍历结束，返回步数
                        return step + 1
                else:
                    # 索引越界，遍历结束，返回步数
                    return step + 1

            p = temp_dict[max(temp_dict.keys())]
            step += 1
        return step

    def jump2(self, nums: List[int]) -> int:
        """
        递归，遍历所有可能性
        :param nums:
        :return:
        """

        len_nums = len(nums)
        if len_nums == 0:
            return 0
        # 初始化最少步数
        min_step = len(nums) - 1

        def _jump(nums: List[int], step=0):
            """
            跳跃
            :param nums:
            :return:
            """
            nonlocal min_step

            if step >= min_step:
                # 当前步数已大于等于最小步数，早停
                return

            len_nums = len(nums)

            if len_nums == 0:
                # 数组已为空，该分支遍历结束，更新最少步数
                min_step = min(min_step, step)
                return

            # 当前数组第一个数字
            current_value = nums[0]

            if current_value == 0:
                # 第一个数字为0，则无法前进，早停
                return

            if current_value >= len_nums - 1:
                # 第一个数字大于等于当前长度，可一步跳至尾端
                min_step = min(min_step, step + 1)
                return
            else:
                # 第一个数字不大于当前长度，遍历所有可能跳跃的长度
                for i in range(current_value, 0, -1):
                    _jump(nums[i:], step=step + 1)

        _jump(nums, step=0)
        return min_step


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    # nums = [3, 2, 1]
    # nums = [1, 2, 0, 1]
    # nums = [8, 2, 4, 4, 4, 9, 5, 2, 5, 8, 8, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6, 0, 4, 8, 6, 0, 3, 2, 8, 7, 6, 5,
    #         1, 7, 0, 3, 4, 8, 3, 5, 9, 0, 4, 0, 1, 0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0,
    #         1, 8, 5, 6, 7, 5, 1, 9, 9, 3, 5, 0, 7, 5]

    s = Solution()
    res = s.jump(nums)
    print(res)
