class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[1])
        max_val = intervals[-1][1]
        indicator = [0]*int(2*max_val+2)
        for start, end in intervals:
            indicator[2*start] += 1
            indicator[2*end+1] -= 1
        running_sum = 0
        start = None
        end = None
        out = []
        for i in range(len(indicator)):
            if start == None and indicator[i] != 0:
                running_sum += indicator[i]
                start = i//2
            elif indicator[i] != 0 and running_sum + indicator[i] == 0:
                end = i//2
                out.append([start, end])
                running_sum = 0
                start = None
                end = None
            else:
                running_sum += indicator[i]
        return out
