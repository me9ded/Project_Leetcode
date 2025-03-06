class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        result=[0,0]
        count={}
        max_val=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_val=max(max_val,grid[i][j])
                count[grid[i][j]]=count.get(grid[i][j],0)+1
        for key,val in count.items():
            if val==2:
                result[0]=key
        for i in range(1,max_val+2):
            temp=list(count.keys())
            if i not in temp:
                result[1]=i
                break
        return result
            


                
        