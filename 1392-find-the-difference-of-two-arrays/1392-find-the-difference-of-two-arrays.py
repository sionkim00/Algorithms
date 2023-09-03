class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        kvp1 = defaultdict()
        kvp2 = defaultdict()
        res = [[], []]

        for num in nums1:
            kvp1[num] = True
        for num in nums2:
            kvp2[num] = True

        for num in kvp1:
            if not(num in kvp2):
                res[0].append(num)
        for num in kvp2:
            if not(num in kvp1):
                res[1].append(num)
        return res