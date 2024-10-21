class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """

        def helper_fn(s, l):
            n = len(s)
            if n == 0:
                return 0
            else:
                ans = 0
                for i in range(1, n+1):
                    subStr = s[:i]
                    if subStr not in l:
                        ans = max(ans, 1 + helper_fn(s[i:], l + [subStr]))
                return ans

        return helper_fn(s, [])

        