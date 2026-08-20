class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0] * len(nums1)
        for i in range(len(nums1)):
            s = nums2.index(nums1[i])
            for j in range(s+1,len(nums2)):
                if nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break
            if res[i] == 0:
                res[i] = -1
        
        return res