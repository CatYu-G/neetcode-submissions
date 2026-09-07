import heapq
class KthLargest:
#加入新数后，把所有数排第，取第K大的,nums.append, nums.sort, nums[-self.k]
    def __init__(self, k: int, nums: List[int]):
        #把nums里面k个数变成最小堆
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
