import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        flag = [[float("inf")] * cols for _ in range(rows)]
        min_heap = []
        heapq.heappush(min_heap, (0, 0, 0))

        while min_heap:
            cost, row, col = heapq.heappop(min_heap)

            if row == rows - 1 and col == cols - 1:
                return cost

            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for adj_i, adj_j in directions:
                new_row, new_col = row + adj_i, col + adj_j

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    new_cost = max(moveTime[new_row][new_col], cost) + 1
                    if new_cost < flag[new_row][new_col]:
                        flag[new_row][new_col] = new_cost
                        heapq.heappush(min_heap, (new_cost, new_row, new_col))

        return flag[-1][-1]

        


                