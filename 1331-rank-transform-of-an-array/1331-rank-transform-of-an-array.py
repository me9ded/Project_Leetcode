class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp=sorted(arr)
        rank=0
        hash_map={}
        for i in range(len(temp)):
            if i > 0 and temp[i] > temp[i-1]:
                rank+=1
            hash_map[temp[i]]=rank
        for i in range(len(arr)):
            arr[i]=hash_map[arr[i]]+1
        return arr