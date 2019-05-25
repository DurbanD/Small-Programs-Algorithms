def is_prime(num):
#Don't Count 0 or 1, just return False
	if num == 0 or num == 1 or num == -1:
		print(f"{num} is not a Prime number.") #Print Statement for feedback
		return False
#Check if the number is negative
	if num < 0:
#Make it positive if so
		num *= -1
#Generate a List of numbers between 2 and num
	for i in range(2,num+1):
#check to see if num is divisible by any of them
		if num % i == 0 and i != num:
#if it is return False
			print(f"{num} is not a Prime number. It is divisible by {i}") #Print Statement for feedback
			return False
#If not continue on
	else:
		pass
#Then Return True if it makes it through
	print(f'{num} is a Prime Number!') #Print Statement for feedback
	return True


#Interactive Function
def interact():
#Open a Loop to Force Answers
	while True:
#Asks for a Number
		try:
			num = int(input("Please Enter a Number: "))
#Returns that Number for future use
			return num
#Make Sure it's a Number
		except (IndexError, ValueError):
#If Not, Print an Error Message
			print("Invalid Input")

#Call Interactive Function
interact = interact()
#Use it with the Prime Checker
print(is_prime(interact))

# print(is_prime(0))
#Call some absurdly high number as a test
# import random
# print(is_prime(random.randint(0,10**100000)))
