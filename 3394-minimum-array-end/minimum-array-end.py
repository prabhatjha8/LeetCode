class Solution:
    def minEnd(self, n: int, x: int) -> int:
        xBin = bin(x)[2:]
        nBin = bin(n-1)[2:]

        ans = ""
        j = len(nBin) - 1
        for i in range(len(xBin)-1, -1, -1):

            if xBin[i] == "0":
                if j >= 0:
                    ans = nBin[j] + ans
                    j -= 1
                else:
                    ans = "0" + ans
            
            else:
                ans = "1" + ans

        ans = nBin[:j+1] + ans
        return int(ans, 2)





        