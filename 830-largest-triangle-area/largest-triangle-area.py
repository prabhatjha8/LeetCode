class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:

        def distance(point1, point2):
            distance_square = ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
            return distance_square**0.5



        def triangle_area(point1, point2, point3):
            d1 = distance(point1, point2)
            d2 = distance(point2, point3)
            d3 = distance(point3, point1)
            s = (d1 + d2 + d3)/2

            ans = (s*max(0, s - d1)*max(0, s - d2)*max(0,s - d3))**0.5
            if isinstance(ans, complex):
                print(f"{ans} is a complex number, and the values are {[s, d1, d2, d3]}")
            return ans

        ans = -1

        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    ans = max(ans, triangle_area(points[i], points[j], points[k]))

        return ans
        