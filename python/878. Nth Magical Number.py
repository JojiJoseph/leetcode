def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)
def lcm(a,b):
    return a*b/gcd(a,b)
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = int(10**9+7)
        lower, upper = 0, n*min(a,b)
        ab = lcm(a, b)
        while lower <= upper:
            mid = (lower + upper) // 2
            candidate = mid//a + mid // b - mid// ab
            if candidate == n:
                return (mid - min(mid%a, mid%b, mid%(ab))) % MOD
            if candidate < n:
                lower = mid + 1
            else:
                upper = mid-1