class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.str = list(characters)
        self.pointers = [i for i in range(combinationLength)]
        self.first_time = True
        

    def next(self) -> str:
        if self.first_time:
            self.first_time = False
            return "".join([self.str[idx] for idx in self.pointers])
        lim = len(self.str)-1
        for idx, ptr in enumerate(self.pointers[::-1]):
            if ptr != lim:
                self.pointers[len(self.pointers)-1-idx] += 1
                p = self.pointers[len(self.pointers)-1-idx]
                idx2=len(self.pointers)-1-idx
                for i in range(idx2+1, len(self.pointers)):
                    self.pointers[i] = (i-idx2)+p
                return "".join([self.str[i] for i in self.pointers])
            else:
                lim -= 1
        

    def hasNext(self) -> bool:
        if self.first_time:
            return True
        return self.pointers[0] != len(self.str)-len(self.pointers)
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()