class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows,cols=len(grid),len(grid[0])
        res=[]
        for i in range(rows-2):
            temp=[]
            for j in range(cols-2):
                a=max([grid[i][j],grid[i][j+1],grid[i][j+2]])
                b=max([grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2]])
                c=max([grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]])
                d=max([a,b,c])
                temp.append(d)
            res.append(temp)
        return res