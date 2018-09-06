# Implement a menu based  program for Arithemetic Calculator*/

def add(a,b):
	return a+b;
def sub(a,b):
	return a-b;
def mul(a,b):
	return a*b;
def div(x,y):
	return x/y;

num1=int(input("enter first number"))
num2=int(input("enter the second number"))
print("enter the operation")
operation=input("enter\n 1 for add \n 2 for sub\n 3 for \n 4 for div\n 5 for mod\n")
if (operation=='1'):
	print("addition of numbers is:",add(num1,num2))
elif (operation=='2'):
	print("subtaction of numbers is:",sub(num1,num2))
elif (operation=='3'):
	print("multiplicaton of numbers is",mul(num1,num2))
elif (operation=='4'):
	print("division of numbers is",div(num1,num2))

