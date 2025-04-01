class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        size=len(questions)
        dp=[0]*size
        for i in range(size-1,-1,-1):
            index=i+questions[i][1]+1
            if index < size:
                dp[i]=dp[index]+questions[i][0]
            else:
                dp[i]=questions[i][0]
            if i < size-1:
                dp[i]=max(dp[i+1],dp[i])
        return dp[0]


