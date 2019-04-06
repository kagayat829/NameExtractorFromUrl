import pandas as pd
import re
import numpy as np

filename = 'data/boyname_h01_data.csv'
data = pd.read_csv(filename, header=None)
data.columns = ['Number', 'Name', 'Total']

re_katakana = re.compile(r'[\u30A1-\u30F4]+')

for index, row in data.iterrows():
    if re_katakana.fullmatch(row['Name']):
        #print(index)
        data.at[index, 'Name'] = np.nan

data = data.dropna()
data.to_csv('data/boyname_h01_data_formatted.csv', mode='a',index=False)