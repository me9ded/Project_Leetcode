class Solution {
public:
    string reverseParentheses(string s) {
        stack<int> temp;
        string answer;
        for(char part:s){
            if (part=='('){
                temp.push(answer.length());
            }
            else if(part==')'){
                int start=temp.top();
                temp.pop();
                reverse(answer.begin()+start,answer.end());
            }
            else{
                answer+=part;
            }
        }
        return answer;

    }
};