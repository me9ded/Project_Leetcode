class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result=[]
        size=len(words)
        for i in range(size):
            if x in words[i]:
                result.append(i)
        return result