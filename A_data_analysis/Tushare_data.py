import tushare as ts
ts.set_token('6b3fc3b525d7ca5a145ce14e50d31be7a5469ca2714b30cee822085f')
pro = ts.pro_api()
pro = ts.pro_api('6b3fc3b525d7ca5a145ce14e50d31be7a5469ca2714b30cee822085f')
df = pro.trade_cal(exchange='600000.sz', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')