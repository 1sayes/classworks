def RMB2Dollar(a,exchange=6):
	print(a/exchange)
RMB2Dollar(5)

def Dollar2RMB(a,exchange=6):
	print(a*exchange)
Dollar2RMB(5)

Dollar2RMB=lambda a:a*6
print(Dollar2RMB(5))
