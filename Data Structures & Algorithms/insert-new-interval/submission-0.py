class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #完全在新区间左边/右边的部分--原样保留
        #和新区间重叠-》合并成更大的区间
        res = []
        for interval in intervals:
            a, b = interval[0], interval[1]
            start, end = newInterval[0], newInterval[1]
            if b < start:
                res.append(interval)
            elif end < a:
                res.append(newInterval)
                newInterval = interval
            else:
                newInterval = [min(a, start), max(b, end)]
        res.append(newInterval)
        return res
