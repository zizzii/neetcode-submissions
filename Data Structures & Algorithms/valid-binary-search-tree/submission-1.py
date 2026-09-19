# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(p, maxV, minV):
            if p.val >= maxV or p.val <= minV:
                return False

            if p.left:
                if not dfs(p.left, p.val, minV):
                    return False;
            if p.right:
                if not dfs(p.right, maxV, p.val):
                    return False
            
            return True

        
        return dfs(root, 1000000000, -1000000000)

        