#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 10:58
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00027_移除元素.py
# @Software: PyCharm

"""
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。
说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

难度： 简单

执行用时 : 40 ms, 在Remove Element的Python3提交中击败了99.50% 的用户
内存消耗 : 13 MB, 在Remove Element的Python3提交中击败了95.54% 的用户
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 目标数字指针
        p_target = 0

        len_list = len(nums)
        for p_list in range(len_list):
            if nums[p_list] != val:
                # 当前数字与目标数字不相等
                if p_target < p_list:
                    # 当前数字指针前出现过目标数字
                    # 当前数字放入目标数字位置
                    nums[p_target] = nums[p_list]
                p_target += 1
        return p_target


if __name__ == '__main__':
    lst = [0, 1, 2, 2, 3, 0, 4, 2]
    v = 2

    s = Solution()
    res = s.removeElement(lst, v)
    print(res)
