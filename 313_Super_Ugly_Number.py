

# Time Limit Exceed
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        index = [0] * len(primes)
        temp_ugly = [0] * len(primes)
        while n > 1:
            for i in range(len(primes)):
                temp_ugly[i] = primes[i] * ugly[index[i]]
            temp_min = min(temp_ugly)
            if temp_min not in ugly:
                n -= 1
                ugly.append(temp_min)
            for i in range(len(primes)):
                if temp_min == temp_ugly[i]:
                    index[i] += 1
                    break
        return ugly[-1]