class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]

        max_value = 0
        for idx, c in enumerate(s):
            if c == "(":
                stack.append(idx)
            elif stack:
                # print stack, idx, stack[-1]
                stack.pop()
                if not stack: stack.append(idx)
                print stack, idx, stack[-1]
                max_value = max(max_value, idx - stack[-1])
                
        return max_value

if __name__ == "__main__":
    # print Solution().longestValidParentheses(")(")
    # print Solution().longestValidParentheses("(()")
    # print Solution().longestValidParentheses(")()())")
    print Solution().longestValidParentheses(")()())()()(")
