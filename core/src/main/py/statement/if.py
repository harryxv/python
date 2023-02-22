# if elif else  to define conditional

def binary_search(day, days):
    left, right = 0, len(days)
    while left <= right:
        mid = left + (right - left) / 2
        if (day == days[mid]):
            return mid
        elif (day < days[mid]):
            right = mid - 1
        else:
            left = mid + 1
    return -1


days = ['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']
print(binarySearch('MONDAY', days))  # ->1
