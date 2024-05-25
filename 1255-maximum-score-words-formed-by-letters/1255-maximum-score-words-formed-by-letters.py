class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        count=[0]*26
        letters_count=[0]*26
        for c in letters:
            count[ord(c)-ord('a')]+=1
        self.ans=0
        self.backtracking(words,count,letters_count,score,0,0)
        return self.ans
    def backtracking(self,words,count,letters_count,score,pos,temp):
        for i in range(26):
            if letters_count[i]>count[i]:
                return
        self.ans=max(self.ans,temp)
        for i in range(pos,len(words)):
            for c in words[i]:
                letters_count[ord(c)-ord('a')]+=1
                temp+=score[ord(c)-ord('a')]
            self.backtracking(words,count,letters_count,score,i+1,temp)
            for c in words[i]:
                letters_count[ord(c)-ord('a')]-=1
                temp-=score[ord(c)-ord('a')]

        
        