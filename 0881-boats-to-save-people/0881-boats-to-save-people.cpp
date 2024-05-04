class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.rbegin(),people.rend());
        int l=0;
        int r=people.size()-1;
        while(l<=r){
            if(people[l]+people[r]<=limit){
                r-=1;
            }
            l+=1;
        }
        return l;
    }
};