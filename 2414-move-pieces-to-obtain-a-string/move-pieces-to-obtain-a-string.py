class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        count_start = (0, 0)
        count_target = (0, 0)


        l_pos1 = []
        r_pos1 = []
        l_pos2 = []
        r_pos2 = []
        for i in range(len(start)):
            if start[i] == "L":
                l_pos1.append(i)
            elif start[i] == "R":
                r_pos1.append(i)

            if target[i] == "L":
                l_pos2.append(i)
            elif target[i] == "R":
                r_pos2.append(i)


        start = "".join([i for i in start if i != "_"])
        target = "".join([i for i in target if i != "_"])
        n = len(start)
        m = len(target)

        if n != m:
            return False 

        for i in range(n):
            if start[i] == "L":
                count_start = (count_start[0] + 1, count_start[1])
            else: 
                count_start = (count_start[0], count_start[1] + 1)

            if target[i] == "L":
                count_target = (count_target[0] + 1, count_target[1])
            else: 
                count_target = (count_target[0], count_target[1] + 1)

            if count_start != count_target:
                return False

        for i in range(len(l_pos1)):
            if l_pos1[i] < l_pos2[i]:
                return False

        for i in range(len(r_pos1)):
            if r_pos1[i] > r_pos2[i]:
                return False

        return True




        
        