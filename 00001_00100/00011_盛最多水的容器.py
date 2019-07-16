#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 17:28
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00011_盛最多水的容器.py
# @Software: PyCharm

"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49

难度： 中等

执行用时 : 76 ms, 在Container With Most Water的Python3提交中击败了88.08% 的用户
内存消耗 : 13.9 MB, 在Container With Most Water的Python3提交中击败了99.38% 的用户
"""
from typing import List


class Solution:
    def maxArea_1(self, height: List[int]) -> int:
        # 优化的循环遍历法，优于暴力破解法，劣于双指针法

        # 最大容积记录
        max_area = 0
        # 最大左边界记录
        max_left = -1

        for i in range(len(height)):
            # height[i] 为容器左边界

            # 当前左边界情况下，最大右边界记录
            max_right = -1

            if height[i] <= max_left:
                # 移动过程中左边界小于出现过的最大左边界
                continue
            else:
                # 记录当前左边界为最大左边界
                max_left = height[i]

            for j in range(len(height) - 1, i, -1):
                # height[j] 为容器右边界
                if height[j] <= max_right:
                    # 移动过程中右边界小于出现过的最大右边界
                    continue
                else:
                    # 记录当前右边界为最大右边界
                    max_right = height[j]

                # 计算当前容积
                this_area = (j - i) * min(height[i], height[j])
                # 更新最大容积记录
                max_area = max(max_area, this_area)

                if height[i] <= height[j]:
                    # 若当前右边界已大于左边界，开始下一个左边界循环
                    break

        return max_area

    def maxArea_2(self, height: List[int]) -> int:
        # 双指针法

        # 起始指针
        p_s = 0
        # 末尾指针
        p_e = len(height) - 1

        max_area = 0

        while p_s < p_e:
            # 计算容积
            max_area = max(max_area, min(height[p_s], height[p_e]) * (p_e - p_s))
            # 左右边界哪个小，哪里向中间移动
            if height[p_s] <= height[p_e]:
                p_s += 1
            else:
                p_e -= 1

        return max_area


if __name__ == '__main__':
    # lst = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    lst = [1, 1]

    s = Solution()
    res = s.maxArea_2(lst)
    print(res)


