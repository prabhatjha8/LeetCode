import heapq
class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """

        targetStartTime = times[targetFriend][0]

        n = len(times)
        emptyChairs = list(range(n))
        heapq.heapify(emptyChairs)
        endTimeIstoChair = defaultdict(list)

        timeSeq = []
        startIstoEnd = {}
        for time in times:
            timeSeq.append((time[0], "O"))
            timeSeq.append((time[1], "C"))
            startIstoEnd[time[0]] = time[1]

        sortedTimeSeq = sorted(timeSeq)
        
        for item in sortedTimeSeq:

            if item[1] == "C":
                for chair in endTimeIstoChair[item[0]]:
                    heapq.heappush(emptyChairs, chair)
                endTimeIstoChair[item[0]] = []

            else:
                chairAssigned = heapq.heappop(emptyChairs)
                endTimeIstoChair[startIstoEnd[item[0]]].append(chairAssigned)
                if item[0] == targetStartTime:
                    return chairAssigned
            