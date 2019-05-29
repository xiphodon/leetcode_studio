#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 16:41
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00023_合并K个排序列表.py
# @Software: PyCharm

"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

难度： 困难

执行用时 : 88 ms, 在Merge k Sorted Lists的Python3提交中击败了96.85% 的用户
内存消耗 : 17.1 MB, 在Merge k Sorted Lists的Python3提交中击败了47.69% 的用户
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lst = list()
        for item_node in lists:
            # 把每个链表值添加到列表中
            while True:
                if item_node:
                    lst.append(item_node.val)
                    item_node = item_node.next
                else:
                    break
        # 列表排序
        lst.sort()
        # 列表转成链表并返回
        return self.create_singly_link_list(lst)

    def create_singly_link_list(self, lst) -> ListNode:
        """
        创建单向链表
        :param lst:
        :return:
        """
        head = ListNode(None)
        p = head
        for i in range(len(lst)):
            node = ListNode(lst[i])
            p.next = node
            p = node
        return head.next

    def print_singly_link_list(self, head):
        """
        打印单向链表
        :param head:
        :return:
        """
        print_list = list()
        node = head
        while True:
            print_list.append(str(node.val))
            if node.next:
                print_list.append('->')
                node = node.next
            else:
                break
        print(''.join(print_list))


if __name__ == '__main__':
    l = [
        [1, 4, 5],
        [1, 3, 4],
        [2, 6]
    ]

    s = Solution()
    res = s.mergeKLists([s.create_singly_link_list(i) for i in l])
    s.print_singly_link_list(res)
