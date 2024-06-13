class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        op = ['+', '-', '*']
        ans = []
        for idx, ch in enumerate(expression):
            if ch not in op:
                continue
            left = self.diffWaysToCompute(expression[:idx])
            right = self.diffWaysToCompute(expression[idx+1:])
            ans += [eval("{} {} {}".format(l, ch, r)) for l in left for r in right]

        if len(ans) == 0:
            return [int(expression)]
        
        return ans
        
if __name__ == "__main__":
    print(Solution().diffWaysToCompute("2*3-4*5"))