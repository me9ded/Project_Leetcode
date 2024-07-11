class Solution:
    def reverseParentheses(self, s: str) -> str:
        temp=deque()
        result=[]
        for part in s:
            if part=="(":
                temp.append(len(result))
            elif part==")":
                begin=temp.pop()
                result[begin:]=result[begin:][::-1]
            else:
                result.append(part)
        return "".join(result)

                

        
        




        