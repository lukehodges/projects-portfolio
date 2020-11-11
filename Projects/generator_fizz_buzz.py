
class fizz_buzz:
	def __init__(self,num):
		self.num = int(num)
	def __iter__(self):
		cur = 1
		for i in range(self.num):
			yield [i, self.test(i)]
	def test(self, number):
		ans = ''
		if number % 3 == 0: ans = ans+ 'fizz'
		if number % 5 == 0: ans = ans+ 'buzz'
		if len(ans) == 0: ans = number
		return ans
		
for i in fizz_buzz(23):
	print(i)
