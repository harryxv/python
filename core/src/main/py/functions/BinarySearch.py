# if elif else  to define conditional
"""
This example demonstrate:
function definition: def function():
while loop
for_in loop
if/elif/else
return statement
List structure
print()
"""


def binary_search(day, days):
    left, right = 0, len(days)
    while left <= right:
        mid = left + int((right - left) / 2)
        if day == days[mid]:
            return mid
        elif day < days[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


days = ['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']

# for loop
for day in days:
    print(day)

print(binary_search('MONDAY', days))  # ->1
