class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        def dfs(x,y,res):
            if x<0 or x>=rows or y<0 or y>=cols or grid[x][y]==0:
                return res
            temp=grid[x][y]
            res+=temp
            grid[x][y]=0
            ans=max(dfs(x+1,y,res),dfs(x-1,y,res),dfs(x,y+1,res),dfs(x,y-1,res))
            grid[x][y]=temp
            return ans
        val=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]!=0:
                    val=max(val,dfs(i,j,0))
        return val
