class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        min_profile = float('inf')
        max_profile = 0

        for value in prices:
            if value < min_profile:
                total += max_profile
                min_profile = value
                max_profile = 0
            elif value - min_profile > max_profile:
                max_profile = value - min_profile
            elif value - min_profile <= max_profile:
                total += max_profile
                min_profile = value
                max_profile = 0
            # print value, 'min, max:', min_profile, max_profile, "total", total

        if max_profile != 0:
            total += max_profile

        return total

if __name__ == "__main__":
    # print Solution().maxProfit([7,1,5,3,6,4])
    # print Solution().maxProfit([7,6,4,3,1])
    print Solution().maxProfit([2,1,2,0,1])

