#coding=gbk
import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取证券信息 ####
rs = bs.query_all_stock(day="2022-03-04")
print('query_all_stock respond error_code:'+rs.error_code)
print('query_all_stock respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
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
#### 结果集输出到csv文件 ####
result.to_csv("all_stock.csv", encoding="gbk", index=False)


#### 登出系统 ####
bs.logout()