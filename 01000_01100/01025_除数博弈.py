#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 11:49
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 01025_除数博弈.py
# @Software: PyCharm

"""
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。



示例 1：

输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。
示例 2：

输入：3
输出：false
解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。


提示：

1 <= N <= 1000

难度： 简单

执行用时 : 40 ms, 在Divisor Game的Python3提交中击败了99.74% 的用户
内存消耗 : 12.9 MB, 在Divisor Game的Python3提交中击败了100.00% 的用户
"""

# 游戏开始，
#
# 若 N=1，该步操作者失败；
#
# 若 N=2，该步操作者只能选择x=1，新的N=N-x=1，后手N=1问题（失败），该步操作者获胜；
#
# 若 N=3，该步操作者只能选择x=1，新的N=N-x=2，后手N=2问题（获胜），该步操作者失败；
#
# 若 N=4，①该步操作者选择x=2，(最大公约数开始，降序向下取约数)， 新的N=2，后手N=2问题（获胜），该步操作者失败；
#        ②该步操作者选择x=1，新的N=3，后手N=3问题（失败），该步操作者获胜；
#        ※ 该步操作者只能选择②，获胜。
#
# 若 N=5，该步操作者只能选择x=1，新的N=4，后手N=4问题（获胜），该步操作者失败；
#
# 若 N=6，①该步操作者选择x=3，新的N=3，后手N=3问题（失败），该步操作者获胜；
#        ②该步操作者选择x=2，新的N=4，后手N=4问题（获胜），该步操作者失败；
#        ③该步操作者选择x=1，新的N=5，后手N=5问题（失败），该步操作者获胜；
#        ※ 该步操作者只能选择①③，获胜。
#
# 若 N=7，该步操作者只能选择x=1，新的N=6，后手N=6问题（获胜），该步操作者失败；
#
# 若 N=8，①该步操作者选择x=4，新的N=4，后手N=4问题（获胜），该步操作者失败；
#        ②该步操作者选择x=2，新的N=6，后手N=6问题（获胜），该步操作者失败；
#        ③该步操作者选择x=1，新的N=7，后手N=7问题（失败），该步操作者获胜；
#        ※ 该步操作者只能选择③，获胜。
# ......
#
# 奇数的因子只能是奇数，偶数的因子可以是奇数或偶数。
#
# 当N=偶数，若选择x为奇数，新的N=偶数N-奇数x，新的N为奇数，则下一手必为奇数问题
#         若选择x为偶数，新的N=偶数N-偶数x，新的N为偶数，则下一手必为偶数问题
# 当N=奇数，若N=1，当前这一手直接失败；
#         若N!=1，因子x只有奇数，新的N=奇数N-奇数x，新的N为偶数，则下一手必为偶数问题
#
# 可以看出，遇到偶数问题的操作者可以把握下一手为奇数问题还是偶数问题，如果可以使自己永远遇到偶数问题，
# 随着N慢慢变小，最终对手遇到N=1问题，对手失败。所以偶数问题操作者必选奇数因子，使对手必为奇数问题，
# 进而可以使自己每次必为偶数问题，并最终取得胜利。
#
# 综上所述，偶数问题操作者采用如上策略，必胜。
#
# ∴爱丽丝遇到偶数问题采用如上策略必胜


class Solution:
    def divisorGame(self, N: int) -> bool:
        # N为偶数，返回True
        if N > 0:
            return N & 1 == 0
        else:
            raise ValueError('N不是正整数')


if __name__ == '__main__':
    n = 100

    s = Solution()
    res = s.divisorGame(n)
    print(res)
