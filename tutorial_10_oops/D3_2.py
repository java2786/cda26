class Mobile:
	platform = None
	ram = None
	storage = None
	ports = None
	charging_port = None
	dimensions = None
 
	def __init__(self, p, r, s):
		self.platform = p 
		self.ram = r 
		self.storage = s 

yourPhone = Mobile("android", 8, 512)

hisPhone = Mobile("keypad", .5, 2)





