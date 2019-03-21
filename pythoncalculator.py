class Calculator:
	def __init__(self,num1,num2):
		self.num1 = num1
		self.num2 = num2
	def getResult(self,operation):
		if operation == "+" :
			return self.num1 + self.num2
		elif operation == "-" :
			return self.num1 - self.num2
		elif operation == "*" :
			return self.num1 * self.num2
		elif operation == "/" :
			return self.num1 / self.num2
		else :
			print("Invalid input")	

num1 = input("enter the first number")
num2 = input("enter the second number")
num1 = int(num1)
num2 = int(num2)
print(num1)
print(num2)
operator = input("enter the operator")
obj = Calculator(num1,num2)
result = obj.getResult(operator)
print("Result = ")
print(result)