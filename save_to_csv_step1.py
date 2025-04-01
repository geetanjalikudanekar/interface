import pandas as pd
import os
from variables import  csv_data_file

def intset_cvs_step1(name,part,po_no,po_qty,shift,currnt_date,currnt_time,cvs_file):
    if os.path.exists(cvs_file):
        df = pd.read_csv(cvs_file)
        print(df)

        # Determine the next Serial Num ber
    if not df.empty:
            next_serial_number = df["S. NO."].max() + 1  # Increment based on the highest Serial Number
    else:
            next_serial_number = 1  # Start from 1 if the DataFrame is empty

    new_data = {"S. NO.":next_serial_number,"Date":currnt_date,"Start":currnt_time,"Name":name,"Part":part,"PO QTY":po_qty,
                "PO No":po_no,"Shift":shift}
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

    # Save the updated DataFrame back to the CSV file
    df.to_csv(cvs_file, index=False)
