class OrderedStream:

    def __init__(self, n: int):
        self.arr = [None] * n
        self.idx = 0
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey-1] = value
        to_ret = []
        while self.idx < self.n and self.arr[self.idx] != None:
            to_ret.append(self.arr[self.idx])
            self.idx += 1
        return to_ret
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)