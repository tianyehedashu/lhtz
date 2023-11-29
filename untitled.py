import glob
import os
import pandas as pd
datafilelist = glob.glob(os.path.join('./data/t23-1129/day/hfq/', '*'))
s = pd.Series(datafilelist);
print(datafilelist[0:2])

s.head(10);
print(s)