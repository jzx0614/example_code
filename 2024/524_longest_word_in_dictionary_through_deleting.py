class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        out_str = ""
        for word in dictionary:
            if len(word) < len(out_str) or (len(word) == len(out_str) and word > out_str):
                continue
            if self.is_substr(s, word):
                out_str = word
                print(word)
        return out_str

    def is_substr(self, s, word):
        word_idx = 0
        for c in s:
            if c == word[word_idx]:
                word_idx += 1
            if word_idx == len(word): 
                return True
        return False

if __name__ == "__main__":
    print(Solution().findLongestWord(["abpcplea"], ["ale","apple","monkey","plea"]))