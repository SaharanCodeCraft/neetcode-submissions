class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = {}

        for card in hand:
            count[card] = count.get(card,0) + 1
        minheap = list(count.keys())
        heapq.heapify(minheap)

        while minheap:
            first = minheap[0]
            for card in range(first, first + groupSize):
                if card not in count:
                    return False
                count[card] -= 1
                if count[card] == 0:
                    if card!= minheap[0]:
                        return False
                    heapq.heappop(minheap)
        return True