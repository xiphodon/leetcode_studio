#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/11 15:21
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00083_删除排序链表中的重复元素.py
# @Software: PyCharm

"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 简单

执行用时：44 ms, 在所有 Python3 提交中击败了84.38%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了56.69%的用户
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        前后双指针
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return head

        # 创建伪节点
        dummy_node = ListNode(val=-1, next=head)
        # 当前指针
        current_node = head
        # 后指针
        next_node = head.next

        while next_node:
            if current_node.val != next_node.val:
                # 两指针指向数值不一致，双指针后移
                next_node = next_node.next
                current_node = current_node.next
            else:
                # 两指针指向数值一致，删除后指针指向节点，后指针后移
                current_node.next = next_node.next
                next_node = next_node.next
        return dummy_node.next


def create_node_list(nums_list: list) -> ListNode:
    """
    创建节点列表
    :param nums_list:
    :return:
    """
    head = ListNode(val=-1)
    node = head
    for i in nums_list:
        temp_node = ListNode(val=i)
        node.next = temp_node
        node = node.next
    return head.next


def print_node_list(node_list: ListNode) -> None:
    """
    打印节点列表
    :param node_list:
    :return:
    """
    print_list = list()
    p_node = node_list
    while p_node:
        print_list.append(str(p_node.val))
        if p_node.next:
            print_list.append('->')
            p_node = p_node.next
        else:
            break
    print(' '.join(print_list))


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 4, 4, 5, 5]
    # 生成链表
    head = create_node_list(nums)
    # 打印链表
    print_node_list(head)

    s = Solution()
    new_head = s.deleteDuplicates(head)
    print_node_list(new_head)
