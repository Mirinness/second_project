'''Generate list with lowercase and uppercase alphabet plus numbers'''
arr = ["test", 2, 6, 5, 9, 10, "A", "B", "C", "d", "e", "f"]
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
for i in arr:
    if type(i) == int:
        print(i)

'''Reverse list using slice'''
print(arr[::-1])

'''Convert base list into string'''
str = ', '.join(map(str, arr))
print(str)