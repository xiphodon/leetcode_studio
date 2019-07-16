#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 11:54
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00017_电话号码的字母组合.py
# @Software: PyCharm


"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射与手机电话按键相同。注意 1 不对应任何字母。


示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

难度： 中等

执行用时 : 40 ms, 在Letter Combinations of a Phone Number的Python3提交中击败了99.20% 的用户
内存消耗 : 13 MB, 在Letter Combinations of a Phone Number的Python3提交中击败了95.48% 的用户
"""
from typing import List

from functools import reduce

mapping = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


class Solution:
    # 方法1 （递归）
    def letterCombinations(self, digits: str) -> List[str]:

        # 过程结果缓存
        temp_dict = dict()

        def get_permutation(lst: List[str], flag=0) -> List[List[str]]:
            """
            获取n个列表的元素全排列
            :param lst:
            :param flag: 递归层数标记，只有flag==1时，全排列为完整全排列
            :return:
            """
            # 递归层数标记
            flag += 1

            if len(lst) == 0:
                return [[]]

            # 是否存在缓存值，存在则直接返回
            if tuple(lst) in temp_dict:
                return temp_dict[tuple(lst)]

            temp_list = list()
            for char in lst[0]:
                # 收集当前第一个序列和后面所有序列的全排列
                temp_list += list(map(lambda x: [char] + x, get_permutation(lst[1:], flag=flag)))

            # 存为缓存
            temp_dict[tuple(lst)] = temp_list
            return temp_list

        if digits == '':
            return []
        res_list = get_permutation([mapping[digit] for digit in digits])
        # 外部列表中间结构为列表，是为了利用两个列表连接的效率高于两个字符串的连接，最后再把内部列表内元素合并为字符串
        return [''.join(i) for i in res_list]

    #####################################################################
    # 方法2

    # 数字字符串对应的字母串的列表
    mapping_str_list = None
    # 组合进位列表
    carry_list = None

    def letterCombinations_2(self, digits: str) -> List[str]:
        self.__class__.mapping_str_list = list()
        self.__class__.carry_list = list()

        if len(digits) == 0:
            return []

        # 结果列表
        res_list = list()
        # 数字字符串对应的字母串长度的列表
        mapping_str_len_list = list()
        for digit in digits:
            mapping_str = mapping[digit]
            self.__class__.mapping_str_list.append(mapping_str)
            mapping_str_len_list.append(len(mapping_str))

        # 计算各个字母串的向后组合数量（进位）
        for i in range(1, len(digits)):
            carry = reduce(lambda x, y: x * y, mapping_str_len_list[i:])
            self.__class__.carry_list.append(carry)
        self.__class__.carry_list.append(1)

        # 遍历每种组合的索引
        for i in range(mapping_str_len_list[0] * self.__class__.carry_list[0]):
            res_list.append(self.case_index_to_case(i))

        return res_list

    @classmethod
    def case_index_to_case(cls, index: int) -> str:
        """
        通过组合的索引，得到组合字符串
        :param index: 组合索引
        :return:
        """
        res_list = list()

        _index = index

        # 获取每位选取的字母
        for i in range(len(cls.carry_list)):
            # 该位进位
            carry = cls.carry_list[i]
            # 该位对应字母串
            string = cls.mapping_str_list[i]
            # 计算出字母串应选出的字母位置，并选出添加到结果集中
            res_list.append(string[_index // carry])

            # 索引取余，便于后面小位计算位置
            _index %= carry

        return ''.join(res_list)


if __name__ == '__main__':
    digit_str = '236468568657'

    s = Solution()
    res = s.letterCombinations(digit_str)
    print(res)
