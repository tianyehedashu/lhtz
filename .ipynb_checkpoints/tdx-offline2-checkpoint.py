import pandas as pd
from tushare_utils import get_tushare_pro


def read_tdx_offline_data():
    global columns, df, df
    columns = ["date", "open", "high", "low", "close", "amount", "volume"]
    # D:\tdx-data\t23-1128
    stock_code1 = "SH#688408.csv"
    wtkj_code = "SZ#002331.csv"
    print(f"D:/tdx-data/t23-1128/{wtkj_code}")
    df = pd.read_csv(f"D:/tdx-data/t23-1128/{wtkj_code}",
                     encoding="gbk",
                     header=None)
    df.columns = columns
    df = df.iloc[:-1]
    df['pct_change'] = df['close'].pct_change()
    df['limit_up'] = ((df['close'] > df['close'].shift(1)) & (df['pct_change'] >= 0.1)) | (
            (df['volume'] > df['volume'].shift(1)) & (df['pct_change'] < 0.1))
    df["ztj"] = df['close'].shift(1) * 1.1
    print(df[['date', 'close', 'ztj']])


# df = pd.read_csv('D:/soft/tdx/T0002/export/SZ#300100.txt',
#                  skiprows=[0,1],
#                  names=["name", "pc", "pcm","code"])


pro = get_tushare_pro()

df2 = pro.limit_list_d(limit_type='U',
                       start_data='19901219',
                       end_data='20231113',
                       fields='ts_code,trade_date,industry,name,close,pct_chg,open_times,up_stat,limit_times')

# 将日期列转换为datetime类型
df2['date'] = pd.to_datetime(df2['trade_date'])

# 按照日期升序排序
df_sorted = df2.sort_values('date')
print(df_sorted)
