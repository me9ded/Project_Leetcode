class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        infinite=float("inf")
        size=len(colors)
        adjacent=defaultdict(list)

        for u,v in edges:
            adjacent[u].append(v)
        freq=[[0]*26 for _ in range(size)]
        visited=[0]*size
        
        def dfs(node):
            if visited[node]==1:
                return infinite
            if visited[node]==2:
                return freq[node][ord(colors[node])-ord('a')]
            
            visited[node]=1

            for nex in adjacent[node]:
                result=dfs(nex)
                if result==infinite:
                    return infinite
                for c in range(26):
                    freq[node][c]=max(freq[node][c],freq[nex][c])
            color=ord(colors[node])-ord('a')
            freq[node][color]+=1
            visited[node]=2
            
            return freq[node][color]
        answer=0
        for i in range(size):
            value=dfs(i)
            if value==infinite:
                return -1
            answer=max(answer,value)
        return answer