#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 13:00
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00049_字母异位词分组.py
# @Software: PyCharm

"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

1、所有输入均为小写字母。
2、不考虑答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-anagrams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :140 ms, 在所有 Python3 提交中击败了94.05%的用户
内存消耗 :15.7 MB, 在所有 Python3 提交中击败了93.32%的用户
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # 同一组合的字母串缓存字典
        cache_dict = dict()

        for item_str in strs:
            # 字母串排序
            sorted_str = ''.join(sorted(item_str))
            if sorted_str not in cache_dict:
                cache_dict[sorted_str] = list()
            # 字母组合一致的字母串放在一起
            cache_dict[sorted_str].append(item_str)
        # 返回字典中收集的所有字母串列表
        return [item_list for item_list in cache_dict.values()]


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    s = Solution()
    res = s.groupAnagrams(strs)
    print(res)
