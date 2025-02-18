class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack=[]
        result=[]
        for i in range(len(pattern)+1):
            stack.append(i+1)
            if i==len(pattern) or 'I'==pattern[i]:
                while stack:
                    result.append(str(stack.pop()))
        return "".join(result)




        