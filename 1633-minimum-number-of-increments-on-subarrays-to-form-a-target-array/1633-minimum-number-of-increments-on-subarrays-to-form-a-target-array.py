class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        size = len(target)
        initial = [0]*size
        result = target[0]
        for i in range(1,size):
            result+=max(target[i] - target[i-1], 0)
        return result