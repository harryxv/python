"""Lambda Expression/Lambda function
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
"""
# lambda a : a + 10
# lambda a: print(a)

days = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
addPrefix = lambda day: "today is " + day
for day in days:
    print(addPrefix(day))
