class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        temp=[]
        result=0

        for row in grid:
            for number in row:
                temp.append(number)
        temp.sort()
        size=len(temp)
        mid=temp[size//2]

        for num in temp:
            if num%x != mid%x:
                return -1
            result+=abs(mid-num)//x
        return result
