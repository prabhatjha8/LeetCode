class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str1)
        m = len(str2)
        if n < m:
            return False

        alphabets = "abcdefghijklmnopqrstuvwxyz"
        nextAlphabet = dict(zip(list(alphabets), list(alphabets[1:]) + ["a"]))
        ls = [(str1[i], nextAlphabet[str1[i]]) for i in range(len(str1))]
        print("ls: ", ls)

        def helper_fn(ls, s):
            if s == "":
                return True
            elif ls == []:
                return False
            else:
                n = len(ls)
                m = len(s)
                i = 0
                j = 0
                while i <= n and j <= m:
                    if j == m:
                        return True 

                    elif i == n:
                        return False
                    
                    else:
                        if s[j] in ls[i]:
                            j += 1
                            i += 1
                        else:
                            i += 1

        return helper_fn(ls, str2)

        