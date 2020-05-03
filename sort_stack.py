from collections import deque
class Solution:
    # @param A : list of integers
    # @return a list of integers
    # def solve(self, A):
    #     temp_stack = deque()
    #     while len(A) != 0:
    #         print A
    #         tmp = A.pop()
    #         print 
    #         while len(temp_stack) != 0 and temp_stack[-1] > tmp:
    #             print temp_stack
    #             A.append(temp_stack.pop())
    #         temp_stack.append(tmp)
    #     print temp_stack
    #     return temp_stack
        def insertAtBottom(self,stack, item): 
            if isEmpty(stack): 
                push(stack, item) 
            else: 
                temp = pop(stack) 
                insertAtBottom(stack, item) 
                push(stack, temp) 
  
        # Below is the function that  
        # reverses the given stack 
        # using insertAtBottom() 
        def reverse(self,stack): 
            if not isEmpty(stack): 
                temp = pop(stack) 
                reverse(stack) 
                self.insertAtBottom(stack, temp) 
s = Solution()
A = [5, 4, 3, 2, 1]
s.reverse(A)
A = [ 66, 96, 43, 28, 14, 1, 41, 76, 70, 81, 22, 11, 42, 78, 4, 88, 70, 43, 90, 6, 12 ]
# s.solve(A)