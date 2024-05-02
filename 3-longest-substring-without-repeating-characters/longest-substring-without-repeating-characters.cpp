class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n=s.size();
        int ans=0;
        int char_count[256]={0};
        for(int i=0,j=0;j<n;j++){
            char_count[s[j]]++;
            while(char_count[s[j]]>1){
                char_count[s[i]]--;
                i++;
            }
            ans=max(ans,j-i+1);
        }
        return ans;
    }
};