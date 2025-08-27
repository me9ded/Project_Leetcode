class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        directions=[(1,1),(1,-1),(-1,-1),(-1,1)]
        rows,cols=len(grid),len(grid[0])

        @cache
        def dfs(x,y,direction,turn,target):
            new_x,new_y=x+directions[direction][0],y+directions[direction][1]
            
            if new_x < 0 or new_y < 0 or new_x >= rows or new_y >= cols or grid[new_x][new_y]!=target:
                return 0
            turn_var=1 if turn else 0
            steps=dfs(new_x,new_y,direction,turn,2-target)
            if turn:
                steps=max(steps,dfs(new_x,new_y,(direction+1)%4,False,2-target))
            return steps+1

        result=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    for direction in range(4):
                        result=max(result,dfs(i,j,direction,True,2)+1)
        return result
