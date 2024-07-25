class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        temp=[]
        ans=[]
        for i in range(len(nums)):
            val=str(nums[i])
            res=""
            for j in range(len(val)):
                res+=str(mapping[int(val[j])])
            temp.append((int(res),i))
        temp.sort()
        for val in temp:
            ans.append(nums[val[1]])
        return ans

        