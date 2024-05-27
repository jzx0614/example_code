import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for v in nums:
            if len(heap) < k:
                heapq.heappush(heap, v)
                continue
            heapq.heappushpop(heap, v)
        return heap[0]

if __name__ == "__main__":
    print(Solution().findKthLargest([3,2,1,5,6,4], 2))
