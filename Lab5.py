def classify_age (age):
	if age <0:
		print ("Invalid age. Please input a non-negative number.")
	elif 0 <= age <= 12:
		print ("You are a child.")
	elif 13 <= age <= 19:
		print ("You are a teenager.")
	elif 20 <= age <= 64:
		print ("You are an adult.")
	else:
		print ("You are a senior")
		
classify_age (5)
classify_age (10)
classify_age (25)
classify_age (100)