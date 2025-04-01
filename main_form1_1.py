import tkinter as tk
from tkinter import ttk ,messagebox,NS,Canvas,Scrollbar
import csv,os
from datetime import datetime
import pandas as pd
from save_to_csv_step1 import intset_cvs_step1
from save_to_csv_step2 import insert_csv_step2
from dshbord_entry import dshbord_enty_1,dshbord_enty_2
from variables import variable_dict,\
                      desctn_e_w_b,desctn_e_w_s,desctn_e_w_m,desctn_label_full,desctn_lable_font,desctn_entry_font ,\
                      stp12_head_font,stp12_l_w,stp12_l_w1,stp12_e_w_s,stp12_e_w_b,stp12_lable_font,stp12_entry_font,stp12_l_wm,\
                      csv_data_file,cvs_descrptn_file ,no_dash_b_ent,step2_valid
from delete_file_dashbord_entry import dlt_entry_form
from export_cvs import export_to_cvs


def on_exp_btn_clk():
    export_to_cvs()

# Allow only digits or an empty value (to support deleting entries)
def validate_number(value):
    return value.isdigit() or value == ""


def on_del_btn_clk():
    value=variable_dict[f"Date_10"].get()
    if value!="":
        dlt_entry_form()
    else:
        messagebox.showerror("Empty", "Nothing to delete!")

def on_btn1_clk():
    name=name_e.get()
    part= part_e.get()
    po_no=po_no_e.get()
    po_qty = po_qty_e.get()
    shift=shift_e.get()
    currnt_time = datetime.now().strftime("%H:%M:%S")
    currnt_date = datetime.now().strftime('%Y-%m-%d')

    # Validate inputs
    if not name or not part or not po_no or not po_qty or not shift:
        messagebox.showerror("Error", "All fields are required!")
        return

    intset_cvs_step1(name,part,po_no,po_qty,shift,currnt_date,currnt_time, csv_data_file)

    dshbord_enty_1(currnt_date,currnt_time,part,po_no,po_qty)

    global step2_valid
    step2_valid = 1
    # Show success message and clear the form inputs
    messagebox.showinfo("Success", "Data saved successfully!")

    for i in [name_e, part_e, po_no_e, po_qty_e, shift_e]:
        i.delete(0, tk.END)

def on_btn2_clk():
    global step2_valid
    if step2_valid==1:
        good_part=good_part_e.get()
        reworked= reworked_e.get()
        QC_OK=QC_OK_e.get()
        x1 = x1_e.get()
        y1 = y1_e.get()
        x2 = x2_e.get()
        y2 = y2_e.get()
        hp=hp_e.get()
        lp=lp_e.get()
        currnt_time = datetime.now().strftime("%H:%M:%S")

        # Validate inputs
        if not good_part or not QC_OK or not reworked or not x1 or not x2 or not y1 or not y2 or not hp or not lp:
            messagebox.showerror("Error", "All fields are required!")
            return

        dshbord_enty_2(currnt_time,good_part,reworked,QC_OK,hp,lp,x1,x2,y2,y1)

        messagebox.showinfo("Success", "Data saved successfully!")
        for i in [good_part_e,reworked_e,QC_OK_e,x1_e,x2_e,y2_e,y1_e,hp_e,lp_e]:
            i.delete(0, tk.END)
        step2_valid=0

    else:
        messagebox.showinfo("", "Complete Step1 first")
        for i in [good_part_e, reworked_e, QC_OK_e, x1_e, x2_e, y2_e, y1_e, hp_e, lp_e]:
            i.delete(0, tk.END)

# Create the main tkinter window
root = tk.Tk()
root.title("Data Entry Form updated")
root.geometry("800x600")  # Adjust the size
root.state("zoomed")
# root.config(bg="WHITE")
vcmd = (root.register(validate_number), "%P")

# Create a frame to hold widgets
frame_out = tk.Frame(root,bg="white")
frame_out.pack(pady=10)

vcmd = (frame_out.register(validate_number), "%P")

# Create a labeled frame for "Parts Details"
step1 = tk.LabelFrame(frame_out, text="STEP 1",font=stp12_head_font, padx=10, pady=10)
step1.grid(row=0, column=0, padx=10, pady=10)
step1.grid_rowconfigure(3, weight=1)  # Allow row 3 to expand
step1.grid_columnconfigure(0, weight=1)
#



# Row 1: Labels and Entry fields for "Name" and "Parts"
name_l = tk.Label(step1, text="Name",font=stp12_lable_font,anchor="w",width=stp12_l_w1)
name_l.grid(row=0, column=0, sticky="w")
name_e = tk.Entry(step1,font=stp12_entry_font,width=stp12_e_w_b)
name_e.grid(row=0, column=1, columnspan=3,sticky="w")

part_l = tk.Label(step1, text="Part",font=stp12_lable_font,anchor="w",width=stp12_l_w1)
part_l.grid(row=1, column=0,sticky="w")
part_e = tk.Entry(step1,font=stp12_entry_font,width=stp12_e_w_s)
part_e.grid(row=1, column=1,sticky="w")

# Row 2: Labels and Entry fields for "PO QTY" and "PO No"
po_qty_l = tk.Label(step1, text="PO QTY",font=stp12_lable_font,anchor="w",width=stp12_l_w1)
po_qty_l.grid(row=1, column=2, sticky="e")
po_qty_e = tk.Entry(step1,font=stp12_entry_font,width=stp12_e_w_s,validate="key",validatecommand=vcmd)
po_qty_e.grid(row=1, column=3, padx=4, pady=5,sticky="w")

po_no_l = tk.Label(step1, text="PO No",font=stp12_lable_font,anchor="w",width=stp12_l_w1)
po_no_l.grid(row=2, column=0, sticky="w")
po_no_e= tk.Entry(step1,font=stp12_entry_font,width=stp12_e_w_s)
po_no_e.grid(row=2, column=1, padx=4, pady=5,sticky="w")

shift_l = tk.Label(step1, text="Shift",font=stp12_lable_font,anchor="w",width=stp12_l_w1)
shift_l.grid(row=2, column=2, sticky="e")
shift_e=ttk.Combobox(step1,values=["First","Second","Third"],font=stp12_entry_font,width=6)
shift_e.set("First")
shift_e.grid(row=2, column=3, padx=4, pady=5,sticky="w")

# Row 3: Submit button
stp1_btn_submit = tk.Button(step1, text="Start Time",font=("Arial", 12,"bold") ,command=on_btn1_clk)
stp1_btn_submit.grid(row=3,column=2, padx=20,pady=10,sticky="nsew")


# Create a labeled frame for "Parts Details"
step2 = tk.LabelFrame(frame_out, text="STEP 2",font=stp12_head_font,padx=10, pady=10)
step2.grid(row=0, column=1, padx=10, pady=10)

# Step 2 row 1
good_part_l= tk.Label(step2, text="Good Parts",font=stp12_lable_font,anchor="w",width=stp12_l_w)
good_part_l.grid(row=0, column=0, sticky="w")
good_part_e= tk.Entry(step2,font=stp12_entry_font,width=stp12_e_w_s,validatecommand=vcmd,validate="key")
good_part_e.grid(row=0, column=1, padx=4, pady=5)

hp_l = tk.Label(step2, text="HP",font=stp12_lable_font,anchor="w",width=stp12_l_wm)
hp_l.grid(row=0, column=2, sticky="e")
hp_e = tk.Entry(step2,font=stp12_entry_font,width=stp12_e_w_s,validatecommand=vcmd,validate="key")
hp_e.grid(row=0, column=3, padx=4, pady=5)

lp_l = tk.Label(step2, text="LP",font=stp12_lable_font,anchor="w",width=stp12_l_wm)
lp_l.grid(row=0, column=4, sticky="w")
lp_e= tk.Entry(step2,font=stp12_entry_font,width=stp12_e_w_s,validatecommand=vcmd,validate="key")
lp_e.grid(row=0, column=5, padx=4, pady=5)

# Step 2 row 2

reworked_l= tk.Label(step2, text="Reworked",font=stp12_lable_font,anchor="w",width=stp12_l_w)
reworked_l.grid(row=1, column=0, sticky="w")
reworked_e= tk.Entry(step2,font=stp12_entry_font,width=stp12_e_w_s,validatecommand=vcmd,validate="key")
reworked_e.grid(row=1, column=1, padx=4, pady=5)

x1_l = tk.Label(step2, text="X1",font=stp12_lable_font,anchor="w",width=stp12_l_wm)
x1_l.grid(row=1, column=2, sticky="w")
x1_e= ttk.Combobox(step2,values=["7--8","8--9","9--10"],font=stp12_entry_font,width=6)
x1_e.grid(row=1, column=3, padx=4, pady=5)
x1_e.set("0")

x2_l = tk.Label(step2, text="X2",font=stp12_lable_font,anchor="w",width=stp12_l_wm)
x2_l.grid(row=1, column=4, sticky="w")
x2_e= tk.Entry(step2,font=stp12_entry_font,width=stp12_e_w_s,validatecommand=vcmd,validate="key")
x2_e.grid(row=1, column=5, padx=4, pady=5)
x2_e.insert(0,"0")

# Step 2 row 3
QC_OK_l = tk.Label(step2, text="QC_OK",font=stp12_lable_font,anchor="w",width=stp12_l_w)
QC_OK_l.grid(row=2, column=0, sticky="w")
QC_OK_e = tk.Entry(step2,font=stp12_entry_font,width=stp12_e_w_s,validatecommand=vcmd,validate="key")
QC_OK_e.grid(row=2, column=1, padx=4, pady=5)

y1_l = tk.Label(step2, text="Y1",font=stp12_lable_font,anchor="w",width=stp12_l_wm)
y1_l.grid(row=2, column=2, sticky="w")
y1_e= ttk.Combobox(step2,values=["7--8","8--9","9--10"],font=stp12_entry_font,width=6)
y1_e.grid(row=2, column=3, padx=4, pady=5)
y1_e.set("0")

y2_l = tk.Label(step2, text="Y2",font=stp12_lable_font,anchor="w",width=stp12_l_wm)
y2_l.grid(row=2, column=4, sticky="w")
y2_e= tk.Entry(step2,font=stp12_entry_font,width=stp12_e_w_s,validatecommand=vcmd,validate="key")
y2_e.grid(row=2, column=5, padx=4, pady=5)
y2_e.insert(0,"0")


# Row 3: Submit button
stp2_btn_submit = tk.Button(step2, text="End Time", font=("Arial", 12,"bold"),command=on_btn2_clk)
stp2_btn_submit.grid(row=3, column=1, columnspan=2, pady=10)

# Create a labeled frame for "Production Dashboard"
Prodtn_Dshbord = tk.LabelFrame(frame_out, padx=5, pady=10,bg="#C00000")
Prodtn_Dshbord.grid(row=1, column=0, pady=0,columnspan=2,sticky="we")
Prodtn_Dshbord_l= tk.Label(Prodtn_Dshbord, text="Production_Dashboard",bg="#C00000",font=stp12_lable_font,fg="white",anchor="center")
Prodtn_Dshbord_l.grid(row=1,column=0, sticky="nsew")
Prodtn_Dshbord.grid_rowconfigure(0, weight=1)
Prodtn_Dshbord.grid_columnconfigure(0, weight=1)



descrptn_frame = tk.LabelFrame(frame_out, padx=10, pady=10)
descrptn_frame.grid(row=2, columnspan=2, padx=0, pady=0,sticky="ewn")

labels = desctn_label_full
for i, text in enumerate(labels):

    # Add label inside descrptn_frame
    label = tk.Label(descrptn_frame, text=text,font=desctn_lable_font)
    label.grid(row=0, column=i)  # All labels in row 0

    for j in range(1,no_dash_b_ent+1):
        if i == 4:
            width = desctn_e_w_b
        elif i in (0,1,5):
            width =desctn_e_w_m
        else:
            width = desctn_e_w_s
        entry=tk.Entry(descrptn_frame,disabledbackground="white", disabledforeground="black",
                       width=width,font=desctn_entry_font)

        entry.grid(row=j,column=i,pady=10)
        entry.config(state="disabled",)
        variable_dict[f"{text}_{j}{i}"] = entry



delete_btn = tk.Button(frame_out, text="Delete",font=("Arial", 12,"bold"),command=on_del_btn_clk )
delete_btn.grid(row=4, column=1, pady=10)

export_btn = tk.Button(frame_out, text="Export",font=("Arial", 12,"bold"),command=on_exp_btn_clk )
export_btn.grid(row=4, column=0,pady=10)

# Run the application
frame_out.mainloop()
