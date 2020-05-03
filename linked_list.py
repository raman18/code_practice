# # class Node:
# #     def __init__(self, dataval=None):
# #         self.dataval = dataval
# #         self.nextval = None

# # class SLinkedList:
# #     def __init__(self):
# #         self.headval = None

# #     def listprint(self):
# #         printval = self.headval
# #         while printval is not None:
# #             print (printval.dataval)
# #             printval = printval.nextval

# # list = SLinkedList()
# # list.headval = Node("Mon")
# # e2 = Node("Tue")
# # e3 = Node("Wed")

# # # Link first Node to second node
# # list.headval.nextval = e2
# # # Link second Node to third node
# # e2.nextval = e3

# # list.listprint()

# class ListNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.next = None
 
 
# A = ListNode(1)
# A.next = ListNode(0)
# A.next.next = ListNode(9)
# A.next.next.next = ListNode(4)
# A.next.next.next.next = ListNode(8)
# A.next.next.next.next.next = ListNode(0)
# A.next.next.next.next.next.next = ListNode(1)
# A.next.next.next.next.next.next.next = ListNode(2)
 
# num_arr = []
# num = ""
 
# while A:
# 	num = num + str(A.val)
# 	if len(num)==2:
# 		num_arr.append(num)
# 		num=""
# 	A=A.next
 
# num_arr.sort()
 
# print(num_arr)
 
# R = None
# tmp = None
 
# for i in range(0,len(num_arr)):
# 	first, second = int(num_arr[i][0]), int(num_arr[i][1])
# 	if R is None:
# 		R = ListNode(first)
# 		tmp = R
# 	else:
# 		R.next = ListNode(first)
# 		R = R.next
# 	R.next = ListNode(second)
# 	R = R.next
 
# # # return tmp

# R = tmp
# while R:
# 	print(R.next)
# 	print(R.val)
# 	R=R.next

# A = "16"
# if len(A) < 3:
# 	A = "00"+A
# 	# A = A[::-1]
# print A
# A = A[-3:]
# if (int(A) % 8 == 0):
# 	print 1
# print 0

A = "1010110111001101101000"
B = "1000011011000000111100110"
result = ""
str_len_A = len(A)
str_len_B = len(B)
str_len = max(str_len_A,str_len_B)
if str_len_A < str_len_B:
	A = "0"*(str_len_B - str_len_A) + A
elif str_len_B < str_len_A:
	B = "0"*(str_len_A - str_len_B) + B
carry = 0
for i in range(str_len-1,-1,-1):
	if int(A[i]) + int(B[i]) + carry > 1:
		result = "0" + result
		carry = 1
	elif int(A[i]) + int(B[i]) + carry == 1:
		result = "1" + result
		carry = 0
	else:
		result = "0" + result
		carry = 0
print result[0]