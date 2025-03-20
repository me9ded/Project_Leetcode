class Solution:
    def find(self,node):
        if self.parent[node]==-1:
            return node
        return self.find(self.parent[node])

    def union(self,node_1,node_2):
        parent_1=self.find(node_1)
        parent_2=self.find(node_2)
        if parent_1==parent_2:
            return
        if self.depth[parent_1] < self.depth[parent_2]:
            parent_1,parent_2=parent_2,parent_1
        self.parent[parent_2]=parent_1

        if self.depth[parent_1]==self.depth[parent_2]:
            self.depth[parent_1]+=1
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        self.parent=[-1]*n
        self.depth=[0]*n

        cost=[-1]*n
        for edge in edges:
            self.union(edge[0],edge[1])
        for edge in edges:
            root=self.find(edge[0])
            cost[root]&=edge[2]
        result=[]
        for query in queries:
            start,end=query

            if self.find(start)!=self.find(end):
                result.append(-1)
            else:
                root=self.find(start)
                result.append(cost[root])
        return result







