class Solution:
    def gcd(self, a,b):
        if a == 0:
            return b
        return self.gcd(b % a, a)
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hashtable = {}
        for item in deck:
            if item in hashtable:
                hashtable[item] += 1
            else:
                hashtable[item] = 1
        gcd = hashtable[deck[0]]
        if gcd < 2:
            return False
        groups = 0
        for key in hashtable:
            gcd = self.gcd(gcd, hashtable[key])
        return gcd >= 2
