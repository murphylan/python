# coding:utf-8

import pandas as pd
idx = "one two three four".split()
val = range(1, 5)
s = pd.Series(val, index=idx)
# print(s)

s = s.append(pd.Series({"five": 6}))
s = s.append(pd.Series({"six": 7}))
print("append后 ", s)
s.at["six"] = 8 # 修改
print(s)

t = s[s > 5]
print(s)
print(t)



