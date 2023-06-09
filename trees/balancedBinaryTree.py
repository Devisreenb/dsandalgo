# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        res = Tgithrue 
        def dfs(root,h):
            nonlocal res
            if not root:
                return h-1
            left = dfs(root.left,h+1)
            right= dfs(root.right,h+1)
            if(abs(left-right))>1:
                res = False
            return max(left,right)
        dfs(root,0)
        return res
            