class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word) < 8:
            return len(word)
        freq=[0]*26
        res=0
        for w in word:
            freq[ord(w)-ord('w')]+=1
        freq.sort(reverse=True)
        for i in range(26):
            if freq[i]==0:
                break
            res+=(i//8+1) * freq[i]
        return res
         