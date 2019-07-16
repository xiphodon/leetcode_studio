#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 15:33
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00057_插入区间.py
# @Software: PyCharm

"""
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]

示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 困难

执行用时 :52 ms, 在所有 Python3 提交中击败了97.95%的用户
内存消耗 :14.4 MB, 在所有 Python3 提交中击败了100.00%的用户
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        # 新区间可能影响的元素范围 （影响范围包含start_index，end_index位置区间）
        start_index = 0
        end_index = len(intervals) - 1
        for i, interval in enumerate(intervals):
            if newInterval[0] > interval[1]:
                # 新区间最小值定落在 start_index 位置区间元素右边界的右侧（未影响到 start_index 区间）
                # 随着遍历进行，start_index 最终更新为新区间左侧的最后一个不收影响的区间位置
                start_index = i
            if newInterval[1] < interval[0]:
                # 新区间最大值定落在 end_index 位置区间元素左边界的左侧（未影响到 end_index 区间）
                # 找到新区间右侧第一个不受影响的位置即可结束循环
                end_index = i
                break
        if newInterval[0] > intervals[start_index][1]:
            # 更新 start_index 为受影响的 区间元素
            start_index += 1
        if newInterval[1] < intervals[end_index][0]:
            # 更新 end_index 为受影响的 区间元素
            end_index -= 1
        # 新区间与所有受影响的区间合并后的最小值
        min_val = min(newInterval[0], intervals[start_index][0]) if start_index < len(intervals) else newInterval[0]
        # 新区间与所有受影响的区间合并后的最大值
        max_val = max(newInterval[1], intervals[end_index][1]) if 0 <= end_index else newInterval[1]
        # 前部分未受影响区间 + 合并后的新区间 + 后部分未受影响的区间
        return intervals[:start_index] + [[min_val, max_val]] + intervals[end_index + 1:]


if __name__ == '__main__':
    intervals = [[1, 5]]
    newInterval = [6, 8]

    s = Solution()
    res = s.insert(intervals, newInterval)
    print(res)
