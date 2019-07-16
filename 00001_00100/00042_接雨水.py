#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 12:16
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00042_接雨水.py
# @Software: PyCharm

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 困难

执行用时 :56 ms, 在所有Python3提交中击败了94.14%的用户
内存消耗 :13.3 MB, 在所有Python3提交中击败了98.46%的用户
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        接雨水

        双指针从外向内缩进，哪边指向边界小哪边向内缩进，
        如果当前左（右）指针指向数值小于刚刚经过的左（右）最大边界数值，则当前格子填充雨水
        （左右指针在扫过时，雨水必定要填满当前左右边界中间的区域，
        哪边指针移动，说明哪边指针指向的边界小，
        所以移动后指向的格子若小于刚刚的同侧边界【同侧边界为两侧边界的小值】的话，
        则填充雨水）
        :param height:
        :return:
        """
        if not height:
            return 0

        # 收集雨水计数
        tain_water = 0

        # 左右指针
        p_s = 0
        p_e = len(height) - 1

        # 双指针在扫动过程中，水池的已扫过的左右最大边界
        left_max = height[p_s]
        right_max = height[p_e]

        while p_s < p_e:
            if height[p_s] == height[p_e]:
                # 左右格子高度一致，检查更新左右最大边界，左指针移动
                left_max = max(left_max, height[p_s])
                right_max = max(right_max, height[p_e])
                p_s += 1
            elif height[p_s] < height[p_e]:
                # 左指针指向的格子高度小
                if left_max > height[p_s]:
                    # 左指针指向的格子小于左边界，填充相差高度雨水
                    tain_water += left_max - height[p_s]
                else:
                    # 左指针指向的格子大于等于左边界，更新左边界
                    left_max = height[p_s]
                # 左指针指向的格子高度小，左指针右移
                p_s += 1
            else:
                # 右指针指向的格子高度小
                if right_max > height[p_e]:
                    # 右指针指向的格子小于右边界，填充相差高度雨水
                    tain_water += right_max - height[p_e]
                else:
                    # 右指针指向的格子大于等于右边界，更新右边界
                    right_max = height[p_e]
                # 右指针指向的格子高度小，右指针左移
                p_e -= 1
        # 返回收集的总雨水量
        return tain_water


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    s = Solution()
    res = s.trap(height)
    print(res)
