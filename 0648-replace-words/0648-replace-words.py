class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        count=sentence.split()
        for i in range(len(count)):
            previous=count[i]
            for word in dictionary:
                if previous.startswith(word):
                    if len(word)<len(previous):
                        previous=word
            count[i]=previous
        return ' '.join(count)
        