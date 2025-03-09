class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        result=0
        left=0
        right=0

        for i in range(k-1):
            colors.append(colors[i])

        while right < len(colors):

            if colors[right]==colors[right-1]:
                left=right
                right+=1
                continue
            right+=1

            if right-left < k:
                continue
            result+=1
            left+=1
        return result





