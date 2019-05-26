class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        output = []
        stack = []
        def valid_ip(s, n):
            # print stack, s, n
            if not s:
                if n == 4:
                    output.append('.'.join(stack[:]))
                return
            if n >= 4:
                return

            if len(s) >= 3 and 100 <= int(s[:3]) < 256:
                stack.append(s[:3])
                valid_ip(s[3:], n+1)
                stack.pop()
            if len(s) >= 2 and 10 <= int(s[:2]) < 100:
                stack.append(s[:2])
                valid_ip(s[2:], n+1)
                stack.pop()
            if len(s) >= 1:
                stack.append(s[0])
                valid_ip(s[1:], n+1)
                stack.pop()

        valid_ip(s, 0)
        return output


if __name__ == "__main__":
    print Solution().restoreIpAddresses("010010")