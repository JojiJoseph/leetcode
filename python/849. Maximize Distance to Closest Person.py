class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev_seat = None
        max_dist = 0
        for i, seat in enumerate(seats):
            if seat == 1:
                if prev_seat is None:
                    max_dist = i
                elif i > prev_seat + 1:
                    seats_bw = i - prev_seat - 1
                    if seats_bw % 2 == 1:
                        max_dist = max(max_dist, (seats_bw+1) // 2)
                    else:
                        max_dist = max(max_dist, seats_bw // 2)
                prev_seat = i
        i = len(seats)
        if i > prev_seat + 1:
            max_dist = max(max_dist, i - prev_seat - 1)
        return max_dist
