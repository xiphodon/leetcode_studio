#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 16:29
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00039_组合总数.py
# @Software: PyCharm


"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :100 ms, 在所有Python3提交中击败了66.97%的用户
内存消耗 :13.1 MB, 在所有Python3提交中击败了88.04%的用户
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        回溯法
        :param candidates:
        :param target:
        :return:
        """

        # 排序，有序列表方便后期处理
        candidates.sort()

        # 结果收集集
        res_list = list()

        def backtrack(item_list: List, start: int):
            """
            回溯体
            :param item_list: 一次深度优先遍历的结果列表
            :param start: 因为是有序列表，深层的循环起始从start开始即可，防重复
            :return:
            """
            if sum(item_list) == target:
                # 满足条件的结果收集到总结果集中
                res_list.append(item_list.copy())

            elif sum(item_list) < target:
                # 列表的和暂未收集够target的值
                # 从上一层递归中的起始位置开始，因为列表顺序，防止结果集重复
                for i in range(start, len(candidates)):
                    item = candidates[i]
                    if item + sum(item_list) > target:
                        # 求和溢出，丢弃
                        break
                    else:
                        # 列表和仍未够target，当前数入栈
                        item_list.append(item)
                        # 递归调用
                        # 因为顺序列表，下一个数从这次起始位置开始即可（同一个数允许使用多次）
                        backtrack(item_list, i)
                        # 当前数的所有情况均已遍历过，弹出当前数，换下一个数继续遍历
                        item_list.pop()

        backtrack(item_list=[], start=0)
        return res_list


if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 8

    s = Solution()
    res = s.combinationSum(candidates, target)
    print(res)
