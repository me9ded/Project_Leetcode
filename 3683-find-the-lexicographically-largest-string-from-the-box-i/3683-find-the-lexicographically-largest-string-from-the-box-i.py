class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        result=""
        if numFriends==1:
            return word
        size=len(word)
        for i in range(size):
            result=max(result,word[i:min(i+size-numFriends + 1,size)])
        return result
