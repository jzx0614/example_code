class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import heapq
        stone_list = [-s for s in stones]
        heapq.heapify(stone_list)

        while len(stone_list) > 1:
            value1, value2 = heapq.heappop(stone_list), heapq.heappop(stone_list)
            if value1 != value2:
                heapq.heappush(stone_list, -abs(value1 - value2))

        return len(stone_list) and -stone_list[0]



if __name__ == "__main__":
    print Solution().lastStoneWeight([2, 7, 4, 1, 8, 1])
