class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0 
        size = len(strs[0])
        size_1 = len(strs)
        for i in range(size):
            for j in range(1,size_1):
                if strs[j][i] < strs[j-1][i]:
                    result+=1
                    break
        return result 