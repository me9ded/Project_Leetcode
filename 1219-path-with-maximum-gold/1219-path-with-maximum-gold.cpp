class Solution {
    int rows,cols;
    int val=0;
    void dfs(int x,int y,int res,vector<vector<int>>& grid){
        if(x<0 || x>=rows || y<0 || y>=cols || grid[x][y]==0){
            return ;
        }
        int temp=grid[x][y];
        res+=temp;
        val=max(val,res);
        grid[x][y]=0;
        dfs(x+1,y,res,grid);
        dfs(x-1,y,res,grid);
        dfs(x,y+1,res,grid);
        dfs(x,y-1,res,grid);
        res-=temp;
        grid[x][y]=temp;
    }
public:
    int getMaximumGold(vector<vector<int>>& grid) {
        rows=grid.size();
        cols=grid[0].size();
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(grid[i][j]!=0){
                    dfs(i,j,0,grid);
                }
            }
        }
        return val;
    }
};