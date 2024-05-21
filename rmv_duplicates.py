
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        self.nums = list(set(nums))
        print(self.nums)
        print(len(self.nums))
        return len(self.nums)

s = Solution()

s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
s.removeDuplicates([1,1,2])