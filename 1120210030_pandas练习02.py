Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list
import pandas as pd
data = [['Google',10],['Runoob',12],['Wiki',13]]
df = pd.DataFrame(data,columns=['Site','Age'])
print(df)
#ndarrays
import pandas as pd
data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
df = pd.DataFrame(data)
print (df)
#dict
import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20,'d':9}]
df = pd.DataFrame(data)
print (df)
#loc
import pandas as pd
data = {"calories": [420, 380, 390],"duration": [50, 40, 45]}
df = pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.loc[2])

data = {"mango": [420, 380, 390],"apple": [50, 40, 45],"pear": [1, 2, 3],"banana": [23, 45,56]}
df = pd.DataFrame(data)
print(df[["apple","banana"]])
