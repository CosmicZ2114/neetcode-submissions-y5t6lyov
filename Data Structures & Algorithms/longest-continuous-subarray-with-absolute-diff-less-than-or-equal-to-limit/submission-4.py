class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dq = []
        min_dq = []
        max_start = 0
        min_start = 0
        left = 0
        result = 0

        for right in range(len(nums)):
            while max_start < len(max_dq) and nums[max_dq[-1]] <= nums[right]:
                max_dq.pop()
            max_dq.append(right)

            while min_start < len(min_dq) and nums[min_dq[-1]] >= nums[right]:
                min_dq.pop()
            min_dq.append(right)

            while nums[max_dq[max_start]] - nums[min_dq[min_start]] > limit:
                left += 1
                if max_dq[max_start] < left: max_start += 1
                if min_dq[min_start] < left: min_start += 1

            result = max(result, right - left + 1)

        return result