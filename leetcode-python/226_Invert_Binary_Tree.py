#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################################
# File Name: 226_Invert_Binary_Tree.py
# Author: Wang Biwen
# mail: wangbiwen88@126.com
# Created Time: 2016.06.23
#########################################################################

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

