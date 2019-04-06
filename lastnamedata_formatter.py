import pandas as pd
import re
import numpy as np

filename = 'data/lastname_data.csv'
data = pd.read_csv(filename, header=None)
data.columns = ['Number', 'LastName', 'Total']

re_katakana = re.compile(r'[\u30A1-\u30F4]+')
re_hiragana = re.compile(r'^[あ-ん]+$')

for index, row in data.iterrows():
    if re_katakana.fullmatch(row['LastName']) or re_hiragana.fullmatch(row['LastName']):
        print(index)
        data.at[index, 'LastName'] = np.nan

data = data.dropna()
print(data[data.duplicated()])
data.to_csv('data/lastname_data_formatted.csv', mode='a', index=False)
