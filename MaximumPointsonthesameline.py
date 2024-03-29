import collections


# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if (len(points)<=2):
            return len(points)
        m = 0 #result value
        for i in range(0, len(points)):
            l = {}  #every time reset the dict
            dup = 1 #count the duplicates
            for j in range(0, len(points)):
                if (points[i].x==points[j].x and points[i].y==points[j].y and i!=j):        
                    dup+=1  #count duplicates
                elif i!=j :
                    if (points[i].x==points[j].x):  #vertical line
                        l['v'] = l.get('v',0) + 1
                    elif (points[i].y==points[j].y): # horizontal line
                        l['h'] = l.get('h',0) + 1
                    else:   #regular slope
                        slope = 1.0*(points[i].y-points[j].y)/(points[i].x-points[j].x)
                        l[slope] = l.get(slope,0)+1
            if (len(l)>0): 
                m = max(m,max(l.values())+dup)
            else: #if all points are duplicates, l is empty.
                m = max(m,dup)
        return m

if __name__ == "__main__":
    print(Solution().maxPoints([Point(), Point(), Point()]))
