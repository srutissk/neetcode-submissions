class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sorting solution
        """
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        arr = []
        for n, cnt in count.items():
            arr.append([cnt, n])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        """

        # min-heap solution
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        heap = []
        for n in count.keys():
            heapq.heappush(heap, (count[n], n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
        