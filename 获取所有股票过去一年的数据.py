import tushare as ts
import datetime
import pandas as pd
pro = ts.pro_api('20231124213221-d996ebbc-c52d-4c6c-bff2-bf4daf5fd33f')
pro._DataApi__http_url = 'http://tsapi.majors.ltd:7000'
# 设置tushare的token
# ts.set_token('20231124213221-d996ebbc-c52d-4c6c-bff2-bf4daf5fd33f')
# pro = ts.pro_api()
# 获取所有股票代码
stock_list = pro.query('stock_basic',
                       exchange='',
                       list_status='L',
                       fields='ts_code,symbol,name,area,industry,list_date')['ts_code'].tolist()

# 初始化一个空的DataFrame，用于存储所有股票的日线数据
all_data = pd.DataFrame()

# 遍历股票代码，获取每只股票去年一年的日线数据
for code in stock_list:
    print(f'正在获取{code}的数据...')
    data = pro.daily(ts_code=code, start_date=f'{pd.Timestamp.now().year - 1}0101', end_date=f'{pd.Timestamp.now().year - 1}1231')
    all_data = pd.concat([all_data,data])

# 将结果保存到CSV文件
all_data.to_csv('all_stocks_daily_data.csv', index=False)
print('数据已保存到all_stocks_daily_data.csv文件中。')

