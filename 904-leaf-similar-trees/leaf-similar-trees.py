# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2):

        def get_leaves(root):
            leaves = []

            def dfs(node):
                if node is None:
                    return

                
                if node.left is None and node.right is None:
                    leaves.append(node.val)
                    return

                dfs(node.left)
                dfs(node.right)

            dfs(root)
            return leaves

        return get_leaves(root1) == get_leaves(root2)