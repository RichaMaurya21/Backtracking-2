
## Problem1 
#Subsets (https://leetcode.com/problems/subsets/)

class Solution:
    def subsets(self, nums):
        res = []
        def backtrack(start, end, path):
            res.append(path[:])
            for i in range(start, end):
                path.append(nums[i])
                backtrack(i+1, end, path)
                path.pop()

        backtrack(0, len(nums),[])
        return res

nums = [1,2,3]
sol = Solution()
print(sol.subsets(nums))
