class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        '''
            - Group the number by thousands(3 digits), can write a helper function that takes
              a number less than 1000, and convert just that chunk to words
            - Edge case: 10,000,010
        '''
        lessThan20 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
                      'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        # https://discuss.leetcode.com/topic/23061/recursive-python
        # Cannot recursively call itself, because cannot deal with the edge case where one of
        # chunk is 000, so have to define a new function to take care of the original edge cases

        def words(n):
            if n < 20:
                # At first, I use '' as index 0, but this will add to the final result, adding unwanted space
                # into the result, so should remove the None string, just use index - 1 here.
                # In this case, if n == 0, will return [], and it won't be added to the final result
                return lessThan20[n - 1:n]
            elif n < 100:
                return [tens[n / 10 - 2]] + words(n % 10)
            elif n < 1000:
                return [lessThan20[n / 100 - 1]] + ['Hundred'] + words(n % 100)
            else:
                for p, w in enumerate(['Thousand', 'Million', 'Billion'], 1):
                    if n < 1000 ** (p + 1):
                        return words(n / 1000 ** p) + [w] + words(n % (1000 ** p))
        # To make the space formatted (no extra spaces) during recursions, the best solution is to join spaces
        # at the last
        return ' '.join(words(num)) or 'Zero'
