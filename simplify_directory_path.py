from collections import deque
class Solution:
	def solve(self,A):
		stack = deque()
		temp_stack = deque()
		result_str = "/"
		i = 0
		str_len = len(A)
		while i < str_len:
			dir_name_str = ""
			while i < str_len and A[i] == "/":
				i += 1
			while i < str_len and A[i] != "/":
				dir_name_str += A[i]
				i += 1
			print dir_name_str
			if dir_name_str == "..":
				if(len(stack)):
					stack.pop()
			elif dir_name_str == ".":
				continue
			elif len(dir_name_str) > 0:
				stack.append(dir_name_str)
			i += 1
		print stack
		stack_len = len(stack)
		while stack_len:
			temp_stack.append(stack.pop())
			stack_len -= 1
		temp_stack_len = len(temp_stack)
		while temp_stack_len:
			if temp_stack_len > 1:
				result_str += temp_stack.pop() + "/"
			else:
				result_str += temp_stack.pop()
			temp_stack_len -= 1
		print result_str

 























# from collections import deque
# class Solution:
#  	def solve(self,A):
#  		stack = deque()
#  		str_len = len(A)
#  		str_result = "/"
#  		i = 0 
#  		while i < str_len:
#  			dir_str = ""
#  			while i < str_len and A[i] == "/":
#  				i += 1
#  			while i < str_len and A[i] != "/":
#  				dir_str += A[i]
#  				i += 1
#  			if dir_str == "..":
#  				if len(stack):
#  					stack.pop()
#  			elif dir_str == '.':
#  				continue
#  			elif len(dir_str) > 0:
#  				stack.append(dir_str)
#  			i += 1 
#  		print stack
#  		temp_stack = deque()
#  		stack_len  = len(stack)
#  		print stack_len
#  		while stack_len:
#  			temp_stack.append(stack.pop())
#  			stack_len -= 1
#  		stack_len = len(temp_stack)
#  		while stack_len:
#  			if stack_len > 1:
#  				str_result += temp_stack.pop() + "/"
#  			else:
#  				str_result += temp_stack.pop()
#  			stack_len -= 1
#  		print str_result
s = Solution()
A = "/home/"
A = "/../"
A = "/home//foo/"
A = "/a/./b/../../c/"
s.solve(A)

