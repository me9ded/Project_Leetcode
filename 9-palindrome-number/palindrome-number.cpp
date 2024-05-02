class Solution {
public:
    bool isPalindrome(int x) {
        string res=to_string(x);
        int l=0;
        int r=res.size()-1;
        while(l<=r){
            if(res[l]!=res[r]){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
};