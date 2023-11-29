
import tushare as ts
import pandas as pd
import datetime

from pandas.tseries.offsets import BDay

def get_previous_trading_day():
# 获取当前日期
    today = pd.Timestamp.today()

# 计算前一个交易日
    previous_trading_day = today - BDay(1)

    print("前一个交易日：", previous_trading_day)

    return previous_trading_day.strftime('%Y-%m-%d')

def get_limit_up_stocks():
    previous_trading_day = get_previous_trading_day()
    stock_list = ts.get_today_all()
    limit_up_stocks = []

    for index, row in stock_list.iterrows():
        stock_code = row['code']

        df = ts.get_hist_data(stock_code, start=previous_trading_day, end=previous_trading_day)
        if df is not None and len(df) > 0:
            open_price = df.iloc[0]['open']
            close_price = df.iloc[0]['close']
            if close_price / open_price >= 1.1:
                limit_up_stocks.append(stock_code)

    return limit_up_stocks

if __name__ == '__main__':
    limit_up_stocks = get_limit_up_stocks()
    print("前一个交易日涨停过的股票：", limit_up_stocks)
#tushare库来获取股票数据，首先定义了一个函数`get_previous_trading_day`来获取前一个交易日，然后定义了一个函数`get_limit_up_stocks`来获取前一个交易日涨停过的股票。最后在主函数中调用`get_limit_up_stocks`并打印结果。