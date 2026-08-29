class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetmap = defaultdict(list)
        self.followmap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append((self.time, tweetId))
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        self.followmap[userId].add(userId)
        minheap = []
        for followeeID in self.followmap[userId]:
            if followeeID in self.tweetmap:
                index = len(self.tweetmap[followeeID]) - 1
                time, tweetID = self.tweetmap[followeeID][index]
                minheap.append((time, tweetID, followeeID , index))
        heapq.heapify(minheap)
        while minheap and len(result) < 10:
            time, tweetID, followeeID, index = heapq.heappop(minheap)
            result.append(tweetID)
            index -= 1
            if index >= 0:
                time, tweetID = self.tweetmap[followeeID][index]
                heapq.heappush(minheap, (time, tweetID, followeeID, index))
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)