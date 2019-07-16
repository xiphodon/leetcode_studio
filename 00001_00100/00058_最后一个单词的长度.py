#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 9:34
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00058_最后一个单词的长度.py
# @Software: PyCharm

"""
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/length-of-last-word
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 简单

执行用时 :40 ms, 在所有 Python3 提交中击败了96.57%的用户
内存消耗 :13.2 MB, 在所有 Python3 提交中击败了70.86%的用户
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_len = len(s)
        # 字符串索引
        # 右索引，右侧第一个不为空格的索引
        right_index = None
        # 左索引，右侧右索引左侧的第一个空格的索引
        left_index = None
        for i in range(s_len - 1, -1, -1):
            if right_index is None:
                # 右索引暂不存在
                if s[i] == ' ':
                    # 跳过末尾空格
                    continue
                else:
                    # 更新右索引值
                    right_index = i
            else:
                # 右索引已存在
                if s[i] == ' ':
                    # 更新左索引 并 退出循环
                    left_index = i
                    break
                else:
                    # 最后一个单词还未遍历到左边界
                    continue
        if right_index is None:
            # 右索引不存在，则说明最后一个单词不存在
            return 0
        else:
            # 右索引存在
            if left_index is None:
                # 左索引不存在，说明最后一个单词的左边界为字符串起点
                return right_index + 1
            else:
                # 左右索引均存在，直接算出最后一个单词长度
                return right_index - left_index


if __name__ == '__main__':
    string = 'Hello World  '
    s = Solution()
    res = s.lengthOfLastWord(string)
    print(res)
