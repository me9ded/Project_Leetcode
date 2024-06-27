class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        temp=[]
        for i in range(len(edges)):
            temp.append(edges[i][0])
            temp.append(edges[i][1])
        count=Counter(temp)
        for item,num in count.items():
            if num==len(edges):
                return item
        


        