class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        if(nums.empty()){
            return nums;
        }
        int min_val=*min_element(nums.begin(),nums.end());
        int max_val=*max_element(nums.begin(),nums.end());
        vector<int> counts(max_val-min_val+1);
        for(int num:nums){
            counts[num-min_val]++;
        }
        int j=0;
        for(int i=0;i<counts.size();i++){
            while(counts[i]-->0){
                nums[j++]=i+min_val;
            }
        }
        return nums;
    }
};