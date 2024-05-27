class Solution {
public:
    int specialArray(vector<int>& nums) {
        int N=nums.size();
        vector<int> freq(N+1,0);
        for(auto num:nums){
            freq[min(N,num)]+=1;
        }
        int answer=0;
        for(int i=N;i>0;i--){
            answer+=freq[i];
            if(i==answer){
                return i;
            }
        }
        return -1;
    }
};