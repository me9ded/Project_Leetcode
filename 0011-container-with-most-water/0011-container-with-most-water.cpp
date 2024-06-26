class Solution {
public:
    int maxArea(vector<int>& height) {
        int i=0;
        int j=height.size()-1;
        int res=0;
        while(i<j){
            int curr=(j-i)*min(height[i],height[j]);
            res=max(res,curr);
            if (height[i]<height[j]){
                i++;
            }
            else{
                j--;
            }
        }
        return res;
    }
};