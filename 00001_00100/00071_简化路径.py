#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 11:23
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : 00071_简化路径.py
# @Software: PyCharm

"""
以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。

在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径

请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。

 

示例 1：

输入："/home/"
输出："/home"
解释：注意，最后一个目录名后面没有斜杠。
示例 2：

输入："/../"
输出："/"
解释：从根目录向上一级是不可行的，因为根是你可以到达的最高级。
示例 3：

输入："/home//foo/"
输出："/home/foo"
解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。
示例 4：

输入："/a/./b/../../c/"
输出："/c"
示例 5：

输入："/a/../../b/../c//.//"
输出："/c"
示例 6：

输入："/a//b////c/d//././/.."
输出："/a/b/c"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/simplify-path
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

难度： 中等

执行用时 :36 ms, 在所有 Python3 提交中击败了99.57%的用户
内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.29%的用户
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        # 每级目录收集栈
        path_name_stack = list()
        # 拆分path字符串表示的每级
        path_list = path.rstrip('/').split('/')

        for path_name in path_list:
            path_name = path_name.strip()
            if path_name == '' or path_name == '.':
                # 空串 or 当前目录，忽略
                continue
            elif path_name == '..':
                # 返回上级目录
                if len(path_name_stack) > 0:
                    path_name_stack.pop()
            else:
                # 增加目录级
                path_name_stack.append(path_name)
        return '/' + '/'.join(path_name_stack)


if __name__ == '__main__':
    path_str = '/a//b////c/d//././/..'

    s = Solution()
    res = s.simplifyPath(path_str)
    print(res)
