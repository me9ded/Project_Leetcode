class Solution:
    def dfs(self,current,distance,distances,edges):
        while current != -1 and distances[current]==-1:
            distances[current]=distance
            distance+=1
            current=edges[current]
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        size=len(edges)
        value=float("inf")
        result=-1
        distances1=[-1]*size
        distances2=[-1]*size
        self.dfs(node1,0,distances1,edges)
        self.dfs(node2,0,distances2,edges)

        for i in range(size):
            if distances1[i] >=0 and distances2[i] >=0:
                max_dist=max(distances1[i],distances2[i])

                if max_dist < value:
                    value=max_dist
                    result=i
        return result
