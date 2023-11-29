import efinance as ef
import pandas as pd
stock_code = '600519'
df = ef.stock.get_quote_history(stock_code)
df2 = ef.stock.get_quote_history('000518')
df3 = pd.concat([df,df2])
# df = ef.stock.get_quote_history()
print(df3)
print(df3.columns)
#df2 = ef.stock.get_realtime_quotes()
#print(df2.info())