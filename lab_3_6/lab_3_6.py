'''create dict with 5 items, where keys will be country name and value - domain name, i.e. {Ukraine:UA}'''
a = {'Ukraine':'UA', 'English':'UK', 'USA':'US', 'Germany':'DE', 'Italy':'IT'}

'''create another dict with 5 items, where values of countries will be keys, and values will be the capitals i.e. {'UA': 'Kiev'}'''
b = {'UA':'Kiev', 'UK':'London', 'US':'Washington', 'DE':'Berlin', 'IT':'Rome'}

'''add one more element to each dict above'''
a.update({'Spain':'ES'})
b.update({'ES':'Madrid'})

'''print sentence "Domain for COUNTRY is DOMAIN." for each record in countries with the replace from dicts'''
for country, domain in a.items():
    print('Domain for {0} is {1}'.format(country, domain))

'''print sentence "The capital of COUNTRY is CAPITAL" for each record in capitals with the replace from dicts'''
for country, capital in b.items():
    print('The capital of {0} is {1}'.format(country, capital))

'''Merge sentences above together with one cycle'''
'''я так зрозумів, що це я зробив уже раніше'''

'''Add to each value of first dict another two domains: COM and GOV'''
cg = ',  COM, GOV'
for i in a.keys():
    a[i]=str(a[i])+cg
print(a)