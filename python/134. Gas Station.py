class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        amount = 0
        n = len(gas)
        while i < n:
            amount = 0
            for j in range(i, i + n + 1):
                amount += (gas[j % n] - cost[j % n])
                if amount < 0:
                    amount = -1
                    i = j
                    break
            if amount >= 0:
                return i
            i += 1
                
        return -1
