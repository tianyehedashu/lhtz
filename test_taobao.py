
##先按照网页示例的代码一行不改试试##先按照网页示例的代码一行不改试试
##需要按照如下代码使用数据接口，您的token已在下方代码设置好

######## 使用方法一 ##############
##!pip install tushare==1.2.89 -i https://pypi.tuna.tsinghua.edu.cn/simple
# 导入tushare
import tushare as ts
# 初始化pro接口
pro = ts.pro_api('20231124213221-d996ebbc-c52d-4c6c-bff2-bf4daf5fd33f')
pro._DataApi__http_url = 'http://tsapi.majors.ltd:7000'

#常规接口
df1 = pro.daily()
print(df1)

#通用行情接口
df2 = ts.pro_bar(api=pro,ts_code='000001.SZ', adj='qfq', start_date='20180101', end_date='20181011')
print(df2)

#股票分钟数据接口,如果您的token不具有分钟权限,这个接口会报错
df3 = pro.stk_mins(ts_code='600519.SH',start_time='2020-11-17 09:30:00',end_time='2020-11-17 15:00:00',freq='5min')
print(df3)

#沪深京实时level1 tick数据接口,如果您的token不具有此权限,这个接口会报错
rt_tick_df = pro.rt_tick(ts_codes=['000001.SH','600519.SH','300750.SZ','510210.SH','832171.BJ','113604.SH','131810.SZ'],fields=[])
#'000001.SH',上证指数,'600519.SH',贵州茅台,'300750.SZ'宁德时代,'510210.SH'上证指数ETF,'832171.BJ'志晟信息,'113604.SH'多伦转债,'131810.SZ'一天期逆回购
rt_tick_df



# 导入mushare
import mushare as ts
# 初始化pro接口
ts.set_token('20231124213221-d996ebbc-c52d-4c6c-bff2-bf4daf5fd33f')
pro = ts.pro_api()

#常规接口
df1 = pro.daily()
print(df1)

#通用行情接口
df2 = ts.pro_bar(ts_code='000001.SZ', adj='qfq', start_date='20180101', end_date='20181011')
print(df2)

#股票分钟数据接口,如果您的token不具有分钟权限,这个接口会报错
df3 = pro.stk_mins(ts_code='600519.SH',start_time='2020-11-17 09:30:00',end_time='2020-11-17 15:00:00',freq='5min')
print(df3)

#沪深京实时level1 tick数据接口,如果您的token不具有此权限,这个接口会报错
rt_tick_df = pro.rt_tick(ts_codes=['000001.SH','600519.SH','300750.SZ','510210.SH','832171.BJ','113604.SH','131810.SZ'],fields=[])
#'000001.SH',上证指数,'600519.SH',贵州茅台,'300750.SZ'宁德时代,'510210.SH'上证指数ETF,'832171.BJ'志晟信息,'113604.SH'多伦转债,'131810.SZ'一天期逆回购
rt_tick_df


