from math import ceil, sqrt 
class Solution:
    # @param A : integer
    # @return an integer
    # def solve(self, A):
    #     dp = [1000] * 100
    #     for i in range(100):
    #         dp[i] = 1000
    #     dp[0] = 0;
    #     for i in range(1,100):
    #         dp[i] = min(dp[i-1] + 1, dp[i])
            
    #     for i in range(10,100):
    #         dp[i] = min(dp[i-10] + 1, dp[i])
            
    #     for i in range(25,100):
    #         dp[i] = min(dp[i-25] + 1, dp[i])
    #     print dp  
    #     print len(dp)
    #     ans = 0
    #     while(A > 0):
    #         ans += dp[int(A % 100)]
    #         A = A//100
    #     return ans
    # def solve(self, A, B, C):
    #     self.result = []
    #     i = 0;
    #     E = list(C)
    #     D = A
    #     cost = 0
    #     cost1 = 0
    #     while A != 0:
    #         ind = C.index(max(C))
    #         # print C[ind]
    #         cost += C[ind] * 1
    #         # print cost
    #         C[ind] = C[ind] - 1
    #         A -= 1
    #         i += 1
    #     # print(cost)
    #     while D != 0:
    #         # ind = C.index(min(C))
    #         num = min(j for j in E if j > 0)
    #         print(ind)
    #         ind = E.index(num)
    #         cost1 += E[ind] * 1
    #         E[ind] = E[ind] - 1
    #         # E = [k for k in E if k != 0]
    #         # print(cost1)
    #         D -= 1
    #         i += 1
    #     self.result.append(cost)
    #     self.result.append(cost1)
    #     return self.result
    # def main(self,A):
    #     # inp_num = raw_input()
    #     inp_num = A
    #     if inp_num == 0 or inp_num == 1:
    #         return 1
    #     result = 1
    #     first_num = 0
    #     second_num = 1
    #     count = 1
    #     while count < inp_num:
    #         result = first_num + second_num
    #         first_num = second_num
    #         second_num = result
    #         count += 1
    #     print(result)
    #     return 0
    def MaxProductSubarray(self,A):
        A = [[0, 0]]
        result = [[0]*len(A[0]) for i in A]
        if A[0][0] == 0:
            result[0][0] = 1
        for i in range(1,len(A)):
            if A[i][0] == 0:
                result[i][0] = result[i-1][0]
        for i in range(1,len(A[0])):
            if A[0][i] == 0:
                result[0][i] = result[0][i-1]
        for i in range(1,len(A)):
            for j in range(1,len(A[0])):
                if A[i][j] == 0:
                    result[i][j] = result[i-1][j] + result[i][j-1]
        print result
        print result[-1][-1]
        return result[-1][-1]
        # A = [ -6, 12, 10, 28, -14, -35, 42, 28 ]
        # X = -5
        # Y = 14
        # Z = 6

        # x_index  = 0
        # y_index = 0
        # z_index = 0
        # x_max = 0
        # y_max = 0
        # result = 0
        # for i in range(len(A)):
        #     if Z > 0:
        #         z_index = i if A[i] >= A[z_index] else z_index
        #     else:
        #         z_index = i if A[i] < A[z_index] else z_index
        #     if Y > 0:
        #         y_index = i if A[i] >= A[y_index] else y_index
        #         if y_index <= z_index:
        #             y_max = max(y_max, Y * A[y_index])
        #     else:
        #         y_index = i if A[i] < A[y_index] else y_index
        #         if y_index <= z_index:
        #             y_max = max(y_max, Y * A[y_index])
        #     if X > 0:
        #         x_index = i if A[i] >= A[x_index] else x_index
        #         if x_index <= z_index:
        #             x_max = max(x_max, X * A[x_index])
        #     else:
        #         x_index = i if A[i] < A[x_index] else x_index
        #         if x_index <= z_index:
        #             x_max = max(x_max, X * A[x_index])
        # print (A[z_index] * Z) + x_max + y_max
        # print (A[x_index] * X) + (A[y_index] * Y) + (A[z_index] * Z)
        #
obj = Solution()
A = 10
B = 5
A = [ 1, 0, 0, 0, 0, 0, -2, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0, 0, -1, -2, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, -3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, -2, 3, 0, 0, 0, 0, 0, 0, -2, -3, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, -2, 0, 0, 0, 2, -3, 0, 0, 0, 0 ]
D = [2, 3, -2, 4]
A = 100
obj.MaxProductSubarray(A)
# result = obj.solve(A,B,C) 
# result = obj.solve(47) 
# obj.main(4)
# print(result)     
        
