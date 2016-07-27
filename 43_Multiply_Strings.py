class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product = [0] * (len(num1) + len(num2))
        for i, e1 in enumerate(reversed(num1)):
            for j, e2 in enumerate(reversed(num2)):
                product[i + j] += int(e1) * int(e2)
                product[i + j + 1] += product[i + j] / 10
                product[i + j] %= 10

        while len(product) > 1 and product[-1] == 0:
            product.pop()

        return ''.join((map(str,product[::-1])))
