import pandas as pd
from numpy import sqrt,sum
a=pd.Series([5,4,3,2,1])
b=pd.Series([10,9,8,7,6])
dist=sqrt(sum([(x-y)**2 for x,y in zip(a,b)]))
print(dist)