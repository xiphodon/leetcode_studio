#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 11:22
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00055_跳跃游戏.py
# @Software: PyCharm

"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :84 ms, 在所有 Python3 提交中击败了30.45%的用户
内存消耗 :14.4 MB, 在所有 Python3 提交中击败了92.28%的用户
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        if len_nums == 0:
            return False
        i = 0
        while i < len_nums - 1:
            # i 为数组索引
            current_num = nums[i]
            jump_two_point_one_time_index_dict = dict()
            for j in range(1, current_num + 1):
                # j 为跳跃步长
                # 跳跃一次后索引
                jump_one_time_index = i + j
                if jump_one_time_index >= len_nums - 1:
                    return True
                # 跳跃一次后的值
                jump_one_time_num = nums[jump_one_time_index]
                # 跳跃两次后的索引
                jump_two_time_index = jump_one_time_num + jump_one_time_index
                if jump_two_time_index >= len_nums - 1:
                    return True
                # 跳跃两次的索引：跳跃一次的索引
                jump_two_point_one_time_index_dict[jump_two_time_index] = jump_one_time_index
            if jump_two_point_one_time_index_dict:
                # 跳跃两次最大的索引所对应的跳跃一次的索引赋值给i
                i = jump_two_point_one_time_index_dict[max(jump_two_point_one_time_index_dict)]
            else:
                return False
        return True


if __name__ == '__main__':
    lst = [1, 1, 2, 2, 0, 1, 1]
    s = Solution()
    res = s.canJump(lst)
    print(res)
