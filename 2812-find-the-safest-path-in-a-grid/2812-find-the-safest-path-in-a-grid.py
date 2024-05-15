class Solution:
    def __init__(self):
        self.row=[0,0,-1,1]
        self.col=[-1,1,0,0]
    def bfs(self,grid,values,rows):
        q=deque()
        for i in range(rows):
            for j in range(rows):
                if grid[i][j]:
                    values[i][j]=0
                    q.append((i,j))
        while q:
            x,y=q.popleft()
            s=values[x][y]
            for i in range(4):
                new_x=x+self.row[i]
                new_y=y+self.col[i]
                if 0<=new_x<rows and 0<=new_y<rows and values[new_x][new_y]>s+1:
                    values[new_x][new_y]=s+1
                    q.append((new_x,new_y))
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        if grid[0][0] or grid[rows-1][rows-1]:
            return 0
        values=[[float('inf')]*rows for _ in range(rows)]
        self.bfs(grid,values,rows)
        visited=[[False] *rows for _ in range(rows)]
        priority_queue=[(-values[0][0],0,0)]
        heapq.heapify(priority_queue)
        while priority_queue:
            safe,x,y=heapq.heappop(priority_queue)
            safe=-safe
            if x==rows-1 and y==rows-1:
                return safe
            visited[x][y]=True
            for i in range(4):
                new_x=x+self.row[i]
                new_y=y+self.col[i]
                if 0 <= new_x < rows and 0 <= new_y < rows and not visited[new_x][new_y]:
                    s=min(safe,values[new_x][new_y])
                    heapq.heappush(priority_queue,(-s,new_x,new_y))
                    visited[new_x][new_y]=True
        return -1


