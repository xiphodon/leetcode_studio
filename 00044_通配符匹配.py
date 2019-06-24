#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 10:39
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00044_通配符匹配.py
# @Software: PyCharm

"""
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

1、s 可能为空，且只包含从 a-z 的小写字母。
2、p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输入: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wildcard-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 困难

执行用时 :2064 ms, 在所有 Python3 提交中击败了5.05%的用户
内存消耗 :37.2 MB, 在所有 Python3 提交中击败了5.33%的用户
"""

# 缓存字典
cache_dict = dict()


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def match(s: str, p: str):
            """
            匹配
            :return:
            """
            # 若之前已缓存，则直接返回
            if (s, p) in cache_dict:
                return cache_dict[(s, p)]

            len_s = len(s)
            len_p = len(p)

            if len_p - p.count('*') > len_s:
                # 若模式串中，除了'*'，剩余字符长度大于字符串长度，则模式串过长，一定匹配失败
                # 缓存匹配结果，返回False
                cache_dict[(s, p)] = False
                return False

            # 若模式串尾部不已*结尾，则直接对比尾部第一个*右侧的模式串与指定长度的字符串
            # 模式串p右侧第一个*的索引
            p_r_star_index = p.rfind('*')
            if p_r_star_index != -1 and p_r_star_index != len_p - 1:
                # 模式串p中存在*，且不是以*结尾
                # 模式串p第一个*右侧字符串
                p_r_star_str = p[p_r_star_index + 1:]
                # 对应长度的字符串s尾部字符串
                s_p_r_star_str = s[-len(p_r_star_str):]
                if match(s_p_r_star_str, p_r_star_str):
                    # 匹配成功，缓存匹配结果
                    cache_dict[(s_p_r_star_str, p_r_star_str)] = True
                else:
                    # 匹配失败，缓存匹配结果，返回False
                    cache_dict[(s_p_r_star_str, p_r_star_str)] = False
                    return False

            # s字符串指针
            s_p = 0
            # p模式字符串指针
            p_p = 0

            # 双指针循环
            while s_p < len_s and p_p < len_p:
                # 双指针当前指向变量
                s_c = s[s_p]
                p_c = p[p_p]

                if p_c == '?':
                    # 当前模式字符为'?'
                    # 匹配通过，双指针右移
                    s_p += 1
                    p_p += 1
                elif p_c == '*':
                    # 当前模式字符为'*'
                    # 剩余字符串长度
                    _len_s = len_s - s_p
                    # 剩余模式串
                    _p = p[p_p:]
                    # 剩余模式串长度
                    _len_p = len(_p)
                    # 剩余模式串中非*长度
                    _len_p_no_star = _len_p - _p.count('*')

                    # *可能匹配s字符串 [0, _len_s] 个字符
                    # 由于模式串字母必须匹配上才算成功，所以 * 无需匹配完剩余的s字符串
                    # 即 *可能匹配s字符串 [0, _len_s - _len_p_no_star]
                    # 回溯遍历
                    for _i in range(_len_s - _len_p_no_star + 1):
                        s_p += _i
                        p_p += 1
                        if match(s[s_p:], p[p_p:]):
                            # 若子串与子模式可匹配成功，缓存匹配结果，返回True
                            cache_dict[(s, p)] = True
                            return True
                        # 回溯到当前位置，进行下一轮遍历
                        s_p -= _i
                        p_p -= 1

                    # 回溯结束，均为匹配成功，缓存匹配结果，返回False
                    cache_dict[(s, p)] = False
                    return False

                else:
                    # 当前模式字符为英文字母
                    if s_c == p_c:
                        # 字符串字符与模式字符匹配，双指针右移
                        s_p += 1
                        p_p += 1
                    else:
                        # 字符串字符与模式字符不匹配，缓存匹配结果，返回False
                        cache_dict[(s, p)] = False
                        return False

            # while 循环结束，检查边界状态
            if s_p == len_s and p_p == len_p:
                # 字符串与模式串均已遍历完成，缓存匹配结果，返回True
                cache_dict[(s, p)] = True
                return True
            elif s_p == len_s and p[p_p:].replace('*', '') == '':
                # 字符串已遍历结束，模式串剩余字符全为'*'，缓存匹配结果，返回True
                cache_dict[(s, p)] = True
                return True
            else:
                # 字符串有剩余字符无法被空模式串匹配 或 模式串有剩余字符匹配字符空串失败，缓存匹配结果，返回True
                cache_dict[(s, p)] = False
                return False

        return match(s, p)


if __name__ == '__main__':
    s_str = 'acdcb'
    p_str = 'a*c?b'

    s = Solution()
    res = s.isMatch(s_str, p_str)
    print(res)
