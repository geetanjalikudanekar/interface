import pandas as pd
import os
from datetime import datetime
from variables import  csv_data_file

def insert_csv_step2(currnt_time,good_part,reworked,QC_OK,hp,lp,inlt,otlt,oth,vlv,PPH_value):
    if os.path.exists(csv_data_file):
        df = pd.read_csv(csv_data_file)

    if pd.isna(df.iloc[-1]["Good Parts"]):
        df.loc[df.index[-1], "Good Parts"] = good_part
        df.loc[df.index[-1], "Reworked"] = reworked
        df.loc[df.index[-1], "QC_OK"] = QC_OK
        df.loc[df.index[-1], "INLT"] = inlt
        df.loc[df.index[-1], "OTLT"] = otlt
        df.loc[df.index[-1], "VLV"] = vlv
        df.loc[df.index[-1], "OTH"] = oth
        df.loc[df.index[-1], "HP"] = hp
        df.loc[df.index[-1], "LP"] = lp
        df.loc[df.index[-1], "End"] = currnt_time
        df.loc[df.index[-1], "PPH"] = PPH_value

  # Save the updated DataFrame back to the CSV file
    df.to_csv(csv_data_file, index=False)