#[ [], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3], ]
S = [1, 2, 3]
N = 3
r = []
temp_r = []
index  = 0
S.sort()
def subsets(set_inp):
    if set_inp == []:
        return [[]]
    x = subsets(set_inp[1:])
    return sorted( x + [[set_inp[0]] + y for y in x])
print(subsets(S))
# def subsets(s):
# 	# base case
# 	if len(s) == 0:
# 		return [[]]
# 	# the input set is not empty, divide and conquer!
# 	h, t = s[0], s[1:]
# 	print(t)
# 	ss_excl_h = subsets(t)
# 	ss_incl_h = [([h] + ss) for ss in ss_excl_h]
# 	return ss_incl_h + ss_excl_h
 
# print subsets([1, 2, 3])
# def help(index, S,temp_r,r):
# 	if(index == len(S) - 1):
# 		r.append(temp_r)
# 		return r
# 	help(index+1,S,temp_r,r)
# 	print("printing temp_r")
# 	print(temp_r)
# 	temp_r.append(S[index])
# 	print(temp_r)
# 	help(index+1,S,temp_r,r)
# result = help(0,S,temp_r,r)
# print(result)










# def smallestGoodBase(n):    
#     num = int(n)
#     thisLen = int(math.log(num,2)) + 1
#     while thisLen > 2:
#         # from equation [3], we havve
#         thisBase = int(num ** (1.0/(thisLen - 1)))
#         # from equation [2], we have
#         if num * (thisBase - 1) == thisBase ** thisLen - 1:
#             return str(thisBase)
#         thisLen -= 1
#     return str(num - 1)
# result = smallestGoodBase(3)
# print(result)
