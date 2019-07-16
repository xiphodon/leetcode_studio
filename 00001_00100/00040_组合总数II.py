#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 11:00
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00040_组合总数II.py
# @Software: PyCharm

"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :60 ms, 在所有Python3提交中击败了97.86%的用户
内存消耗 :13.1 MB, 在所有Python3提交中击败了83.33%的用户
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # 排序，有序列表方便后期处理
        candidates.sort()

        # 结果收集集
        res_list = list()

        def backtrack(item_list: list, start: int) -> None:
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

                # 记录当前位置上一次元素数字，若此次和上一次一样，跳过
                # [1, 1, 3] 4  => [1, 3]第一个1,[1, 3]第二个1
                last_v = None
                for i in range(start, len(candidates)):
                    v = candidates[i]

                    if last_v == v:
                        # 若此次和上一次一样，跳过
                        continue

                    if sum(item_list) + v <= target:
                        # 列表和仍未够target，当前数入栈
                        item_list.append(v)
                        # 递归调用
                        # 因为顺序列表，下一个数从这次起始位置开始即可（同一个元素只允许使用一次）
                        backtrack(item_list, i+1)
                        # 当前数的所有情况均已遍历过，弹出当前数，换下一个数继续遍历
                        item_list.pop()
                    else:
                        # 求和溢出，丢弃
                        return

                    # 更新上一次元素值
                    last_v = v

        backtrack(item_list=[], start=0)

        return res_list


if __name__ == '__main__':
    n_list = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    s = Solution()
    res = s.combinationSum2(n_list, target)
    print(res)
