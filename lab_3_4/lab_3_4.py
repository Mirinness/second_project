import math
'''Generate string with lowercase and uppercase alphabet plus numbers'''
text = "This is the third Laboratory Work"

'''Print 1st symbol of string'''
print(text[0])

'''Print last symbol'''
print(text[-1])

'''Print 3rd from start and 3rd from the end'''
print(text[2], text[-3])

'''Slice first 8 symbols'''
print(text[:8])

'''Print only symbols with index, which divides on 3 without remaining'''
print(text[::3])

'''Print the symbol of the middle of the string text'''
x=len(text)
x=round(x/2)
print(text[x])
'''ще можна так'''
print(text[len(text)//2])

'''Reverse text using slice'''
print(text[::-1])