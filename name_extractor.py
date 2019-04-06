import pandas as pd

for i in range(1, 22):
    if i < 10:
        year = '0' + str(i)
    else:
        year = str(i)
    for j in range(1, 1000):
        if j < 10:
            page = '0' + str(j)
        else:
            page = str(j)
        url = 'http://www.namaejiten.com/h' + year + '/boy' + page + '.html'
        dfs = pd.read_html(url)
        # print(url)
        for item in dfs:
            #print(item)
            if sum(x < 2 for x in item['件数']) > 0:
                item_moremin = item[item['件数'] > 2]
                item_moremin.to_csv('data/boyname_data_h' + year + '.csv',
                                    mode='a', index=False, header=0)
                print('Proceed next year')
                break
            item.to_csv('data/boyname_data_h' + year + '.csv',
                        mode='a', index=False, header=0)
        else:
            continue
        break
print('End process')
