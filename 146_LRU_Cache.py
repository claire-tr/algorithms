class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = collections.OrderedDict()
        self.remain = capacity


    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)
        self.cache[key] = val   # set key as the newest one
        return val


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = value
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.cache.popitem(last=False)
            self.cache[key] = value

'''
    Ordered Dict is construct based on double-linked list
    Double-linked List
    hash map: <value, linked node>
    node: key, val, pre, next
    https://discuss.leetcode.com/topic/14591/python-dict-double-linkedlist
'''