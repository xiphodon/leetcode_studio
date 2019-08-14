#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 14:18
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00072_编辑距离.py
# @Software: PyCharm


"""
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 困难

执行用时 :232 ms, 在所有 Python3 提交中击败了71.96%的用户
内存消耗 :17.5 MB, 在所有 Python3 提交中击败了5.38%的用户
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        动态规划
        :param word1:
        :param word2:
        :return:
        """
        # dp[i][j] 表示 word1字符串从头到第i位置字符串 转换成 word2字符串从头到j位置字符串 需要的最小步数
        # 即：word1[0: i + 1] 转换成 word2[0: j + 1] 需要的最小步数
        # i,j 表示为第i个字符，第j个字符

        word1_len = len(word1)
        word2_len = len(word2)

        # 各种状态值，增加一行一列，第一行为word1空串情况，第一列为word2空串情况
        dp = [[0] * (word2_len + 1) for _ in range(word1_len + 1)]

        for i in range(word1_len + 1):
            for j in range(word2_len + 1):
                if i != 0 and j == 0:
                    # j指向word2为空串，表示word1删除操作（上一步步数 + 1）
                    dp[i][j] = dp[i - 1][j] + 1
                    continue
                if i == 0 and j != 0:
                    # i指向word1为空串，表示word2插入操作（上一步步数 + 1）
                    dp[i][j] = dp[i][j - 1] + 1
                    continue

                if i != 0 and j != 0:
                    # i、j 指向均不为空串
                    # i、j 均从空串开始自增，i - 1, j - 1 才为 word1、word2对应索引
                    if word1[i - 1] == word2[j - 1]:
                        # i、j当前指向的最后一位相同，相当于当前步不需要操作，等于i - 1, j - 1状态步数
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        # i、j指向的最后一位不同
                        # dp[i - 1][j - 1] 表示修改操作，变更word1最后一位字符为word2最后一位字符
                        # dp[i - 1][j] 表示删除操作，删除word1当前最后一位字符
                        # dp[i][j - 1] 表示插入操作，插入word1尾部为word2最后一位字符
                        # 在上一个可能状态的最小步数情况 + 当前步操作步数1，即为当前状态最小步数
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]


if __name__ == '__main__':
    w_1 = 'a'
    w_2 = 'ab'

    s = Solution()
    res = s.minDistance(w_1, w_2)
    print(res)
