import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)
#### 获取沪深A股历史K线数据 ####
# 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。“分钟线”不包含指数。
# 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
# 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
rs = bs.query_history_k_data_plus("sz.000036",
    "time,open,high,low,close,volume",
    start_date='2010-01-01', end_date='2022-03-04',
    frequency="5", adjustflag="2")
print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
def Date_list_ALL_A():
    code_A = []
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

#### 结果集输出到csv文件 ####

#print(result)
result['datetime'] = result['time'] #把time变为datetime列
result['date'] = (result['datetime'].astype(str)) #把datetime列数据类型改为str并把列改为date
result['date'] = result['date'].str[:8] #把date列的前8位去除放到date列中并在最后自动生成列
result['time'] = (result['datetime'].astype(str)) #把datetime列数据类型改为str并把列改为time
result['time'] = result['time'].str[8:12] #把time列的前8-12位去除放到time列中并在最后自动生成列
#print(result)
result1 = result.pop('datetime') #删除datetime列并存放在result1中
date = result.pop('date') #删除date列并存放在date中
result.insert(0, 'date',date) #在第一列前插入date列
result.to_csv("F:/BFOS/备份桌面/外汇学习-钻潜交易/A股股池/000036_5M_2010-01-01_2022-03-04.csv", index = False,header = False)
#result.drop(index=0,)
#print(result1)
print(result)
#print(df.dtype)
#df['time'] = df['time'].str[-2:]
#print(df)
#### 登出系统 ####
bs.logout()