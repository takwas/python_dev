

class Point:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __str__(self):
		return self.to_str()
	
	def to_str(self):
		return "Point: (" + str(self.x) + ", " + str(self.y) + ")"


def print_pnt(point):
	print point.to_str()
