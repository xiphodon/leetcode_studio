#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 10:26
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00025_k个一组反转链表.py
# @Software: PyCharm

"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

难度： 困难

执行用时 : 68 ms, 在Reverse Nodes in k-Group的Python3提交中击败了94.56% 的用户
内存消耗 : 13.8 MB, 在Reverse Nodes in k-Group的Python3提交中击败了100.00% 的用户
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head

        if k == 1:
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

                if i > k:
                    # 右指针移动次数＞k次，即链表长度≥k，反转链表
                    self.reverse_listnode(p_left, p_right, k)
                    return none_head.next
                else:
                    # 右指针移动次数≤k次，即链表长度小于k
                    return head

            else:
                # 右指针不为空
                if i < k + 1:
                    # 右指针先移动k步
                    p_right = p_right.next
                    i += 1
                    continue
                # 反转子链表
                self.reverse_listnode(p_left, p_right, k)

                temp_left = p_left
                temp_right = p_right
                for _ in range(k):
                    if temp_right is not None:
                        # temp右指针不为空，temp左右指针后移
                        temp_right = temp_right.next
                        temp_left = temp_left.next
                    else:
                        # 剩下的节点不足数量以反转，直接返回
                        return none_head.next
                # 左右指针接手temp左右指针移动
                p_right = temp_right
                p_left = temp_left
                # 更新移动步数
                i += k

    def reverse_listnode(self, p_left, p_right, k):
        """
        反转链表
        （反转左指针和右指针中间k个节点的链表）
        :param p_left: 左指针
        :param p_right: 右指针
        :param k: 反转节点的数量
        :return:
        """
        # 栈
        stack = list()
        # 将左指针和右指针中间k个节点依次入栈
        # 中间子链表指针
        temp_node = p_left.next
        while True:
            stack.append(temp_node)
            if len(stack) == k:
                # 若栈深 等于 反转节点数量，结束入栈
                break
            # 指针后移
            temp_node = temp_node.next

        # 创建返回链表头节点
        head = ListNode(None)
        # 返回链表指针
        p_node = head
        # 依次出栈，拼接链表
        while len(stack) >= 0:
            if len(stack) == 0:
                # 栈已空，新子链表尾接上右指针
                p_node.next = p_right
                break
            p_node.next = stack.pop()
            p_node = p_node.next
        # 新子链表头接在左指针后
        p_left.next = head.next

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
    # k = 3
    k = 4

    # node_list = range(1)
    # node_list = range(2)
    # node_list = range(3)
    node_list = range(4)
    # node_list = range(5)
    # node_list = range(6)
    # node_list = range(7)
    # node_list = range(8)
    # node_list = range(9)
    # node_list = range(10)

    s = Solution()
    node = s.create_singly_link_list(node_list)
    s.print_singly_link_list(node)
    res_node = s.reverseKGroup(node, k)
    s.print_singly_link_list(res_node)
