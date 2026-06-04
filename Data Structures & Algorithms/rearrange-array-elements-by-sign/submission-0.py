class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0  
        neg = 0  
        arr = []
        for i in range(len(nums) // 2):
            while nums[pos] < 0:
                pos += 1
            while nums[neg] > 0:
                neg += 1
            arr.append(nums[pos])
            arr.append(nums[neg])
            pos += 1
            neg += 1
        return arr