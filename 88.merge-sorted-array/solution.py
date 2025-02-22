class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        wPtr = m + n - 1 # writing pointer
        mPtr = m - 1     # reading pointer for nums1
        nPtr = n - 1     # reading pointer for nums2
        
        while mPtr >= 0 and nPtr >= 0:
            if nums1[mPtr] <= nums2[nPtr]:
                nums1[wPtr] = nums2[nPtr]
                nPtr -= 1
            else:
                nums1[wPtr] = nums1[mPtr]
                mPtr -= 1
            wPtr -= 1
        
        while nPtr >= 0:
            nums1[wPtr] = nums2[nPtr]
            wPtr -= 1
            nPtr -= 1
        while mPtr >= 0:
            nums1[wPtr] = nums1[mPtr]
            wPtr -= 1
            mPtr -= 1
   