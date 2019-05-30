#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 17:24
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00024_两两交换链表中的节点.py
# @Software: PyCharm

"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

难度： 中等

执行用时 : 40 ms, 在Swap Nodes in Pairs的Python3提交中击败了99.23% 的用户
内存消耗 : 12.8 MB, 在Swap Nodes in Pairs的Python3提交中击败了98.87% 的用户
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        # 添加一个新的头节点
        none_head = ListNode(None)
        none_head.next = head

        p_left = none_head
        p_right = none_head
        i = 0
        while True:
            if p_right is None:
                # 右指针为空

                # 上次移动两次，交换
                self.swap(p_left, p_right)
                return none_head.next

            else:
                # 右指针不为空
                if i < 3:
                    # 右指针先移动3步
                    p_right = p_right.next
                    i += 1
                    continue
                # 交换节点
                self.swap(p_left, p_right)

                if p_right.next is not None:
                    # 右指针后有下一个节点
                    p_right = p_right.next.next
                    p_left = p_left.next.next
                    i += 2
                else:
                    # 右指针已走到尾节点
                    return none_head.next

    def swap(self, p_left, p_right):
        """
        交换节点
        （左指针和右指针中间两个节点）
        :param p_left: 左指针
        :param p_right: 右指针
        :return:
        """
        # 取出中间两个节点
        node_1 = p_left.next
        node_2 = node_1.next

        # 交换中间两个节点
        p_left.next = node_2
        node_2.next = node_1
        node_1.next = p_right

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
    # node_list = [1]
    # node_list = [1, 2]
    # node_list = [1, 2, 3]
    # node_list = [1, 2, 3, 4]
    node_list = [1, 2, 3, 4, 5]

    s = Solution()
    node = s.create_singly_link_list(node_list)
    s.print_singly_link_list(node)
    res_node = s.swapPairs(node)
    s.print_singly_link_list(res_node)
