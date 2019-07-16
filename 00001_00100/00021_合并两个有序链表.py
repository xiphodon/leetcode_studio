#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 10:22
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00021_合并两个有序链表.py
# @Software: PyCharm

"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

难度： 简单

执行用时 : 44 ms, 在Merge Two Sorted Lists的Python3提交中击败了99.85% 的用户
内存消耗 : 12.9 MB, 在Merge Two Sorted Lists的Python3提交中击败了97.43% 的用户
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 新链表头指针
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        # 生成头节点
        head = ListNode(None)
        # 新链表指针
        p_n = head
        while True:
            if l1 and l2:
                # 两链表当前节点都不为空

                # 对比两节点，值小者接入新链表
                if l1.val < l2.val:
                    p_n.next = l1
                    l1 = l1.next
                else:
                    p_n.next = l2
                    l2 = l2.next
                # 新链表指针后移
                p_n = p_n.next
            elif l1 is None and l2:
                # 链表1当前节点为空，链表2当前节点不为空
                # 将链表2当前节点后所有节点一同接入新链表，返回新链表
                p_n.next = l2
                return head.next
            elif l2 is None and l1:
                # 链表2当前节点为空，链表1当前节点不为空
                # 将链表1当前节点后所有节点一同接入新链表，返回新链表
                p_n.next = l1
                return head.next
            else:
                # 链表1/2均为空，返回新链表
                return head.next

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
    l1 = [1, 2, 5, 8]
    l2 = [3, 6, 7, 8]

    s = Solution()
    head_1 = s.create_singly_link_list(l1)
    head_2 = s.create_singly_link_list(l2)
    s.print_singly_link_list(head_1)
    s.print_singly_link_list(head_2)

    head = s.mergeTwoLists(head_1, head_2)
    s.print_singly_link_list(head)
