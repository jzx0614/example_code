class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans



# [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# [4,4][5,0][5,2][6,1][7,0][7,1]
# [5,0][7,0][5,2][6,1][4,4][7,1]

if __name__ == "__main__":
    print(Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))