def vfunc(a,*b):
	print(type(b))
	for i in b:
		a+=i
	return a
result=vfunc(1,2,3,4)
print(result)
