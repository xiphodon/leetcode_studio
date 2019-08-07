#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 16:07
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00061_旋转链表.py
# @Software: PyCharm

"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :52 ms, 在所有 Python3 提交中击败了88.64%的用户
内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.40%的用户
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        # 获取链表长度
        link_list_len = 0
        node = head
        while node:
            link_list_len += 1
            node = node.next

        if link_list_len <= 1:
            # 链表长度小于等于1，则直接返回原链表，无需移动
            return head

        # 移动步数可能大于链表长度，则会移动多个周期
        new_k = k % link_list_len

        if new_k == 0:
            # 链表移动步数为0，则无需移动
            return head

        def rotate_right_k_step(temp_head: ListNode, new_k: int) -> ListNode:
            """
            向右移动一步链表（仅支持链表长度大于1）
            :param temp_head: 链表
            :param new_k: 移动数量
            :return:
            """
            if new_k == 0:
                return temp_head

            # 快慢指针
            temp_node_fast = temp_head
            temp_node_slow = temp_head

            # 快指针先移动 new_k 步
            for _ in range(new_k):
                temp_node_fast = temp_node_fast.next

            while True:
                if temp_node_fast.next is None:
                    # 此时快指针已到尾节点，将慢指针后链表摘下，连在头指针前
                    new_head = temp_node_slow.next
                    temp_node_slow.next = None
                    temp_node_fast.next = temp_head
                    return new_head
                else:
                    temp_node_fast = temp_node_fast.next
                    temp_node_slow = temp_node_slow.next

        return rotate_right_k_step(head, new_k)

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
        while node:
            print_list.append(str(node.val))
            if node.next:
                print_list.append('->')
                node = node.next
            else:
                break
        print(''.join(print_list))


if __name__ == '__main__':
    link_list = [1, 2]
    k = 2

    s = Solution()
    link_list = s.create_singly_link_list(link_list)
    s.print_singly_link_list(link_list)
    res = s.rotateRight(link_list, k)
    s.print_singly_link_list(res)
