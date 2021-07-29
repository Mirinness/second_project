'''Generate list with lowercase and uppercase alphabet plus numbers'''
import string
arr = [char for char in string.ascii_uppercase]
arr2 = [char for char in string.ascii_lowercase]
arr3 = [char for char in string.digits]
arr+=arr2+arr3
print(arr)

'''Print 1st symbol of list'''
print(arr[0])

'''Print last symbol'''
print(arr[-1])

'''Print 3rd from start and 3rd from the end'''
print(arr[2])
print(arr[-3])

'''Slice first 10 symbols'''
print(arr[0:10])

'''Print only symbols with index, which divides on 2 without remaining'''
print(arr[::2])

'''Print only integer values from list'''
for i in range(len(arr)):
    if type(arr[i])==type(int):
        print(arr[i])

'''Reverse list using slice'''
print(arr[::-1])

