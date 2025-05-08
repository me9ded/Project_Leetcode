class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        freq = [[float("inf")] * cols for _ in range(rows)]
        freq[0][0] = 0
        min_heap = []
        heapq.heapify(min_heap)
        heapq.heappush(min_heap, (0, 0, 0))
        
        while len(min_heap) > 0:
            cost, row, col = heapq.heappop(min_heap)
            if (row,col)==(rows-1,cols-1):
                return cost
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            
            for adj_i, adj_j in directions:
                new_row = row + adj_i
                new_col = col + adj_j
                
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    moves= 1 if (row + col) % 2==0 else 2
                    new_cost = max(cost , moveTime[new_row][new_col]) + moves
                    if new_cost < freq[new_row][new_col]:
                        freq[new_row][new_col] = new_cost
                        heapq.heappush(min_heap, (new_cost, new_row, new_col))
        return freq[-1][-1]

                  