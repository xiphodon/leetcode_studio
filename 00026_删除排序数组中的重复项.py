#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 11:48
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00026_删除排序数组中的重复项.py
# @Software: PyCharm

"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

难度： 简单

执行用时 : 80 ms, 在Remove Duplicates from Sorted Array的Python3提交中击败了84.26% 的用户
内存消耗 : 14.7 MB, 在Remove Duplicates from Sorted Array的Python3提交中击败了81.66% 的用户
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 不同数的计数器
        count = 0
        # 上一个的数字
        last_num = None
        for i in range(len(nums)):
            if nums[i] == last_num:
                # 若当前位置数和上一个数字一样，重复出现，跳过
                continue
            # 若当前位置数和上一个数字不一样，未重复出现
            # 更新上一个数
            last_num = nums[i]
            # 将新数更新在列表中，第几次出现的新数就放在指定索引处
            nums[count] = last_num
            # 计数器自增
            count += 1
        return count


if __name__ == '__main__':
    lst = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    s = Solution()
    res = s.removeDuplicates(lst)
    print(res)
    print(lst[:res])
