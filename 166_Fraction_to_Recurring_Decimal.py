class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # repeating: same remainder
        # Use HashMap to store a remainder and its associated index while doing the division
        # so that whenever a same remainder comes up, we know there is a repeating fractional part.
        # Need to store index, because may be a sequence repeating

        if numerator == 0:
            return '0'
        res = ''
        if (numerator > 0) ^ (denominator > 0):
            res += '-'

        num, den = abs(numerator), abs(denominator)

        # integral part
        res += str(num / den)
        num %= den
        if num == 0:
            return res
        # fractional part
        res += '.'
        dic = {num: len(res)}  # store a remainder and its index
        while num != 0:
            num *= 10
            res += str(num/den)
            num %= den
            if num in dic:
                index = dic[num]
                res = res[:index] + '(' + res[index:] + ')'
                break
            else:
                dic[num] = len(res)

        return res