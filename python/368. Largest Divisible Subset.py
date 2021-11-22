class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        next = [-1]*n
        count = [0]*n
        count[-1] = 1
        max_idx = n-1
        for i in range(n-2,-1,-1):
            local_max_len = 0
            local_max_idx = -1
            for j in range(i+1, n):
                if nums[j] % nums[i] == 0 and count[j] > local_max_len:
                    local_max_idx = j
                    local_max_len = count[j]
            count[i] = 1 + local_max_len
            next[i] = local_max_idx
            if count[i] > count[max_idx]:
                max_idx = i
        idx = max_idx
        results = []
        while True:
            results.append(nums[idx])
            idx = next[idx]
            if idx == -1:
                break
        return results
            
