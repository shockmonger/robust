#robust#

##ASSERTION - always only checks something which is boolean

#1 '''assert True == True'''
#means that an alarm is raised by the program  at the assertion error, 
#and that means that it will stop running thereafter
#if assert is true, program just goes to the next line.


#2
'''def mean(num_list):
	return sum(num_list)/len(num_list)'''
#what if list is empty? Then it'll try to devide by zero

#users will always use something that is unexpected


#MAIN PROGRAM IS ALWAYS AS SHORT AS POSSIBLE

# def mean(num_list):
# 	assert len(num_list) > 2
# 	return sum(num_list)/len(num_list)


#WHAT IF you passed a string?

#Exception is even more sophisticated than assert

'''def mean(num_list):
	if len(num_list) ==0:
		raise Exception('what the fuck')
	return sum(num_list)/len(num_list)'''

#THE FIRST STEP YOU THINK ABOUT IS WHAT IS STANDARD BEHAVIOR - CHECK FOR WHAT WILL COMPUTE WRONG VALUES / EMPTY STRINGS LISTS ETC
#SECOND STEP IS TO CHECK WHAT ARE THE STUPID THINGS THAT THE USER CAN DO?
#WHEN IT IS UNSTANDARD, THEN IT IS BETTER TO RAISE EXCEPTIONS

#write a valuable message for users

def mean(num_list):
	try:
		return sum(num_list)/len(num_list)
	except ZeroDivisionError as detail:
		msg = 'why have you given me an empty list?'
		raise ZeroDivisionError(detail.__str__()+msg)
	except TypeError as detail:
		raise TypeError(detail.__str__()+' type error')

