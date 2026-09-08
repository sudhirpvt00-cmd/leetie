# ──────────────────────────────────────────────────
# Problem  : 105. Construct Binary Tree from Preorder and Inorder Traversal
# Difficulty: Medium
# Tags     : Array, Hash Table, Divide and Conquer, Tree, Binary Tree
# Link     : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12340000 (beats 0%)
# Language : python
# Copyright: (c) 2026 sudhirpvt00-cmd. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Map values to their indices in inorder for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        self.pre_idx = 0
        
        def array_to_tree(left, right):
           
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            
            self.pre_idx += 1
 
            index = inorder_map[root_val]

            root.left = array_to_tree(left, index - 1)
            root.right = array_to_tree(index + 1, right)
            
            return root

        return array_to_tree(0, len(inorder) - 1)