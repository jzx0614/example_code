class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if len(letters) == 1: return letters[0]
        if letters[-1] <= target: return letters[0]

        l, r = 0, len(letters) - 1
        while l < r:
            idx = l + (r-l) // 2
            print(l, r, idx)

            if letters[idx] <= target:
                l = idx + 1
            else:
                r = idx

        return letters[l]
if __name__ == "__main__":
    print(Solution().nextGreatestLetter(["c", "f", "j"], "c"))