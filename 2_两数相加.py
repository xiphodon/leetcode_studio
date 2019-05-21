#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 10:52
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 2_两数相加.py
# @Software: PyCharm

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

难度： 中等

执行用时 : 92 ms, 在Add Two Numbers的Python3提交中击败了99.42% 的用户
内存消耗 : 13.1 MB, 在Add Two Numbers的Python3提交中击败了93.85% 的用户
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 返回的目标链表
        l3 = None
        # 目标链表指针节点
        t0 = l3
        # 链表1指针节点
        t1 = l1
        # 链表2指针节点
        t2 = l2
        # 进位值
        c = 0
        while True:
            if t1 and t2:
                # 链表1、链表2 指针均指向有效位置

                # 计算当前数字和
                n = t1.val + t2.val + c
                # 计算完毕，进位清零
                c = 0

                if n > 9:
                    # 是否满足进位，满十进一
                    n -= 10
                    c = 1

                # 创建当前链表节点
                t3 = ListNode(n)

                if l3 is None:
                    # 链表为空，使t3为头节点
                    l3 = t3
                else:
                    # 链表不空，把t3串在目标链表的指针节点t0后
                    t0.next = t3
                # 目标指针后移
                t0 = t3

            elif t1 and (t2 is None):
                # 仅链表1指针指向有效位置
                if c == 0:
                    # 无进位，把链表1指针后面的链表接在目标指针节点后，并返回目标链表
                    t0.next = t1
                    return l3
                else:
                    # 有进位

                    # 计算新值，进位清零
                    n = t1.val + c
                    c = 0

                    if n > 9:
                        # 满十进一
                        n -= 10
                        c = 1

                    # 创造新节点
                    t3 = ListNode(n)
                    # t3串在目标链表的指针节点t0后
                    t0.next = t3
                    # 指针后移
                    t0 = t3

            elif (t1 is None) and t2:
                # 仅链表2指针指向有效位置，同上
                if c == 0:
                    t0.next = t2
                    return l3
                else:
                    n = t2.val + c
                    c = 0

                    if n > 9:
                        n -= 10
                        c = 1

                    t3 = ListNode(n)
                    t0.next = t3
                    t0 = t3
            elif (t1 is None) and (t2 is None) and c == 1:
                # 链表1、链表2 指针均指向无效位置（遍历结束），但仍有新进位

                # 创建新节点，进位清零，连接在目标指针节点后，指针后移
                t3 = ListNode(c)
                c = 0
                t0.next = t3
                t0 = t3
            else:
                # 链表1、链表2 指针均指向无效位置（遍历结束），并无进位
                return l3

            # 若链表1、链表2 指针节点有效，指针后移
            if t1:
                t1 = t1.next
            else:
                t1 = None

            if t2:
                t2 = t2.next
            else:
                t2 = None


def list_to_listnode(lst: List) -> ListNode:
    """
    创造ListNode（list 转 ListNode）
    :param lst:
    :return:
    """
    listnode = None
    p = None
    for i in lst:
        temp = ListNode(i)
        if p:
            p.next = temp
        else:
            listnode = temp
        p = temp
    return listnode


def listnode_to_list(ln: ListNode) -> list:
    """
    ListNode 装 list
    :param ln:
    :return:
    """
    _list = list()
    while True:
        if ln:
            _list.append(ln.val)
            ln = ln.next
        else:
            break
    return _list


if __name__ == '__main__':
    lst1 = [2, 4, 5, 2, 3, 5]
    lst2 = [5, 6, 4]

    ln1 = list_to_listnode(lst1)
    ln2 = list_to_listnode(lst2)

    s = Solution()
    ln3 = s.addTwoNumbers(ln1, ln2)
    lst3 = listnode_to_list(ln3)

    print(lst3)
