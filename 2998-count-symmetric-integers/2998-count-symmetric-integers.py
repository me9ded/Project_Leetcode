class Solution:
    def calculate(self,s:str):
        size=len(s)
        result=0
        for i in range(size):
            result+=int(s[i])
        return result
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result=0
        for number in range(low,high+1):
            current=str(number)

            size=len(current)
            if(size%2==0):
                mid=size//2
            else:
                mid=size//2-1

            left,right=current[:mid],current[mid:]

            if(self.calculate(left)==self.calculate(right)):
                result+=1
            else:
                continue
        return result

        
