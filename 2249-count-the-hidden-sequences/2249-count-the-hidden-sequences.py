class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        left=right=result=0
        for number in differences:
            result+=number
            left=min(left,result)
            right=max(right,result)
        if right-left > upper-lower:
            return 0
        return (upper-lower)-(right-left)+1
                
        