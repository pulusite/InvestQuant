class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

    def midian(self,A,B):
        m,n=len(A),len(B)
        if m>n:
            A,B,m,n=B,A,n,m
        if n==0:
            raise ValueError

        imin,imax,half=0,m,(m+n+1)/2
        while imin<imax:
            i=(imin+imax)/2

