import traceback
import dill
class library(object):
	def __init__(self, name, description="", max_count=None):
		self.name = name
		self.description = description
		self.max_count = max_count
		self.book_shelf = []
		self.users = []
		self.file_name = name
		
		
	def read_file(self):
		file_name = self.file_name
		try:
			self.file = dill.load( open( file_name, "rb" ) )
			if input("do you want to continue?Y/N\n: ").upper() == 'Y':
				for i in depickle(self.file_name):
					self.name = i.name
					self.description = i.description
					self.max_count = i.max_count
					self.book_shelf = i.book_shelf
					self.users = i.users
		                
		except FileNotFoundError:
			if input("File Not Found Would you like to add a directory?Y/N\n> ").upper() == 'YES' or 'Y':
				self.file_name = input('please enter the file address\n> ')
			
	def save_object(obj, file_name):
		self.file_name = file_name
		with open(file_name, 'wb') as output: 
			dill.dump(obj, output, dill.HIGHEST_PROTOCOL)
			
			
	def add_book(self,book_name, ISBN, Description=None, Author=None):
		adding = book(book_name, ISBN, Description, Author)
		self.book_shelf.append({ISBN : adding})
		print(self.book_shelf, '\n', adding)
	def find_book(self,ISBN):
		for i in self.book_shelf:
			for z in i.keys():
				if z == ISBN:
					for v in i.values():
						if isinstance(v, book):
							print('book has been found')
							print('name : %s\nauthor : %s\nDescription : %s\nISBN : %s' % (v.book_name, v.Author, v.Description, v.ISBN))
							return v
	def remove_book(self,ISBN):
		self.book_shelf.remove(self.find_book(ISBN))
		print(self.book_shelf)
	def add_user(self,name,year=None, admin=False):
		id_num = len(self.users)+1
		self.users.append({id_num : user(id_num,name,year,admin)})
		print(self.users)
		
	def find_user(self, id_num):
		for i in self.users:
			for z in i.keys():
				if z == id_num:
					for v in i.values():
						if isinstance(v, user):
							print('book has been found')
							print('name : %s\nyear : %s\nadmin : %s\nID : %s' % (v.name, v.year, v.admin, v.id_num))
							return v
	def remove_user(self,id_num):
		self.users.remove(index(id_num))
		
		print(self.users)
		
class book(library):
	def __init__(self, book_name, ISBN, Description=None, Author=None):
		self.book_name = book_name
		self.ISBN = str(ISBN)
		self.Description = Description
		self.Author = Author
		
def depickle(file_name):
	with open(file_name, "rb") as f:
		        while True:
		            try:
		                yield dill.load(f)
		            except EOFError:
		                break
		                

class user(library):
	def __init__(self,id_num, name,year=None, admin=False,):
		self.name = name
		self.year = year
		self.admin = admin
		self.id_num = str(id_num)
	
rgs = library("RoyalGrammarSchool", 'library at the royal grammar school in high wycombe')

# add user
#rgs.add_user('tom', 10)# name, year, admin Perms
rgs.add_book('python basics',111_333_444_552,'descrition of book', 'name of author')
rgs.add_user('tom',10,False)
