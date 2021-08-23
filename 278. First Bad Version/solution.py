# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 0, n-1
        if isBadVersion(1):
            return 1
        while start <= end:
            mid = (start+end)//2
            if not isBadVersion(mid+1) and isBadVersion(mid+2):
                return mid+2
            if not isBadVersion(mid+1):
                start = mid+1
            else:
                end = mid-1