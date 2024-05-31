class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int start=0;
        int answer=0;
        int res=0;
        for(int i=0;i<s.size();i++){
            res+=abs(s[i]-t[i]);
            while(res > maxCost){
                res-=abs(s[start]-t[start]);
                start+=1;
            }
            answer=max(answer,i-start+1);
        }
        return answer;
    }
};