import pandas as pd
import numpy as np
code_list_list = []
code_list = pd.DataFrame()
code_list = pd.read_excel(r'code.xls')
code_list_list = code_list('���롮)
print(code_list.index)
print(code_list.columns)
