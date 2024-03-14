class MyClass:
	def __init__(self):
		pass

	@staticmethod
	def get_max_value(x, y):
		#write you code logic !!
		return (max(x, y))

# Create an instance of MyClass
x = int(input())
y = int(input())
obj = MyClass()

res = obj.get_max_value(x,y)
print(res)

# Problem statement
# You are given a Python class MyClass with a static method getmaxvalue that returns the maximum of two given values.
# Sample Input :
# 3
# 4
# Sample Output:
# 4


