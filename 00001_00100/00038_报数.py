#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 15:47
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00038_报数.py
# @Software: PyCharm

"""
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

 

示例 1:

输入: 1
输出: "1"
示例 2:

输入: 4
输出: "1211"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-and-say
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度：简单

执行用时 :52 ms, 在所有Python3提交中击败了94.55%的用户
内存消耗 :13.2 MB, 在所有Python3提交中击败了44.04%的用户
"""


class Solution:
    def countAndSay(self, n: int) -> str:

        # 边界值
        if n == 1:
            return '1'

        def count_and_say(string='1', d=1):
            """
            报数
            :param string:
            :param d:
            :return:
            """
            # 递归深度
            d += 1

            temp_say_str = ''
            len_str = len(string)
            # 上一个字符
            last_str = None
            # 上一个字符出现数量
            last_str_times = 1

            for i in range(len_str):
                s = string[i]
                if last_str is None:
                    # 首次记录上一次字符
                    last_str = s
                else:
                    if s == last_str:
                        # 此次字符与上次一样，计数加一
                        last_str_times += 1
                    else:
                        # 此次字符与上次不一致，计数归一，拼接上一次读数
                        temp_say_str += f'{last_str_times}{last_str}'
                        last_str_times = 1
                        last_str = s

            # 拼接最后一次读数
            temp_say_str += f'{last_str_times}{last_str}'

            if d == n:
                # 到达要求层数
                return temp_say_str
            else:
                # 递归调用
                return count_and_say(temp_say_str, d)

        return count_and_say()


if __name__ == '__main__':
    n = 2

    s = Solution()
    res = s.countAndSay(n)
    print(res)
