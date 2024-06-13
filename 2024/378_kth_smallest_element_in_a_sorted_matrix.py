import heapq

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        hq = []
        m, n = len(matrix), len(matrix[0])
        
        for idx in range(min(k, m)):
            heapq.heappush(hq, (matrix[idx][0], idx, 0))
            
        while k > 0:
            value, row, col = heapq.heappop(hq)
            print(value, row, col)
            k -= 1

            if col + 1 < n:
                heapq.heappush(hq, (matrix[row][col+1], row, col + 1))
        return value
        
if __name__ == "__main__":
    print(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))