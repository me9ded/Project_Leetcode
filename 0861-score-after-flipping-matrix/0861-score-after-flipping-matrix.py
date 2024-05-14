class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        res=0
        for i in range(rows):
            if grid[i][0]==0:
                for j in range(cols):
                    grid[i][j]=1-grid[i][j]
        for j in range(1,cols):
            count1,count0=0,0
            for i in range(rows):
                if grid[i][j]==1:
                    count1+=1
                else:
                    count0+=1
            if count0>count1:
                for i in range(rows):
                    grid[i][j]=1-grid[i][j]
        for i in range(rows):
            res+=int(''.join(str(c) for c in (grid[i])),2)
        return res
        
