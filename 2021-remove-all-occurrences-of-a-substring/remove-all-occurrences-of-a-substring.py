class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        m = len(part)

        def removeFirstPart(s, part):
            window = s[:m]
            j = m - 1
            while (j < len(s)-1) and (window != part):
                j += 1
                window = window[1:] + s[j]
            if window == part:
                return s[:j + 1 - m] + s[j + 1:]
            return s

        while removeFirstPart(s, part) != s:
            s = removeFirstPart(s, part)
            print(s)

        return s



        

        
            

            
            


        