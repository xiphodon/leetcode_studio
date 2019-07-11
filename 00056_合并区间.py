#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 12:03
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00056_合并区间.py
# @Software: PyCharm

"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :96 ms, 在所有 Python3 提交中击败了28.69%的用户
内存消耗 :14 MB, 在所有 Python3 提交中击败了100.00%的用户
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res_set = set()
        # 遍历区间
        for interval in intervals:
            # 是否合并到结果集中
            is_update = False
            # 遍历结果集 与区间对比，合并
            for item_res in res_set.copy():
                if item_res[0] <= interval[0] <= item_res[1] or interval[0] <= item_res[0] <= interval[1]:
                    # 有交叉，合并到结果集，并删除合并前数据
                    res_set.remove(item_res)
                    res_set.add((min(item_res[0], interval[0]), max(item_res[1], interval[1])))
                    # 标记已更新
                    is_update = True
            if not is_update:
                # 若无更新，则新区间与老区间集无交叉
                res_set.add(tuple(interval))
        if len(intervals) == len(res_set):
            # 若本次合并流程无实际合并动作，直接返回结果集
            return list(res_set)
        else:
            # 继续瘦身合并结果集
            return self.merge(list(res_set))


if __name__ == '__main__':
    intervals = [[2, 3], [4, 6], [5, 7], [3, 4]]

    s = Solution()
    res = s.merge(intervals)
    print(res)
