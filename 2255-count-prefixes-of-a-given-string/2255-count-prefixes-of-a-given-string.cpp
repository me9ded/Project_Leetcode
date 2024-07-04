class Solution {
public:
    int countPrefixes(vector<string>& words, string s) {
        int res=0;
        for (auto word:words){
            if(s.starts_with(word)){
                res++;
            }
        }
        return res;
    }
};