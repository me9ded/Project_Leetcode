class Solution {
public:
    int minDifference(vector<int>& nums) {
        int n=nums.size();
        int res=INT_MAX;
        if(n<=4){
            return 0;
        }
        partial_sort(nums.begin(),nums.begin()+4,nums.end());
        nth_element(nums.begin()+4,nums.begin()+(n-4),nums.end());
        sort(nums.begin()+(n-4),nums.end());
        for(int i=0,j=n-4;i<4;i++,j++){
            res=min(res,nums[j]-nums[i]);
        }
        return res;
        
    }
};