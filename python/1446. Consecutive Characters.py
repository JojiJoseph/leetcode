class Solution:
    def maxPower(self, s: str) -> int:
        prev = None
        power = 1
        running_power = 1
        for ch in s:
            if ch == prev:
                running_power+=1
            else:
                running_power = 1
            power = max(power, running_power)
            prev = ch
        return power
