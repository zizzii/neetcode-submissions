# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nGoodNodes = 1
        def dfs(n ,maxValue):
            nonlocal nGoodNodes
            if n.val >= maxValue:
                nGoodNodes += 1
                maxValue = n.val
            if n.left:
                dfs(n.left, maxValue)
            if n.right:
                dfs(n.right, maxValue)

        if root.left:
            dfs(root.left, root.val)
        if root.right:
            dfs(root.right, root.val)

        return nGoodNodes
