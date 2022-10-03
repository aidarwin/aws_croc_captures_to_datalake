import pandas as pd
from datetime import date
import os
from pathlib import Path

#cur_path = os.path.dirname(__file__)
cur_path=Path(__file__).parents[1]
print(cur_path)

print("full path is:", (str(cur_path)+'\sourcedata\\NT Crocodile Capture Data 2020 and Earlier.csv'))

df_NT_Crocodile_Capture_2020_Earlier=pd.read_csv(str(cur_path)+'\sourcedata\\NT Crocodile Capture Data 2020 and Earlier.csv')
df_NT_Crocodile_Capture_Zones=pd.read_csv(str(cur_path)+'\sourcedata\\NT Crocodile Capture Zones.csv')

today = date.today()

df_date_range=pd.DataFrame({'date':pd.date_range(start='2005-01-01', end='{}'.format(today.strftime("%Y/%m/%d")))})

df_date_range.to_csv(str(cur_path)+'\Outputfiles\datetable.csv', index=False)

print(df_NT_Crocodile_Capture_Zones.T)
df_NT_Crocodile_Capture_Zones=df_NT_Crocodile_Capture_Zones.T

print("post T: ",df_NT_Crocodile_Capture_Zones)

df_NT_Crocodile_Capture_Zones.to_csv(str(cur_path)+'\Outputfiles\\NT_Crocodile_Capture_Zones_T.csv',header=False)
