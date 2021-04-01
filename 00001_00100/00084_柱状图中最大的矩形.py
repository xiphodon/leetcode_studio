#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/16 17:30
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00084_柱状图中最大的矩形.py
# @Software: PyCharm

"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。


示例:

输入: [2,1,5,6,2,3]
输出: 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 困难

执行用时：256 ms, 在所有 Python3 提交中击败了74.60%的用户
内存消耗：25.4 MB, 在所有 Python3 提交中击败了28.50%的用户
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        def range_area(height_list: List[int]):
            """
            区间内面积
            （计算高度列表以首末数字为边界的最大矩形面积，即高度为高度列表中数值最小的数字）
            二分法
            :param height_list:
            :return:
            """
            nonlocal max_area
            if len(height_list) == 0:
                return

            # 找出当前高度列表中最大值和最小值的索引与数值
            min_height_index = 0
            min_height_value = height_list[0]
            max_height_index = 0
            max_height_value = height_list[0]

            for i in range(1, len(height_list)):
                if height_list[i] < min_height_value:
                    min_height_value = height_list[i]
                    min_height_index = i
                if height_list[i] > max_height_value:
                    max_height_value = height_list[i]
                    max_height_index = i

            # 计算出当前高度列表的矩形面积，以首末数为宽，以最小值为高的矩形面积
            current_area = len(height_list) * min_height_value
            if current_area > max_area:
                max_area = current_area

            if min_height_value == max_height_value:
                # 若最大值与最小值一样，可以早停
                return

            # 二分法计算，从最小值处左右分为两个部分（舍弃最小值数），若高度列表中有大面积区域，
            # 高度一定会大于当前最小值高度，继续筛选下去

            if min_height_index * max_height_value > max_area:
                # 若左侧区域的宽度乘以最大高度值都不大于现有最大面积值，则可早停，反之继续筛选
                range_area(height_list[:min_height_index])

            if (len(height_list) - min_height_index - 1) * max_height_value > max_area:
                # 若右侧区域的宽度乘以最大高度值都不大于现有最大面积值，则可早停，反之继续筛选
                range_area(height_list[min_height_index + 1:])

        range_area(heights)
        return max_area

    def largestRectangleArea2(self, heights: List[int]) -> int:
        """
        单调栈方法
        :param heights:
        :return:
        """
        # 增加左右哨兵(左右哨兵值小于任意高度)
        heights = [-1] + heights + [-1]
        size = len(heights)
        max_area = 0
        # 单调栈
        stack = list()
        # 向栈内压入左哨兵索引
        stack.append(0)

        for i in range(1, size):
            # i 为当前遍历柱子的索引位置
            while True:
                if heights[i] >= heights[stack[-1]]:
                    # 若当前柱子的高度大于或等于栈内记录的最后一个柱子高度，则当前柱子的左极限一定在栈中，压入栈，待找出右极限
                    stack.append(i)
                    break
                if heights[i] < heights[stack[-1]]:
                    # 当前柱子高度小于栈内记录的最后一个柱子的高度，即栈内所记录的最后一个柱子的右极限也已找到，弹出栈，计算面积
                    height = heights[stack.pop()]
                    # 新栈尾元素则为当前柱子的左极限柱子索引
                    # 【注：若栈内有等高柱子的情况，说明两柱子是可以相互左右扩展到的，即面积会相等，
                    # 后入栈的实际左边界将会更大，则当前宽度计算会小于实际值，不过，不影响最终结果】
                    width = i - stack[-1] - 1
                    max_area = max(max_area, height * width)
        return max_area


if __name__ == '__main__':
    height_list = [2, 1, 5, 6, 2, 3]
    # height_list = [0, 0]
    s = Solution()
    print(s.largestRectangleArea2(height_list))
