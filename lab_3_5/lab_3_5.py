'''Generate list with lowercase and uppercase alphabet plus numbers'''
import string
arr = [char for char in string.ascii_uppercase]
arr2 = [char for char in string.ascii_lowercase]
arr3 = [char for char in string.digits]
arr+=arr2+arr3
print(arr)


