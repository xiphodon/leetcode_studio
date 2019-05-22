#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 11:28
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 470_用Rand7实现Rand10.py
# @Software: PyCharm

"""
已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。

不要使用系统的 Math.random() 方法。



示例 1:

输入: 1
输出: [7]
示例 2:

输入: 2
输出: [8,4]
示例 3:

输入: 3
输出: [8,1,10]


提示:

rand7 已定义。
传入参数: n 表示 rand10 的调用次数。


进阶:

rand7()调用次数的 期望值 是多少 ?
你能否尽量少调用 rand7() ?

难度： 中等

执行用时 : 508 ms, 在Implement Rand10() Using Rand7()的Python3提交中击败了65.81% 的用户
内存消耗 : 15.5 MB, 在Implement Rand10() Using Rand7()的Python3提交中击败了100.00% 的用户
"""

import random
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

# 计算两次rand7()和的个位
#
# 穷举如下：
#    a 	1	2	3	4	5	6	7
# b
# 1		2	3	4	5	6	7	8
# 2		3	4	5	6	7	8	9
# 3		4	5	6	7	8	9	0
# 4		5	6	7	8	9	0	1
# 5		6	7	8	9	0	1	2
# 6		7	8	9	0	1	2	3
# 7		8	9	0	1	2	3	4

# 去掉右上角的
# 6	 7	8
# 7	 8	9
# 8	 9	0      后
#
# 每个数字的出现次数为4次，0-9的概率相同


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            a = rand7()
            b = rand7()

            if (a > 4) and (b < 4):
                # 落在丢弃区，再次尝试
                continue
            else:
                return (a + b) % 10 + 1


def rand7():
    """
    随机出一个[1, 7]的数
    :return:
    """
    return random.randint(0, 7)


if __name__ == '__main__':
    s = Solution()
    res = s.rand10()
    print(res)
