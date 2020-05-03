class TreeNode:
    def __init__(self, x):
        self.x = x
        self.y = y
        self.sum = 0
        self.left = None
        self.right = None  
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        N = 10
        self.tree = [0] * (2 * N)  
        self.build_segment_tree(A)
    def build_segment_tree(self,A): 
        n = len(A)
        for i in range(n) :  
            self.tree[n + i] = A[i]
        print self.tree
        # build the tree by calculating parents  
        for i in range(n - 1, 0, -1) :  
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]  
        print self.tree
    def updateTree(index, value):
        self.tree[index + n] = value
        index+=n
        i = index
        while i > 1: 
            self.tree[i//2] = self.tree[i] + self.tree[i+1]
    
    def queryTree(l, r):
        sum = 0
        l += n
        r += n
        while l < r:
            if ((l & 1)>0):
                sum += self.tree[l]
                l += 1
            if ((r & 1)>0):
                r -= 1
                sum += self.tree[r]
            l =l// 2
            r =r// 2
        return sum
obj = Solution()
A   = [ 1, 2, 5, 3, 4 ]
B   = [[4, 2, 4],[3, 3, 0],[1, 6, 0],[4, 3, 5]]
obj.solve(A,B)

# https://www.geeksforgeeks.org/segment-tree-efficient-implementation/
# https://www.codespeedy.com/implement-segment-tree-in-python/