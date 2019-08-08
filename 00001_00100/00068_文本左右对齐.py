#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 15:32
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00068_文本左右对齐.py
# @Software: PyCharm

"""
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/text-justification
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度：困难

执行用时 :52 ms, 在所有 Python3 提交中击败了55.19%的用户
内存消耗 :13.8 MB, 在所有 Python3 提交中击败了6.82%的用户
"""
from pprint import pprint
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        两端对齐
        :param words:
        :param maxWidth:
        :return:
        """

        def split_blank(blank_num: int, split_num: int) -> List[int]:
            """
            分离空格
            :param blank_num: 空格数量
            :param split_num: 分离数量
            :return:
            """
            # 平均每部分空格数（向下取整）
            avg_blank = blank_num // split_num
            # 多余出的空格
            remain_blank = blank_num - avg_blank * split_num
            # 生成返回的分离后的空格列表
            split_blank_num_list = [avg_blank] * split_num

            # 将多余空格分配在空格列表中
            for remain_blank_index in range(remain_blank):
                split_blank_num_list[remain_blank_index] += 1
            return split_blank_num_list

        def full_justify_one_line(words_list: list, is_tail=False) -> str:
            """
            一行两端对齐
            :param words_list:
            :param is_tail: 是否是尾行
            :return:
            """
            words_list_len = len(words_list)
            if not is_tail:
                # 不为尾行
                if words_list_len == 1:
                    # 当前行仅一个单词
                    the_only_word = words_list[0]
                    return the_only_word + ' ' * (maxWidth - len(the_only_word))
                else:
                    # 当前行多个单词
                    # 总单词长度
                    all_word_size = sum([len(w) for w in words_list])
                    # 需要的空格数
                    blank_num = maxWidth - all_word_size
                    # 拆分好的空格数
                    split_blank_num_list = split_blank(blank_num, words_list_len - 1)
                    # 生成当前行
                    line_str_list = list()
                    for b_i in range(words_list_len - 1):
                        line_str_list.append(words_list[b_i])
                        line_str_list.append(' ' * split_blank_num_list[b_i])
                    line_str_list.append(words_list[-1])
                    return ''.join(line_str_list)
            else:
                # 为尾行
                tail_line_str = ' '.join(words_list)
                return tail_line_str + ' ' * (maxWidth - len(tail_line_str))

        # 主逻辑：
        # 结果集
        res_list = list()
        # 单词数量
        words_len = len(words)

        # 需要填充的每行单词列表
        temp_words = list()
        # 需要填充的每行单词列表所需要的最短长度
        temp_min_size = 0
        for i in range(words_len):
            # 取出当前单词
            word = words[i]
            # 添加当前单词后单词列表所需的最短长度
            if temp_min_size == 0:
                # 当前需要填充的每行单词列表为空，预先计算添加当前单词后长度，为当前单词长度
                add_word_min_size = len(word)
            else:
                # 当前需要填充的每行单词列表为空，预先计算添加当前单词后长度，为当前长度 + 空格 + 当前单词长度
                add_word_min_size = temp_min_size + 1 + len(word)

            if add_word_min_size <= maxWidth:
                # 若添加当前单词后最短长度不超过规定的最大长度
                # 更新当前单词到每行单词列表
                temp_words.append(word)
                # 更新每行单词列表所需要的最短长度
                temp_min_size = add_word_min_size
                continue
            else:
                # 两端对齐单行数据
                one_line_str = full_justify_one_line(temp_words)
                # 收集结果
                res_list.append(one_line_str)
                # 临时单词列表清空，增加当前单词
                temp_words = [word]
                temp_min_size = len(word)

        if len(temp_words) > 0:
            # 尾行
            last_line_str = full_justify_one_line(temp_words, is_tail=True)
            res_list.append(last_line_str)
        return res_list


if __name__ == '__main__':
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    max_size = 20

    s = Solution()
    res = s.fullJustify(words, max_size)
    pprint(res)
