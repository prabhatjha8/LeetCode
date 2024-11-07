class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        n = len(candidates)
        def getBitCount(num):
            s = bin(num)[2:]
            return s

        bitsCountList = [getBitCount(num)[::-1] for num in candidates]
        bitsToLength = {i: len(i) for i in bitsCountList}
        maxPos = max(bitsToLength.values())
        positionIstoOnes = defaultdict(int)
 
        for pos in range(maxPos):
            posCount = 0
            for binaryNum in bitsCountList:
                if (pos < bitsToLength[binaryNum]) and (binaryNum[pos] == "1"):
                    posCount += 1
            positionIstoOnes[pos] = posCount

        return max(positionIstoOnes.values())

                    






        