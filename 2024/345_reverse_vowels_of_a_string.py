class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        vowels_list = [*vowels]
        v_index = [idx for idx, c in enumerate(s) if c in vowels_list ]
        print(v_index)
        
        s_list = [*s]
        print(s_list)
        for i in range(len(v_index) // 2):
            left, right = v_index[i], v_index[-1-i]
            s_list[left], s_list[right] = s_list[right], s_list[left]

        return "".join(s_list)
    
    def reverseVowels(self, s: str) -> str:
        # if len(s) == 0: return ""

        vowels = 'aeiouAEIOU'
        vowels_list = [*vowels]
        
        s_list = [*s]
        left, right = 0, len(s)-1

        while left <= right:
            while left <= right and s[left] not in vowels_list : left += 1
            while left <= right and s[right] not in vowels_list: right -= 1
            if left > right:
                break
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return "".join(s_list)

if __name__ == "__main__":
    # print(Solution().reverseVowels("leetcode"))
    print(Solution().reverseVowels(""))