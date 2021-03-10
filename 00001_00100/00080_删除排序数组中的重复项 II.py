#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 14:23
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00080_删除排序数组中的重复项 II.py
# @Software: PyCharm


"""
给定一个增序排列数组 nums ，你需要在 原地 删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

说明：

为什么返回数值是整数，但输出的答案是数组呢？

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下：

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
 

示例 1：

输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 你不需要考虑数组中超出新长度后面的元素。
示例 2：

输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。 你不需要考虑数组中超出新长度后面的元素。
 

提示：

0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums 按递增顺序排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时：36 ms, 在所有 Python3 提交中击败了91.86%的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了84.64%的用户
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        覆盖法
        :param nums:
        :return:
        """
        # 结果列表索引（结果列表与原始列表头指针重叠，即原地修改）
        res_nums_index = 0
        for num in nums:
            if res_nums_index < 2 or num != nums[res_nums_index - 2]:
                # 结果列表长度不到2（即不可能重复，直接覆盖并更新）
                # 或
                # 当前遍历数字不与结果列表倒数第二个数字相等（即重复次数不超过2，直接覆盖并更新）
                nums[res_nums_index] = num
                res_nums_index += 1
        return res_nums_index


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    s = Solution()
    print(nums)
    print(s.removeDuplicates(nums))
    print(nums)
