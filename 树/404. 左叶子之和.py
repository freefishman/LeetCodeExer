class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 前序遍历
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        if root == None:
            return 0
        stack = [root]
        res = 0
        while stack:
            node = stack.pop()
            if node.left != None and node.left.left == None and node.left.right == None:
                res += node.left.val
            stack.append(node.left)
            stack.append(node.right)
        return res
Solution.sumOfLeftLeaves(1, [3,9,20,None,None,15,7])