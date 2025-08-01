class Solution:
    def generate(self, s: int) -> List[List[int]]:
        if s==0:
            return [[]]
        if s==1:
            return[[1]]
        prevrows=self.generate(s-1)
        newrow=[1]*s
        for i in range(1,s-1):
            newrow[i]=prevrows[-1][i-1]+prevrows[-1][i]
        prevrows.append(newrow)
        return prevrows
