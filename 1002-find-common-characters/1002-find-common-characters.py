class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res=Counter(words[0])
        for word in words:
            res&=Counter(word)
        return list(res.elements())

        