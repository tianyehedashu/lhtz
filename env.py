tushare_token = '443aeefda1c2148045e0cf12a3a561677f4d6b233b049fee355c39a4'

import pandas as pd


from pandas.tseries.offsets import BDay
# 设置tushare的token
today = pd.Timestamp.today()

# 计算前一个交易日
previous_trading_day = (today - BDay(1)).strftime('%Y-%m-%d')