class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        s_len, p_len = len(s), len(p)
        dp = [[False for _ in xrange(s_len+1)] for _ in xrange(p_len+1)]
        dp[0][0] = True # s[:0]  p[:0] match

        def print_dp():
            print '      ' + '  '.join(s)
            for idx in xrange(p_len + 1):
                if idx == 0 : print " ",
                else: print p[idx-1],
                print map(lambda x: 1 if x else 0, dp[idx])
            print 

        for i in xrange(1, p_len+1):
            if p[i-1] != "*": break
            dp[i][0] = True

        for p_idx in xrange(1, p_len+1):
            for s_idx in xrange(1, s_len+1):
                if (p[p_idx-1] in ['?', s[s_idx-1]]) and dp[p_idx-1][s_idx-1]:
                    dp[p_idx][s_idx] = True 
                 
                elif p[p_idx-1] == "*" and (dp[p_idx-1][s_idx-1] or dp[p_idx-1][s_idx]):
                    for k in xrange(s_idx, s_len+1):
                        dp[p_idx][k] = True
                    continue
        print_dp()
        return dp[-1][-1]


    # def isMatch(self, s, p):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: bool
    #     """
    #     self.s_len, self.p_len = len(s), len(p)
    #     s_idx = p_idx = 0
    #     stack = []
    #     while s_idx < self.s_len:
    #         if p_idx == self.p_len and not stack:
    #             return False

    #         elif p_idx < self.p_len and p[p_idx] in ['?', s[s_idx]]:
    #             s_idx +=1
    #             p_idx +=1
    #         elif p_idx < self.p_len and p[p_idx] == "*":
    #             while p_idx + 1 < self.p_len and "*" == p[p_idx+1]: 
    #                 p_idx += 1
    #             stack.append((s_idx+1, p_idx+1))
    #             p_idx += 1
    #         elif not stack:
    #             return False
    #         else:
    #             s_idx, p_idx = stack[-1]
    #             stack[-1] = (s_idx+1, p_idx)
            
    #     return all(x == '*' for x in p[p_idx:])
        

if __name__ == "__main__":
    # print Solution().isMatch("a", "a*")
    # print Solution().isMatch("aa", "*")
    print Solution().isMatch("acdcba", "a*c?b")
    # print Solution().isMatch("adceb", "*a*b")
    # print Solution().isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b")
    # print Solution().isMatch("mississippi", "m??*ss*?i*pi")
    
    # print Solution().isMatch("axccxxcxxdcxxxcb", "a*c*c*?b")
    # print Solution().isMatch("bbaaaabaaaaabbabbabbabbababaabababaabbabaaabbaababababbabaabbabbbbbbaaaaaabaabbbbbabbbbabbabababaaaaa",
    # "******aa*bbb*aa*a*bb*ab***bbba*a*babaab*b*aa*a****")