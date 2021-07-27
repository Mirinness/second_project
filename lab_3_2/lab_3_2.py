var1 = True
print(type(var1))
print(var1 is True)
print(var1 is False)
var2 = (var1 or True)
print(var2 is True)
print(var2 is False)
print(var2 is var1)