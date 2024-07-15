# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        temp={}
        nodes=set()
        child_nodes=set()
        for parent,child,position in descriptions:
            if parent not in temp:
                temp[parent]=[]
            temp[parent].append((child,position))
            nodes.add(parent)
            nodes.add(child)
            child_nodes.add(child)
        root_val=(nodes-child_nodes).pop()
        def dfs(val):
            node=TreeNode(val)
            if val in temp:
                for child,position in temp[val]:
                    if position:
                        node.left=dfs(child)
                    else:
                        node.right=dfs(child)
            return node
        return dfs(root_val)


        


            
        



        