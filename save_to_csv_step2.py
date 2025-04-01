import pandas as pd
import os
from datetime import datetime
from variables import  csv_data_file

def insert_csv_step2(currnt_time,good_part,reworked,QC_OK,hp,lp,x1,x2,y2,y1,PPH_value):
    if os.path.exists(csv_data_file):
        df = pd.read_csv(csv_data_file)

    if pd.isna(df.iloc[-1]["Good Parts"]):
        df.loc[df.index[-1], "Good Parts"] = good_part
        df.loc[df.index[-1], "Reworked"] = reworked
        df.loc[df.index[-1], "QC_OK"] = QC_OK
        df.loc[df.index[-1], "X1"] = x1
        df.loc[df.index[-1], "X2"] = x2
        df.loc[df.index[-1], "Y1"] = y1
        df.loc[df.index[-1], "Y2"] = y2
        df.loc[df.index[-1], "HP"] = hp
        df.loc[df.index[-1], "LP"] = lp
        df.loc[df.index[-1], "End"] = currnt_time
        df.loc[df.index[-1], "PPH"] = PPH_value

  # Save the updated DataFrame back to the CSV file
    df.to_csv(csv_data_file, index=False)