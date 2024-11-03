class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        res=True
        res1=False
        for i in range(len(sentence)):
            if sentence[i]==" ":
                if sentence[i-1]!=sentence[i+1]:
                    res=False
        if sentence[-1]==sentence[0]:
            res1=True
        return res and res1

        