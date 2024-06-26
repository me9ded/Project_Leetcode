# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        temp=[]
        self.dfs(root,temp)
        return self.bst_creator(temp,0,len(temp)-1)
    def dfs(self,node,temp):
        if not node:
            return
        self.dfs(node.left,temp)
        temp.append(node.val)
        self.dfs(node.right,temp)
    def bst_creator(self,temp,start,end):
        if start > end:
            return None
        mid=(start+end)//2
        left_tree=self.bst_creator(temp,start,mid-1)
        right_tree=self.bst_creator(temp,mid+1,end)
        res=TreeNode(temp[mid],left_tree,right_tree)
        return res    


            
            
        