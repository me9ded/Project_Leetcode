class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        set<int> distinctElements(nums.begin(), nums.end());
        int size = nums.size();
        int result = 0;

        for (int i = 0; i < size; i++) {
            unordered_set<int> currentSet;
            for (int j = i; j < size; j++) {
                currentSet.insert(nums[j]);
                if (currentSet.size() == distinctElements.size()) {
                    result++;
                }
            }
        }
        return result;
    }
};