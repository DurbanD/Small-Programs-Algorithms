def is_prime(num):
#Don't Count 0 or 1, just return False
	if num == 0 or num == 1 or num == -1:
#Print Statement for feedback
		print(f"{num} is not a Prime number.") 
		return False
#Check if the number is negative
	if num < 0:
#Make it positive if so
		num *= -1
#Generate a List of numbers between 2 and num
	for i in range(2,num+1):
#check to see if num is divisible by any of them
		if num % i == 0 and i != num:
#Print Statement for feedback
			print(f"{num} is not a Prime number. It is divisible by {i}") 
#if it is return False
			return False
#If not continue on
	else:
		pass
#Print Statement for feedback
	print(f'{num} is a Prime Number!') 
#Then Return True if it makes it through
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
#Call is_prime with interactivity
print(is_prime(interact))

#Call some absurdly high number as a test
# import random
# print(is_prime(random.randint(0,10**100000)))
