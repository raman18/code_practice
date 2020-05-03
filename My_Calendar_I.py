class Solution:
	def __init__(self):
		self.calendar =  []
	def solve(self, start, end):
		for s, e in self.calendar:
			if s < end and start < e:
				print False
				return False
		self.calendar.append((start,end))
		print self.calendar
		print True
		return True
s = Solution()
start = 25
end   = 32
s.solve(start,end)
start = 26
end   = 35
s.solve(start,end)
start = 19
end   = 25
s.solve(start,end)
