#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 16:43
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00019_删除链表的倒数第N个节点.py
# @Software: PyCharm

"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

难度： 中等

执行用时 : 56 ms, 在Remove Nth Node From End of List的Python3提交中击败了84.04% 的用户
内存消耗 : 12.9 MB, 在Remove Nth Node From End of List的Python3提交中击败了98.13% 的用户
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 双指针，一趟扫描
        assert n > 0, 'n must be a positive integer'

        # 左右两指针相差n步
        # 左指针（目的找到待删除节点的上一个节点）
        p_left = head
        # 右指针（目的找到链表结尾）
        p_right = head

        # 右指针移动次数
        i = 0
        while True:
            if p_right.next:
                # 有下一个节点

                if i < n:
                    # 右节点先移动n步
                    p_right = p_right.next
                else:
                    p_left = p_left.next
                    p_right = p_right.next
                i += 1
            else:
                # 右指针已到尾节点，此时左指针在待删除节点的上一个节点

                if i == n - 1:
                    # 待删除的是头节点，左指针与右指针相差n-1步，此时左指针未曾移动，指向头节点
                    # 找到新的头节点（完成删除操作）
                    head = p_left.next

                    # 防止内存泄露
                    p_left.next = None
                    del p_left
                elif i < n - 1:
                    # 右指针移动步数少于n-1步，已移动到尾节点，倒数第n个节点不存在
                    raise ValueError('The n reciprocal node does not exist')
                else:
                    # 删除节点
                    temp_node = p_left.next
                    p_left.next = temp_node.next

                    # 防止内存泄露
                    temp_node.next = None
                    del temp_node
                # 返回新链表的头节点
                return head

    def create_singly_link_list(self, lst) -> ListNode:
        """
        创建单向链表
        :param lst:
        :return:
        """
        head = None
        last_node = None
        for i in range(len(lst)):
            node = ListNode(lst[i])
            if i == 0:
                head = node
            else:
                last_node.next = node
            last_node = node
        return head

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
    lst = [1, 2, 3, 4, 5]

    s = Solution()
    head = s.create_singly_link_list(lst)
    s.print_singly_link_list(head)

    head = s.removeNthFromEnd(head, 2)
    s.print_singly_link_list(head)












