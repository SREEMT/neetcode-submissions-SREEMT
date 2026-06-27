# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def depth(node):
            # return 0 if node doesnt exist, doesnt contribute to diameter calc
            if not node:
                return 0

            # recursion for left and right branches, ads one as it comes back up to root
            left = depth(node.left)
            right = depth(node.right)

            self.diameter = max(self.diameter, left + right)    # Updates diameter size

            # Returns 1 added to the depth of the max branch depth
            return 1 + max(left, right) 

        depth(root)
        return self.diameter