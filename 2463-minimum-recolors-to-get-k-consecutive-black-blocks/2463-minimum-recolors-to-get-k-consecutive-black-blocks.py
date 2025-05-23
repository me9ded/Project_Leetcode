class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left=0
        whites=0
        result=float("inf")
        for right in range(len(blocks)):
            if blocks[right]=="W":
                whites+=1
            if right-left+1==k:
                result=min(result,whites)
                if blocks[left]=="W":
                    whites-=1
                left+=1
        return result