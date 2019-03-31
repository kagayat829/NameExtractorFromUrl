import pandas as pd

for i in range(1 ,196):
    if i < 10:
        page = '0' + str(i)
    else:
        page = str(i)
    url = 'http://www.namaejiten.com/h01/boy' + page + '.html'
    dfs = pd.read_html(url, header=1)
    print(url)
    for item in dfs:
        print(item)
        item.to_csv('data/boyname_h01_data.csv', mode='a',index=False)