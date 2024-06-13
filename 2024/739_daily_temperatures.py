class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ans = [0] * len(temperatures)
        for idx, value in enumerate(temperatures):
            while len(stack) > 0 and temperatures[idx] > stack[-1][1]:
                print(idx, temperatures[idx], stack, ans)
                pre_index, value = stack.pop()
                ans[pre_index] = idx- pre_index
            stack.append([idx, temperatures[idx]])
        
        return ans

if __name__ == "__main__":
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))