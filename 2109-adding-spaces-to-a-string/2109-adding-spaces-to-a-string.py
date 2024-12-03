class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=[]
        index=0
        for i in range(len(s)):
            print(index)
            if index < len(spaces) and i==spaces[index]:
                res.append(" ")
                index+=1
            res.append(s[i])
        return "".join(res)
        

                
            
        