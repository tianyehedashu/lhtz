import tushare as ts
import datetime
import pandas as pd
pro = ts.pro_api('20231124213221-d996ebbc-c52d-4c6c-bff2-bf4daf5fd33f')
pro._DataApi__http_url = 'http://tsapi.majors.ltd:7000'
# 设置tushare的token
# ts.set_token('20231124213221-d996ebbc-c52d-4c6c-bff2-bf4daf5fd33f')
# pro = ts.pro_api()

from pandas.tseries.offsets import BDay
# 设置tushare的token
today = pd.Timestamp.today()

# 计算前一个交易日
previous_trading_day = (today - BDay(1)).strftime('%Y%m%d')


# 获取昨天的交易日
trade_date = previous_trading_day

# # 获取昨天的涨停股票
limit_up_stocks = pro.daily(trade_date='20230301',
                             end_data ='20231101',
                             fields='ts_code,trade_date,pre_close,open,high,low,close,pct_chg,vol,amount')
#
print("size is = ")
print(limit_up_stocks.shape[0])

test = limit_up_stocks['ts_code'] == '300497.SZ'

test2 = limit_up_stocks[test]
test2.to_csv("stock_daily_20230101-20201101.csv")
print(test2)
# df = pd.DataFrame(limit_up_stocks)
#

#selected_stocks = df.loc[(df['close'] >= 1.1 * df['pre_close']) & (df['close'].round(2) == df['close'])]

# selected_stocks = df.loc[(
#         df['close'] >= (1.1 * df['pre_close']).round(2) & (df['ts_code'].str.startswith(('60', '00')))
# ) | (df['close'] >= 1.2 * df['pre_close']) & (df['ts_code'].str.startswith('30'))]
# # 获取昨天的涨停股票
print(trade_date)
#df = pro.limit_list_d(trade_date=trade_date, limit_type='U', fields='ts_code,trade_date,industry,name,close,pct_chg,open_times,up_stat,limit_times')
df = pro.limit_list_d(trade_date=trade_date, limit_type='Z', fields='ts_code,trade_date,industry,name,close,pct_chg,open_times,up_stat,limit_times')
print(df)
print(df.index)
df
# print(df[['ts_code', 'trade_date',  'name', 'pct_chg']])
df.to_csv("stock_data.csv",index=False)
# 打印结果





