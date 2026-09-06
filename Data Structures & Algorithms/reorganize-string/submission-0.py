class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = [(-freq,char) for char, freq, in count.items()]
        heapq.heapify(maxheap)
        result = []
        prev = None
        while maxheap or prev:
            if not maxheap and prev:
                return ""
            freq, char = heapq.heappop(maxheap)
            result.append(char)
            freq += 1
            if prev:
                heapq.heappush(maxheap,prev)
                prev= None
            if freq != 0:
                prev = (freq, char)
        return "".join(result)