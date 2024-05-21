from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = dict()
        lst = []
        n = len(nums)
        for i in nums:
            if res.get(i, 0) == 0:
                res[i] = 1
            else:
                res[i] = res[i] + 1
        for i in res.keys():
            for j in range(min(2, res[i])):
                lst.append(i)
        nums[:len(lst)] = lst
        for i in range(len(lst), n):
            nums[i] = n+1
        print(nums)
        return len(lst)

nums = [1,1,1,2,2,3]

s = Solution()
s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
s.removeDuplicates([1,1,2])
s.removeDuplicates(nums)