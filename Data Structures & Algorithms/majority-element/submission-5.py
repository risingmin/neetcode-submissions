class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        thres = len(nums) // 2
        counts = {}

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

        for n in counts:
            if counts[n] > thres:
                return n





        