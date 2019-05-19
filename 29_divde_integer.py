class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        def divide_numer(dividend, divisor):
            print dividend, divisor,
            count = 0
            while not (dividend >= 0 and dividend < abs(divisor)):
                # if(dividend > 0) ^ (divisor > 0):
                #     dividend += divisor
                #     count -= 1
                # else:
                #     dividend -= divisor
                #     count += 1
                dividend -= divisor
                count += 1
            print count, dividend
            return count, dividend

        sign = [(dividend > 0), (divisor > 0)]

        str_dividend = str(abs(dividend))
        unsign_divisor = abs(divisor)
        cal_dividend = output = idx = 0
        for n in str_dividend:
            cal_dividend = cal_dividend * 10 + int(n)
            count, cal_dividend = divide_numer(cal_dividend, unsign_divisor)
            output = output * 10 + count

        if sign[0] ^ sign[1]:
            if output > 2**31:
                output = 2**31 - 1
            else:
                output = -output
        output = min(2**31-1, output)
        return output

if __name__ == "__main__":
    print Solution().divide(2147483647, 2)
    1079241879
    1073741823