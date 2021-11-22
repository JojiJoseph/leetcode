class RandomizedSet(object):

    def __init__(self):
        self.arr = []
        self.val2idx = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val2idx:
            return False
        self.arr.append(val)
        self.val2idx[val] = len(self.arr)-1
        return True
        
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not val in self.val2idx:
            return False
        self.arr[-1], self.arr[self.val2idx[val]] =  self.arr[self.val2idx[val]], self.arr[-1]
        self.val2idx[self.arr[self.val2idx[val]]] = self.val2idx[val]
        del self.val2idx[val]
        self.arr.pop()
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        return self.arr[random.randint(0, len(self.arr)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
