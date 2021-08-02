'''Generate two sets with not unique numbers and few symbols'''
a = set('fish164')
b = set('crab154')

'''Print 1st set'''
print(a)

'''Create tuple from intersection of first and second set'''
t = tuple(a) + tuple(b)

'''Create tuple from difference first and second set'''
t2 = a-b
print(t2)

'''Slice first 3 symbols from first tuple'''
print(t[:3])

'''Print only symbols with numbers from second set'''
for i in b:
    if (i.isnumeric())==True:
        print(i)

'''Reverse tuple using slice'''
print(t[::-1])

'''Convert both tuples into list'''
l = list(t) + list(t2)
print(l)