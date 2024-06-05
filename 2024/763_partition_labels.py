class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_mp = {c: idx for idx, c in enumerate(s)}
        # print(mp)
        ans = []
        start = end = 0
        for idx, c in enumerate(s):
            end = max(end, last_mp[c])

            if idx == end:
                ans.append(end - start + 1)
                start = idx + 1
        return ans
if __name__ == "__main__":
    print(Solution().partitionLabels("ababcbacadefegdehijhklij"))