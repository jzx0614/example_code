class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        r = [""] * 31
        r[1] = "1"
        r[2] = "11"

        for idx in range(2, n):
            pre_char = ""
            count = 1
            for c in r[idx]:
                if pre_char == c:
                    count += 1
                else:
                    if pre_char:
                        r[idx+1] += str(count) + pre_char
                    pre_char = c
                    count = 1
            r[idx+1] += str(count) + c
            
        return r[n]

if __name__ == "__main__":
    print Solution().countAndSay(10)