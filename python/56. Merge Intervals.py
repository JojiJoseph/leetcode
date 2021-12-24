# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort(key = lambda x:x[1])
#         max_val = intervals[-1][1]
#         indicator = [0]*int(2*max_val+2)
#         for start, end in intervals:
#             indicator[2*start] += 1
#             indicator[2*end+1] -= 1
#         running_sum = 0
#         start = None
#         end = None
#         out = []
#         for i in range(len(indicator)):
#             if start == None and indicator[i] != 0:
#                 running_sum += indicator[i]
#                 start = i//2
#             elif indicator[i] != 0 and running_sum + indicator[i] == 0:
#                 end = i//2
#                 out.append([start, end])
#                 running_sum = 0
#                 start = None
#                 end = None
#             else:
#                 running_sum += indicator[i]
#         return out

# New solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        stack = []
        stack.append(intervals[0])
        for i in range(1,len(intervals)):
            if stack[-1][1] < intervals[i][0]:
                stack.append(intervals[i])
            else:
                stack[-1] = [stack[-1][0], max(intervals[i][1], stack[-1][1])]
        return stack
