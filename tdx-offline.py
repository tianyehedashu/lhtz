from mootdx.reader import Reader

# market 参数 std 为标准市场(就是股票), ext 为扩展市场(期货，黄金等)
# tdxdir 是通达信的数据目录, 根据自己的情况修改

reader = Reader.factory(market='std', tdxdir='D:/soft/tdx')

# 读取日线数据

df = reader.daily(symbol='600036')
df.to_csv('../dlt/tdx-offline/600036.csv')
print(df)
print(df.info)

