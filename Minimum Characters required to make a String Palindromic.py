class Solution:
        # @param A : string
        # @return an integer
        def solve(self,A):
                arr_len = len(A)
                if arr_len == 0:
                        return
                j = arr_len - 1
                targetA = None
                targetB = None
                print j
                while j > 0:
                        if A[j - 1] > A[j]:
                                if targetA is None:
                                        targetA = j
                                        j -= 1
                                        continue
                                if targetB is None:
                                        targetB = j - 1
                        if targetA is not None and targetB is not None:
                                print targetA
                                print targetB
                                A[targetA], A[targetB] = A[targetB],A[targetA]
                                break
                        j -= 1
                print(targetA)
                print(targetB)
                print A


        # def solve(self, A):
        #         A = A[::-1]
        #         print A
        #         str_len = len(A)
        #         count = 0
        #         for i in range(str_len-2,-1,-1):
        #         	if A[i] == A[i+1]:
        #         		continue
        #         	else:
        #         		count += 1
        #         print count
        #         return count
S = Solution()
A = "ABC"
A = "xgg"
A = [10, 20, 60, 40, 50, 30, 70]
S.solve(A)
# self.parent = TreeNode(-float('inf'))
#     self.first = True
#     def recoverTree(self, root: TreeNode) -> None:
#         def recover(root, arr):
#             if not root:
#                 return
#             recover(root.left, arr)
#             if root.val <= self.parent.val:
#                 if self.first:
#                     arr[0] = self.parent
#                     self.first = False
#                 arr[1] = root
#             self.parent = root
#             recover(root.right, arr)

#         arr = [None, None]
#         recover(root, arr)
#         arr[0].val, arr[1].val = arr[1].val, arr[0].val
#         