class Solution(object):
    map_letters = {
        '2':'abc', 
        '3':'def', 
        '4':'ghi', 
        '5':'jkl', 
        '6':'mno', 
        '7':'pqrs', 
        '8':'tuv', 
        '9':'wxyz'
    }
	    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []        
        result = []
        self.stack_str = ""
        def dfs (digit_idx):
            if len(digits) == digit_idx:
                result.append(self.stack_str)
                return

            for c in self.map_letters[digits[digit_idx]]:
                self.stack_str += c
                dfs(digit_idx+1)
                self.stack_str = self.stack_str[:-1]
        dfs(0)

        return result

if __name__ == "__main__":
    print Solution().letterCombinations("23")

