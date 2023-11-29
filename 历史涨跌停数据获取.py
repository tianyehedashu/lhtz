
from datetime import datetime, timedelta, time
from time import sleep

import pandas as pd

from tushare_utils import get_tushare_pro

pro = get_tushare_pro()

# yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')

start_date = '2020-01-01'
end_date = pd.Timestamp.now().normalize()
date_range = pd.date_range(start=start_date, end=end_date, freq='D')
next_day = date_range[0]
# 循环调用limit_list_d接口获取涨跌停情况
while next_day <= end_date:
    try:
        # 调用 get_limit_list_d 函数获取数据
        trade_date = next_day.strftime('%Y%m%d')
        print(f'handle {next_day} ... ')
        result = pro.limit_list_d(trade_date=trade_date)
        # result = pro.limit_list_d(trade_date=trade_date,
        #                           fields='ts_code,trade_date,industry,name,close,pct_chg,amount,limit_amount'
        #                                  'float_mv,total_mv,turnover_ratio,fd_amount,first_time,last_time,fd_amount'
        #                                  'open_times,up_stat,limit_times,limit')

        result.to_csv('涨跌停情况统计3.csv', mode='a', header=False, index=False)
        next_day = next_day + timedelta(days=1)
    except Exception as e:
        # 如果出现异常，等待一段时间后再次尝试
        print('Error:', e)
        sleep(10)

    # 将起始日期加1天，以便在下一次循环中获取下一个日期的涨跌停情况
