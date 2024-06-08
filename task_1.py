import random
import pandas as pd


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})


data_one_hot = pd.DataFrame()

data_one_hot['robot'] = (data['whoAmI'] == 'robot').astype(int)
data_one_hot['human'] = (data['whoAmI'] == 'human').astype(int)


print(data.head())
print(data_one_hot.head())