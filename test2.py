import tushare as ts
import pandas as pd
import datetime

from pandas.tseries.offsets import BDay
# 设置tushare的token
today = pd.Timestamp.today()

# 计算前一个交易日
previous_trading_day = (today - BDay(1)).strftime('%Y-%m-%d')
# previous_trading_day.strftime('%Y-%m-%d')
ts.set_token('443aeefda1c2148045e0cf12a3a561677f4d6b233b049fee355c39a4')
# 初始化pro接口
pro = ts.pro_api()
data = pro.query('stock_basic',  list_status='L',fields='ts_code,symbol,name,area,industry,fullname,enname,cnspell,market,exchange,curr_type,list_date')

stock_code = '000001'  # 股票代码，例如：000001
df = ts.get_hist_data(stock_code)

# 计算涨幅
df['pct_chg'] = (df['close'] - df['pre_close']) / df['pre_close'] * 100

# 筛选出涨停的股票
df_limit_up = df[df['pct_chg'] >= 9.9]

print(df_limit_up[['trade_date', 'open', 'close', 'pct_chg']])

print(df_limit_up[['ts_code', 'symbol', 'name', 'area', 'industry', 'list_date', 'pct_chg']])