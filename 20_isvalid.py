class Solution(object):
    stack = ""
    pop_map = ["()", "{}", "[]"]

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            # print self.stack
            return not self.stack

        self.stack += s[0]
        
        # print self.stack, s[0]
        if len(self.stack) >= 2 and self.stack[-2:] in self.pop_map:
            print self.stack, s[0]
            self.stack = self.stack[:-2]
        return self.isValid(s[1:])
        

if __name__ == "__main__":
    print Solution().isValid('{[]}')