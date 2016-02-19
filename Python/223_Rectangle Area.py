class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        totalarea = (C-A)*(D-B) + (G-E)*(H-F)
        # if no overlap
        if C<E or G<A or B>H or D<F:
            return totalarea
        else:
            # calculate the overlapped rectangle
            BLx,BLy = max(A,E),max(B,F)
            TRx,TRy = min(C,G),min(D,H)
            overlap = (TRx-BLx)*(TRy-BLy)
            return totalarea-overlap