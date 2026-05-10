class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # just search the lement using binary search and return if it matched if not there then store the value in the end where the mid is present there the tarrget should be placed
        res = len(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res