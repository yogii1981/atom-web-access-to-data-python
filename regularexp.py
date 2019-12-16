import re
x = "My 2 favourite numbers are 19 and 42"
y = re.findall ('[0-9]+',x)
print(y)
y= re.findall('[AIEOU]+',x)
print(y)
y= re.findall('[aieou]+',x)
print(y)
y= re.findall('[aie]+',x)
print(y)
y= re.findall('[e]+',x)
print(y)
y= re.findall('[ur]',x)
print(y)
