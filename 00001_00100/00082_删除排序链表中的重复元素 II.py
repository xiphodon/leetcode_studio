#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/11 13:32
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00082_删除排序链表中的重复元素 II.py
# @Software: PyCharm

"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时：40 ms, 在所有 Python3 提交中击败了94.92%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了20.84%的用户
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
        # # 方法1：
        # # 新链表头指针
        # new_head = None
        # # 新链表当前指针
        # new_node = new_head
        # # 链表前指针
        # pre_node = head
        # if head:
        #     # 链表当前指针（后指针）
        #     node = head.next
        # else:
        #     return head
        #
        # # 上一个节点的值是否已重复
        # pre_node_value_repeat = False
        # while node:
        #     if pre_node.val == node.val:
        #         # 前后两指针数值一致，放弃收录，变更标记为重复
        #         pre_node_value_repeat = True
        #     else:
        #         # 前后两指针数值不一致
        #         if pre_node_value_repeat:
        #             # 前指针指向数值重复过，放弃收录，更新标记为不重复
        #             pre_node_value_repeat = False
        #         else:
        #             # 前指针指向数值不重复，收录
        #             # 生成新的节点
        #             temp_node = ListNode(val=pre_node.val)
        #             if new_head is None:
        #                 # 结果链表为空
        #                 # 更新结果链表头和当前节点指针
        #                 new_head = temp_node
        #                 new_node = temp_node
        #             else:
        #                 # 结果链表已存在
        #                 # 更新结果链表当前节点数据并指针后移
        #                 new_node.next = temp_node
        #                 new_node = new_node.next
        #     # 两指针后移
        #     pre_node = node
        #     node = node.next
        #
        # if pre_node_value_repeat is False:
        #     # 最后一个节点未重复，收录
        #     temp_node = ListNode(val=pre_node.val)
        #     if new_head:
        #         new_node.next = temp_node
        #     else:
        #         new_head = temp_node
        # return new_head

        # #方法2： 前中后三指针
        if head is None or head.next is None:
            return head

        # 创建伪链表头
        dummy_node = ListNode(val=-1, next=head)
        # 前指针
        pre_node = dummy_node
        # 当前指针
        current_node = head
        # 后指针
        next_node = head.next
        while next_node:
            while next_node is not None and current_node.val == next_node.val:
                # 将后指针移动到第一个与当前指针所指值不相等的位置
                next_node = next_node.next
            # 此时要么后指针指向None，要么当前指针指向与后指针指向数值不相等
            if current_node.next != next_node:
                # 若当前指针与后指针不相邻，则说明当前指针数值重复
                # 删除前后指针间所有节点（连接前后指针节点）
                pre_node.next = next_node
                if next_node is None:
                    # 后指针指向None，遍历结束，返回结果
                    return dummy_node.next
                else:
                    # 更新当前指针和后位置
                    current_node = next_node
                    next_node = next_node.next
            else:
                # 若当前指针与后指针相邻，则说明当前指针数值不重复
                if next_node is None:
                    # 后指针指向None，遍历结束，返回结果
                    return dummy_node.next
                else:
                    # 前中后三个指针向后移动一位
                    next_node = next_node.next
                    current_node = current_node.next
                    pre_node = pre_node.next
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
    nums = [1, 2, 3, 3, 4, 4, 5]
    # 生成链表
    head = create_node_list(nums)
    # 打印链表
    print_node_list(head)

    s = Solution()
    new_head = s.deleteDuplicates(head)
    print_node_list(new_head)


