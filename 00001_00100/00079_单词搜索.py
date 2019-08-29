#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 9:39
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00079_单词搜索.py
# @Software: PyCharm


"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :504 ms, 在所有 Python3 提交中击败了29.10%的用户
内存消耗 :15.6 MB, 在所有 Python3 提交中击败了11.25%的用户
"""
from typing import List, Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        不存储路径
        :param board:
        :param word:
        :return:
        """

        # 棋牌行列
        rows = len(board)
        cols = len(board[0])

        # 索引位置偏移，（行索引偏移，列索引偏移）
        site_offest_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def recall(last_step_r: int,
                   last_step_c: int,
                   target_sub_str: str,
                   selected_r_c_list: List[Tuple[int, int]],
                   last_step_arrow: Tuple[int, int]):
            """
            回溯体
            :param last_step_r: 上一步行索引
            :param last_step_c: 上一步列索引
            :param target_sub_str: 需要搜索的目标子串
            :param selected_r_c_list: 已收集索引
            :param last_step_arrow: 上一步到这一步所走的方向
            :return:
            """

            if target_sub_str == '':
                return True

            if len(selected_r_c_list) == 0:
                # 分支刚开始，记录起点
                selected_r_c_list.append((last_step_r, last_step_c))

            # 下一个要匹配的字符
            target_char = target_sub_str[0]

            # 上下左右四个方向尝试
            for delta_site in site_offest_list:

                # 上一步到这一步的方向的反向
                last_step_arrow_mirror = (- last_step_arrow[0], - last_step_arrow[1])

                if delta_site == last_step_arrow_mirror:
                    # 回到上一步的位置，跳过
                    continue

                # 行列坐标偏移量
                delta_r, delta_c = delta_site

                # 下一步新位置
                next_step = (last_step_r + delta_r, last_step_c + delta_c)

                if next_step[0] < 0 or next_step[0] > rows - 1 or next_step[1] < 0 or next_step[1] > cols - 1:
                    # 新位置坐标越界
                    continue

                if board[next_step[0]][next_step[1]] == target_char:
                    # 搜索到匹配的字符
                    if next_step not in selected_r_c_list:
                        # 新位置未被收集
                        selected_r_c_list.append(next_step)
                        _res = recall(next_step[0], next_step[1], target_sub_str[1:], selected_r_c_list, delta_site)
                        if _res:
                            return True
                        selected_r_c_list.pop()

        # 找起点
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    # 找到起点，开始搜索
                    res = recall(r, c, word[1:], [], (0, 0))
                    if res:
                        return True

        return False

    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     """
    #     （存储路径）
    #     :param board:
    #     :param word:
    #     :return:
    #     """
    #
    #     # 结果集
    #     all_result_list = list()
    #
    #     # 棋牌行列
    #     rows = len(board)
    #     cols = len(board[0])
    #
    #     def recall(last_step_r: int, last_step_c: int, target_sub_str: str, selected_r_c_list: List[Tuple[int, int]]):
    #         """
    #         回溯体
    #         :param last_step_r: 上一步行索引
    #         :param last_step_c: 上一步列索引
    #         :param target_sub_str: 需要搜索的目标子串
    #         :param selected_r_c_list: 已收集索引
    #         :return:
    #         """
    #
    #         if target_sub_str == '':
    #             all_result_list.append(selected_r_c_list[:])
    #             return
    #
    #         if len(selected_r_c_list) == 0:
    #             # 分支刚开始，记录起点
    #             selected_r_c_list.append((last_step_r, last_step_c))
    #
    #         # 下一个要匹配的字符
    #         target_char = target_sub_str[0]
    #
    #         # 索引位置偏移，（行索引偏移，列索引偏移）
    #         site_offest_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #         for delta_r, delta_c in site_offest_list:
    #             # 下一步新位置
    #             next_step = (last_step_r + delta_r, last_step_c + delta_c)
    #
    #             if next_step[0] < 0 or next_step[0] > rows - 1 or next_step[1] < 0 or next_step[1] > cols - 1:
    #                 # 新位置坐标越界
    #                 continue
    #
    #             if board[next_step[0]][next_step[1]] == target_char:
    #                 # 搜索到匹配的字符
    #                 if next_step not in selected_r_c_list:
    #                     # 新位置未被收集
    #                     selected_r_c_list.append(next_step)
    #                     recall(next_step[0], next_step[1], target_sub_str[1:], selected_r_c_list)
    #                     selected_r_c_list.pop()
    #
    #     # 找起点
    #     for r in range(rows):
    #         for c in range(cols):
    #             if board[r][c] == word[0]:
    #                 # 找到起点，开始搜索
    #                 recall(r, c, word[1:], [])
    #
    #     print(all_result_list)
    #
    #     if len(all_result_list) > 0:
    #         return True
    #     else:
    #         return False


if __name__ == '__main__':
    board = [
                ['A', 'B', 'C', 'E'],
                ['S', 'F', 'E', 'S'],
                ['A', 'D', 'E', 'E']
            ]

    word = "ABCESEEEFS"

    s = Solution()
    result = s.exist(board, word)
    print(result)
