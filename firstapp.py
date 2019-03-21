# import pythoncalculator
# print("Python learning ")

# a = 10
# b = 20
# print(a+b)

# operator = {
# 			"name" : "subash",
# 			"age" : 23,
# 			"address" : "banglore"
# 			}

# print(type(operator))			
# print(operator)
class ClassName:
	def __init__(self, arg):
		print(arg)
	# def mymeth(self):
	#     print(self.arg)


obj = ClassName("python programming")
# obj.mymeth()

class Student:
	def __init__(self, username, password):
		self.username = username
		self.password = password
	def getValue(self):
		print("username = " + self.username  + "\n" + "password = " + self.password)
obj2 = Student("subash", "tharu")
obj2.getValue()

