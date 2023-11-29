import datetime
import tushare as ts
import pandas as pd
from pandas.tseries.offsets import BDay
# 获取前一个交易日的日期
yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
today = pd.Timestamp.today()

# 计算前一个交易日
previous_trading_day = today - BDay(1)
# 设置tushare的token

ts.set_token('443aeefda1c2148045e0cf12a3a561677f4d6b233b049fee355c39a4')
pro = ts.pro_api()

# 查询前一个交易日的涨停价格
df = pro.daily(trade_date=yesterday)
test = df['pct_chg']
limit_up_price = df[df['pct_chg'] >= 9.9].iloc[0]['close']

# 添加涨停日期和股票代码到backtrace信息中
backtrace = f"涨停日期：{yesterday},股票代码：000001.SZ,涨停价格：{limit_up_price}"
print(backtrace)
