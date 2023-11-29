import pandas as pd
import os
import glob
import re
from tushare_utils import get_tushare_pro

def read_tdx_offline_data(csvfile):
    columns = ["date", "open", "high", "low", "close", "amount", "volume"]
    std_code  = re.findall(r'\d+', csvfile)[-1]
    abs_path = os.path.abspath(csvfile)
    print(abs_path)
    df = pd.read_csv(abs_path,
                     encoding="gbk",
                     skiprows=2,
                     header=None)
    df.columns = columns
    df = df.iloc[:-1]
    df['std_code'] = std_code
    df['pct_change'] = df['close'].pct_change()
    df['limit_up'] = ((df['close'] > df['close'].shift(1)) & (df['pct_change'] >= 0.1)) | (
            (df['volume'] > df['volume'].shift(1)) & (df['pct_change'] < 0.1))
    df["ztj"] = df['close'].shift(1) * 1.1
    print(df[['date', 'std_code','close', 'ztj']])

datafilelist = glob.glob(os.path.join('./data/t23-1129/day/hfq/', '*'))
for i in range(2):
    csvfile = datafilelist[1]
    print(datafilelist[1])
    df3 = read_tdx_offline_data(csvfile);



# pro = get_tushare_pro()
#
# df2 = pro.limit_list_d(limit_type='U',
#                        start_data='19901219',
#                        end_data='20231113',
#                        fields='ts_code,trade_date,industry,name,close,pct_chg,open_times,up_stat,limit_times')
#
# # 将日期列转换为datetime类型
# df2['date'] = pd.to_datetime(df2['trade_date'])
#
# # 按照日期升序排序
# df_sorted = df2.sort_values('date')
# print(df_sorted)
