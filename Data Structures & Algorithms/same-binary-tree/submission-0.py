# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_lst = []
        q_lst = []
        def dfs(node, lst):
            if not node:
                lst.append(None)
                return False
            lst.append(node.val)
            dfs(node.left, lst)
            dfs(node.right, lst)
        
        dfs(p, p_lst)
        dfs(q, q_lst)

        if p_lst == q_lst:
            return True

        return False
        