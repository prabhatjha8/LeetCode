class Solution:
    def compressedString(self, word: str) -> str:

         comp = ""
         curChar = word[0]
         n = len(word)
         
         i = 1
         curCount = 1
         while i < n:

            if (word[i] == word[i-1]) and (curCount < 9):
                curCount += 1
            
            else:
                comp = comp + str(curCount) + curChar
                curCount = 1
                curChar = word[i]

            i += 1

         comp = comp + str(curCount) + curChar

         return comp

        
        