class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=set()
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    res.add(words[i])
                elif words[j] in words[i]:
                    res.add(words[j])
        res=list(res)        
        return res
        