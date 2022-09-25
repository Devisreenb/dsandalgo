# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def init(self):
        self.maxi=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi=0
        self.height(root)
        return self.maxi
    def height(self,root):
        if root ==None:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        self.maxi = max(self.maxi,r+l)
        return (1+max(r,l))