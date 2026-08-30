class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neighbors = defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):

                pattern = word[:j] + "*" + word[j+1:]

                neighbors[pattern].append(word)

        visit = set([beginWord])

        q = deque([beginWord])

        result = 1

        while q:

            for _ in range(len(q)):

                word = q.popleft()

                if word == endWord:
                    return result

                for j in range(len(word)):

                    pattern = word[:j] + "*" + word[j+1:]

                    for neighbor in neighbors[pattern]:

                        if neighbor not in visit:

                            visit.add(neighbor)

                            q.append(neighbor)

            result += 1

        return 0
        