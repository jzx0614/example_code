class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if not p:
            return not s

        if p[0] == "*":
            while 1 < len(p) and "*" == p[1]: p = p[1:]
            
            return self.isMatch(s, p[1:]) or (bool(s) and  self.isMatch(s[1:], p))
        elif not s:
            return False
        elif p[0] in ['?', s[0]]:
            return self.isMatch(s[1:], p[1:])
        else:
            return False

if __name__ == "__main__":
    print Solution().isMatch("acdcb", "a*c?b")
    # print Solution().isMatch("adceb", "*a*b")
    # print Solution().isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b")
    # print Solution().isMatch("mississippi", "m??*ss*?i*pi")
    

    # print Solution().isMatch("bbaaaabaaaaabbabbabbabbababaabababaabbabaaabbaababababbabaabbabbbbbbaaaaaabaabbbbbabbbbabbabababaaaaa",
    # "******aa*bbb*aa*a*bb*ab***bbba*a*babaab*b*aa*a****")