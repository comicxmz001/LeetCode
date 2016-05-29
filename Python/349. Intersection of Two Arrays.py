class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # NOT a subarray! Just need to find duplicated elements (unique)
        # hashtable/hashset is apperently the ideal choice for finding something unique
        # otherwise, we could use sort the two arrays and use two pointers etc.
        return list(set(nums1)&set(nums2))