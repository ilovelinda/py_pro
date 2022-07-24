# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import baostock as bs
import pandas as pd

class test:

    def __init__(self):
        self.data_list=[]
        self.rs=None

    def get(self,gpd):
        rs = bs.query_history_k_data_plus(gpd[0],"date,code,open,high,low,close,volume,isST",start_date='2022-01-24', end_date='2022-01-25',frequency="d", adjustflag="2")
        while (rs.error_code == '0') & rs.next():
            self.data_list.append(rs.get_row_data())
            print(rs.get_row_data())
            self.rs=rs

if __name__ == "__main__":

    lg = bs.login()
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)
    rs = bs.query_all_stock(day="2022-01-24")
    te=test()
    i=0
    while (rs.error_code == '0') & rs.next():
        i=i+1
        print(i)
        gpd=rs.get_row_data()
        te.get(gpd)
    result = pd.DataFrame(te.data_list, columns=te.rs.fields)
    result.to_csv("all.csv", index=False)
    bs.logout()