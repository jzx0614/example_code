class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0": 
            return "0"

        result = [0] * (len(num1) + len(num2))
        
        val1 = [int(n) for n in num1]
        val2 = [int(n) for n in num2]
        for i, n1 in enumerate(val1[::-1]):
            for j, n2 in enumerate(val2[::-1]):
                result[i+j] += n1 * n2

        for idx, num in enumerate(result):
            if idx == len(result) - 1: break
            result[idx+1] += num / 10
            result[idx] = num % 10

        output = ''
        for num in result[::-1]:
            if num == 0 and not output: continue
            output += str(num)
            
        return output

if __name__ == "__main__":
    Solution().multiply("123","456")