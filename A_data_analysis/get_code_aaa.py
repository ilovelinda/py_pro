#coding=gbk
import baostock as bs
import pandas as pd

#### ��½ϵͳ ####
lg = bs.login()
# ��ʾ��½������Ϣ
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### ��ȡ֤ȯ��Ϣ ####
rs = bs.query_all_stock(day="2022-03-04")
print('query_all_stock respond error_code:'+rs.error_code)
print('query_all_stock respond  error_msg:'+rs.error_msg)

#### ��ӡ����� ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # ��ȡһ����¼������¼�ϲ���һ��
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
#print(result.columns.values)
#print(result.index.values)
#print(result.dtypes)
result = result.applymap(str)
#print(result.dtypes)
result['code'] = result['code'].astype(str)
result['tradeStatus'] = result['tradeStatus'].astype(str)
result['code_name'] = result['code_name'].astype(str)
#result['code'] = result['code'].str[3:9]
#print(result.dtypes)
print(result)
#print(result('code'))
#### ����������csv�ļ� ####
result.to_csv("all_stock.csv", encoding="gbk", index=False)


#### �ǳ�ϵͳ ####
bs.logout()