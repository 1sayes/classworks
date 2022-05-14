import pandas as pd
df = pd.read_csv('nba.csv',encoding='gbk/')
print(df.to_string())
print(df.head(10))
print(df.info())

import pandas as pd

# 三个字段 name, site, age
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]

# 字典
dict = {'name': nme, 'site': st, 'age': ag}

df = pd.DataFrame(dict)

# 保存 dataframe
df.to_csv('site.csv')
df2=pd.read_csv('site.csv')
print(df2)

import pandas as pd
a = [1, 2, 3]
myvar = pd.Series(a)
print(myvar)

import pandas as pd
a = ["Google", "Runoob", "Wiki"]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print(myvar["y"])·
