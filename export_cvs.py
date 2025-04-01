import pandas as pd
from variables import desctn_label_full,no_dash_b_ent,variable_dict,export_csv,\
    entry_normal,entry_disable
from datetime import datetime
from tkinter import messagebox

temp_dict=[]
currnt_date=datetime.now().strftime("%m-%d-%Y")
def export_to_cvs():
    entry_normal()
    value = variable_dict["Date_10"].get()
    if value != "":
        response = messagebox.askyesno("Confirm Export", "Are you sure you want to export this?")
        if response:  # If the user clicks "Yes"

            df=pd.DataFrame(columns=desctn_label_full)
            for column_index,text in enumerate(desctn_label_full):
                for row_index in range(1,no_dash_b_ent+1):
                    temp_dict.append(variable_dict[f"{text}_{row_index}{column_index}"].get())
                df[text]=temp_dict
                temp_dict.clear()
            file_path = f"{export_csv}{currnt_date}.csv"

   #  write data to csv
            df.to_csv(file_path)
            messagebox.showinfo("Message", f"File is saved  {file_path}.")
        else:
            messagebox.showinfo("Cancled", "Cancle data export!")
    else:
        messagebox.showinfo("Empty", "Nothing to Export")


    entry_disable()