print ("Age Decider")
age = int(input("Enter your age: "))

if age <= 12:
	print("You're a kid!")
    
if age in range(13, 20):
	print("You're a teenager!")
   
else:
	print("You're A Grown-up")
   

# If any of these statements are true
# the corresponding message will be displayed.
# If neither statement is true, the "else"
# message is displayed.