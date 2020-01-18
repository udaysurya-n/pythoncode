import logging
logging.basicConfig(filename='mylog.txt',level=logging.INFO)
logging.info("A new request came:")
try:
	x=int(input("Enter first number:"))
	y=int(input("Enter second number:"))
	print(x/y)
except ZeroDivisionError as msg:
	print("can't divide with zero")
	logging.exception(msg)
except ValueError as msg:
	print("Enter only int values")
	logging.exception(msg)
logging.info("Request processing completed")