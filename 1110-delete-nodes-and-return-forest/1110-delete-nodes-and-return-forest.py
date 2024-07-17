# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        res = []
        root = self.dfs(root, to_delete_set, res)
        if root:
            res.append(root)
        return res

    def dfs(self,node, to_delete_set,res):
        if not node:
            return None
        node.left = self.dfs(node.left, to_delete_set, res)
        node.right = self.dfs(node.right, to_delete_set, res)

        if node.val in to_delete_set:
            if node.left:
                res.append(node.left)
            if node.right:
                res.append(node.right)
            return None
        return node
