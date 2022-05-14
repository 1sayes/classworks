import re
test='012'
if re.match(r'\d\d\d',test):
    print('ok')
else:
    print('false')

s=re.split(r'\s+','a b   c')
print(s)
s2=re.split(r'[\s\,]+','a,b,,   c')
print(s2)
s3=re.split(r'[\s\,\;]+','a;b,,   c')
print(s3)

s4=re.match(r'^(\d{3})\-(\d{3,8})$','010-134665')
print(s4)
s5=s4.group(0)
ss=s4.group(2)
print(ss)

s6=re.compile(r'^(\d{3})\-(\d{3,8})$')
s7=s6.match('010-12345').groups()
print(s7)
