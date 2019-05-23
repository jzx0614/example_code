class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if k == 0 or n == 0:
            return ''

        order = [1, 1]
        for i in xrange(1, n):
            order.append((i+1) * order[-1])
        
        if k > order[-1]:
            return ''

        n_list = [str(i+1)for i in range(n)]
        output = ""

        k -= 1
        for value in order[-2::-1]:
            output += n_list.pop(k // value)
            k = k % value
        
        return output

if __name__ == "__main__":
    print Solution().getPermutation(9, 219601)
    # print Solution().getPermutation(4, 9)

 
