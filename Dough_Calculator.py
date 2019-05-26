#Version Check Import
from sys import version_info
#Set vernum as a usable variable
vernum = float(version_info.major) + float(version_info.minor*0.1)
##Check the Version and Spit out a Warning if Version is Less than 3.0
if vernum <= 3:
	print("WARNING: This Program May Break if Python 3 or Greater is not used. Current Version of Python is %s"%vernum)

###Function to make interactive
def interact():
#Asks for Flour in Grams
	while True:
		try:
			flourweight = float(input("Please Enter Flour Weight in Grams: "))
			break
#Int/float Check
		except (IndexError, ValueError, NameError):
#If Not Int, Print Error
			print("Invalid Input")
#Ask for the Hydration Goal
	while True:
		try:
			percentwater = float(input("Please enter desired hydration % (Water, Milk): "))
			break
#Int/float Check
		except (IndexError, ValueError, NameError):
#If Not Int, Print Error
			print("Invalid Input")
#Ask for the fat Goal
	while True:
		try:
			percentfat = float(input("Please enter desired fat % (Oil, Butter): "))
			break
#Int/float Check
		except (IndexError, ValueError, NameError):
#If Not Int, Print Error
			print("Invalid Input")
#Ask for the sugar Goal
	while True:
		try:
			percentsugar = float(input("Please enter desired sugar % (Honey, Sugar): "))
			break
#Int/float Check
		except (IndexError, ValueError, NameError):
#If Not Int, Print Error
			print("Invalid Input")
#Ask for the salt Goal
	while True:
		try:
			percentsalt = float(input("Please enter desired salt %: "))
			break
#Int/float Check
		except (IndexError, ValueError, NameError):
#If Not Int, Print Error
			print("Invalid Input")
#Ask for the Yeast Goal
	while True:
		try:
			percentyeast = float(input("Please enter desired yeast %: "))
			break
#Int/float Check
		except (IndexError, ValueError, NameError):
#If Not Int, Print Error
			print("Invalid Input")
#Returns the Values
	return flourweight,percentwater,percentfat,percentsugar,percentsalt,percentyeast
interact = interact()


#Function to Create an Ingredient List for given bakers math
#Take weight of flour in grams, % of water, fat, sugar, salt, and yeast
def ingredients(flourweight,percentwater,percentfat,percentsugar,percentsalt,percentyeast):
#Find the weight in grams per given % of flourweight
    fatweight = int((percentfat * 0.01) * flourweight)
    waterweight = int((percentwater * 0.01) * flourweight)
    sugarweight = int((percentsugar * 0.01) * flourweight)
    saltweight = int((percentsalt * 0.01) * flourweight)
    yeastweight = float((percentyeast * 0.01) * flourweight)
    #Print Ingredient List
    print("\n\nFor %s"%flourweight+" Grams of Flour: \n" +
    	"%s"%waterweight+"g Water or Milk"+" (%s"%percentwater+"%) \n" + 
    	"%s"%fatweight+"g Fat or Oil"+" (%s"%percentfat+"%) \n" + 
    	"%s"%sugarweight+"g Sugar or Honey"+" (%s"%percentsugar+"%) \n" + 
    	"%s"%saltweight+"g Salt"+" (%s"%percentsalt+"%) \n" + 
    	"%s"%yeastweight+"g Yeast"+" (%s"%percentyeast+"%) \n")

ingredients(interact[0], interact[1], interact[2], interact[3], interact[4], interact[5])

###Function to print result to a file
