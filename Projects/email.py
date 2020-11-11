class verify(object):
	def __init__(self, string):
		if type(string) is str:
			self.string = string
			self.string_temp = self.string
			self.email_run = False
		else:
			raise ValueError
	def is_website(self):
		if self.email_run != True: self.string_temp = self.string
		if len(self.string_temp) >= 3:
			try:
				lst = self.string_temp.split(".")
				if len(lst) == 1: return False
				for i in lst:
					if i.isalnum() != True:
						return False
					else:
						return True
				else:
					return False
			except AttributeError:
				return False
	def is_email(self):
		if "@" in self.string:
			self.email_run = True
			lst = self.string.split("@")
			self.string_temp = lst[1]
			if self.is_website():
				self.email_run = False
				if lst[0].isalnum():
					return True
			else:
				self.email_run = False
				return False
		return False
		
		
		
def flip(string):
	return string[::-1]# for forward gain repeat this twise
	
	
def cycle(string):
	lst = []
	for i in range(len(string)):
		string = string[1:] + string[0]
		lst.append(string)
	return lst
	
	
def capitalise(string):
	lst = []
	for i in range(len(string)):
		string = string[1:] + string[0].upper()
		lst.append(string)
	return lst
	
	
example = verify(input("enter the test string: "))
print("is an email: ", example.is_email(), "\nis website: ", example.is_website(), "\nflipped: ", flip(example.string))
print('capitalise: ',capitalise(example.string), '\n\n\n')
print('loop: ',cycle(example.string))
x
