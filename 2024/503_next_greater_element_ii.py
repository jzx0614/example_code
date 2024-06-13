class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n
        for idx in range(n*2):
            num = nums[idx % n]
            while len(stack) > 0 and nums[stack[-1]] < num:
                ans[stack.pop()] = num
            
            if idx < n:
                stack.append(idx)

        return ans

if __name__ == "__main__":
    print(Solution().nextGreaterElements([1,2,1]))