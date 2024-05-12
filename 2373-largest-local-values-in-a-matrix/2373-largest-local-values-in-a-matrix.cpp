class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int rows=grid.size();
        int cols=grid[0].size();
        vector<vector<int>> res;
        for(int i=0;i<rows-2;i++){
            vector<int> temp;
            for(int j=0;j<cols-2;j++){
                int a=max({grid[i][j],grid[i][j+1],grid[i][j+2]});
                int b=max({grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2]});
                int c=max({grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]});
                int d=max({a,b,c});
                temp.push_back(d);
            }
            res.push_back(temp);
        }
        return res;
    }
};