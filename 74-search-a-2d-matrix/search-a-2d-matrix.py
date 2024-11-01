class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])

        def rankToCoordinate(rank):
            i, j = divmod(rank, n)
            return (i, j)

        def binarySearch(left, right):
            print("left: ", left)
            print("right: ", right)
            if left > right:
                return False 

            elif left == right:
                i, j = rankToCoordinate(left)
                return (matrix[i][j] == target)

            else:
                mid = (left + right)//2
                i, j = rankToCoordinate(mid) 

                if (matrix[i][j] == target):
                    return True

                elif (matrix[i][j] < target):
                    return binarySearch(mid + 1, right)

                else: 
                    return binarySearch(left, mid - 1)

        return binarySearch(0, m*n-1)



            


        
        