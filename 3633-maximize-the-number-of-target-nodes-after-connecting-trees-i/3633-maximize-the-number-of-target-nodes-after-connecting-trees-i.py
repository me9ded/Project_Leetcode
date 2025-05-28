class Solution:
    def dfs(self,node,parent,children,k):
        if k < 0:
            return 0
        res=1
        for child in children[node]:
            if child==parent:
                continue
            res+=self.dfs(child,node,children,k-1)
        return res
    def build(self,edges,k):
        size=len(edges)+1
        children=[[] for _ in range(size)]
        for u,v in edges:
            children[u].append(v)
            children[v].append(u)
        res=[0]*size
        for i in range(size):
            res[i]=self.dfs(i,-1,children,k)
        return res

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        size=len(edges1)+1
        count1=self.build(edges1,k)
        count2=self.build(edges2,k-1)
        max_count2=max(count2)
        result=[count1[i]+max_count2 for i in range(size)]
        return result