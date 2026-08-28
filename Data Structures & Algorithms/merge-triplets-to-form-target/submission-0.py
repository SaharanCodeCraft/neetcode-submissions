class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for triplet in triplets:
            if any(triplet[i] > target[i] for i in range(3)):
                continue
            for i in range(3):
                if triplet[i] == target[i]:
                    good.add(i)
        return len(good) == 3