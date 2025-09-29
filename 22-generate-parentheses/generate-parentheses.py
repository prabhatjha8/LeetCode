class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        left_paren = "("
        right_paren = ")"

        def helper_fn(s, left_paren_count, right_paren_count):

            if left_paren_count + right_paren_count == 2*n:
                ans.append(s)

            elif right_paren_count < left_paren_count:
                helper_fn(s + ")", left_paren_count, right_paren_count + 1)

                if left_paren_count < n:
                    helper_fn(s + "(", left_paren_count + 1, right_paren_count)


            else:
                helper_fn(s + "(", left_paren_count + 1, right_paren_count)

        helper_fn("", 0, 0)

        return ans


            

        