class Solution:
    def anagram(self,word_1,word_2):
        if len(word_1)!= len(word_2):
            return False
        count_1,count_2=Counter(word_1),Counter(word_2)
        return True if count_1==count_2 else False
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result=[words[0]]
        size=len(words)
        for i in range(1,size):
            print(words[i])
            if self.anagram(words[i],words[i-1]):
                continue
            result.append(words[i])
        return result