import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        heap = []
        for num, freq in d.items():
            heapq.heappush(heap, (-freq, num))
        result = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            result.append(num)
        return result