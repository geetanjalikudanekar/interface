import tkinter as tk
from tkinter import messagebox
from  tkinter import ttk
from variables import desctn_label_full,variable_dict,no_dash_b_ent,\
    entry_disable,entry_normal
from variables import csv_data_file,variable_dict
import pandas as pd
def dlt_entry_form():
          # Create a del window
        entry_normal()
        def del_entries():
            entry_normal()
            del_form.attributes("-topmost", True)
            row_num = int(sel_rw_no_e.get())
            value=variable_dict[f"Date_{row_num}0"].get()
            if value!="":
                response = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this?")
                if response:  # If the user clicks "Yes"
                    date_value = str(variable_dict[f"Date_{row_num}0"].get())
                    Start_value = str(variable_dict[f"Start_{row_num}1"].get())

                    for i in range (row_num,no_dash_b_ent):
                        for index,lables in enumerate(desctn_label_full):
                            if i==7:
                                variable_dict[f"{lables}_{i}{index}"].delete(0, tk.END)
                                variable_dict[f"{lables}_{i}{index}"].insert(0, "")
                                break
                            else:
                                value= variable_dict[f"{lables}_{i+1}{index}"].get()
                                variable_dict[f"{lables}_{i}{index}"].delete(0,tk.END)
                                variable_dict[f"{lables}_{i}{index}"].insert(0,value)

                    def update_csv_file(date_value,Start_value):
                        df=pd.read_csv(csv_data_file)
                        df['Date'] = df['Date'].astype(str)
                        df['Start'] = df['Start'].astype(str)
                        df =df[~((df["Date"]==date_value)&(df["Start"]==Start_value))]
                        df['S. NO.'] = range(1, len(df) + 1)
                        df.columns = [col for col in df.columns if not col.startswith("Unnamed")]
                        df.to_csv(csv_data_file,index=False)


                    update_csv_file(date_value,Start_value)
                    messagebox.showinfo("Success", "Data Deleted successfully!")
                    del_form.destroy()

                else:  # If the user clicks "No"
                    messagebox.showinfo("Deletion Cancled")
            else:
                messagebox.showinfo("Invalid", "Select Valid Row Number!")

            entry_disable()
        del_form = tk.Toplevel()
        del_form.title("delete Form")
        del_form.geometry("300x200")

        del_form.protocol("WM_DELETE_WINDOW",entry_disable())

        # Add widgets to the del window
        sel_rw_no_l = tk.Label(del_form, text="Select Row Number", font=("Arial", 12), anchor="w")
        sel_rw_no_l.grid(row=0, column=0, padx=4, pady=5, sticky="w")
        sel_rw_no_e = ttk.Combobox(del_form, values=["1","2","3","4","5","6","7"], font=("Arial", 12), width=11)
        sel_rw_no_e.set("1")
        sel_rw_no_e.grid(row=0, column=1, padx=4, pady=5)

        close_button = tk.Button(del_form, text="Delete", command=del_entries)
        close_button.grid(row=2, column=0,columnspan=2, padx=4, pady=5)

        # Add a button to open the del form

        # Run the application
        del_form.mainloop()