[1mdiff --git a/main_form1_1.py b/main_form1_1.py[m
[1mindex e71abcd..33d95ef 100644[m
[1m--- a/main_form1_1.py[m
[1m+++ b/main_form1_1.py[m
[36m@@ -6,10 +6,12 @@[m [mimport pandas as pd[m
 from save_to_csv_step1 import intset_cvs_step1[m
 from save_to_csv_step2 import insert_csv_step2[m
 from dshbord_entry import dshbord_enty_1,dshbord_enty_2[m
[31m-from variables import variable_dict,\[m
[31m-                      desctn_e_w_b,desctn_e_w_s,desctn_e_w_m,desctn_label_full,desctn_lable_font,desctn_entry_font ,\[m
[31m-                      stp12_head_font,stp12_l_w,stp12_l_w1,stp12_e_w_s,stp12_e_w_b,stp12_lable_font,stp12_entry_font,stp12_l_wm,\[m
[31m-                      csv_data_file,cvs_descrptn_file ,no_dash_b_ent,step2_valid[m
[32m+[m[32mfrom variables import variable_dict, \[m
[32m+[m[32m    desctn_e_w_b, desctn_e_w_s, desctn_e_w_m, desctn_label_full, desctn_lable_font, desctn_entry_font, \[m
[32m+[m[32m    stp12_head_font, stp12_l_w, stp12_l_w1, stp12_e_w_s, stp12_e_w_b, stp12_lable_font, stp12_entry_font, stp12_l_wm, \[m
[32m+[m[32m    csv_data_file, cvs_descrptn_file, no_dash_b_ent, step2_valid, \[m
[32m+[m[32m    shift_deflt,oth_deflt,vlv_deflt,inlt_deflt,otlt_deflt[m
[32m+[m
 from delete_file_dashbord_entry import dlt_entry_form[m
 from export_cvs import export_to_cvs[m
 [m
[36m@@ -52,8 +54,9 @@[m [mdef on_btn1_clk():[m
     # Show success message and clear the form inputs[m
     messagebox.showinfo("Success", "Data saved successfully!")[m
 [m
[31m-    for i in [name_e, part_e, po_no_e, po_qty_e, shift_e]:[m
[32m+[m[32m    for i in [name_e, part_e, po_no_e, po_qty_e]:[m
         i.delete(0, tk.END)[m
[32m+[m[32m    shift_e.set(shift_deflt)[m
 [m
 def on_btn2_clk():[m
     global step2_valid[m
[36m@@ -61,30 +64,34 @@[m [mdef on_btn2_clk():[m
         good_part=good_part_e.get()[m
         reworked= reworked_e.get()[m
         QC_OK=QC_OK_e.get()[m
[31m-        x1 = x1_e.get()[m
[31m-        y1 = y1_e.get()[m
[31m-        x2 = x2_e.get()[m
[31m-        y2 = y2_e.get()[m
[32m+[m[32m        inlt = inlt_e.get()[m
[32m+[m[32m        vlv = vlv_e.get()[m
[32m+[m[32m        otlt = otlt_e.get()[m
[32m+[m[32m        oth = oth_e.get()[m
         hp=hp_e.get()[m
         lp=lp_e.get()[m
         currnt_time = datetime.now().strftime("%H:%M:%S")[m
 [m
         # Validate inputs[m
[31m-        if not good_part or not QC_OK or not reworked or not x1 or not x2 or not y1 or not y2 or not hp or not lp:[m
[32m+[m[32m        if not good_part or not QC_OK or not reworked or not inlt or not otlt or not vlv or not oth or not hp or not lp:[m
             messagebox.showerror("Error", "All fields are required!")[m
             return[m
 [m
[31m-        dshbord_enty_2(currnt_time,good_part,reworked,QC_OK,hp,lp,x1,x2,y2,y1)[m
[32m+[m[32m        dshbord_enty_2(currnt_time,good_part,reworked,QC_OK,hp,lp,inlt,otlt,oth,vlv)[m
 [m
         messagebox.showinfo("Success", "Data saved successfully!")[m
[31m-        for i in [good_part_e,reworked_e,QC_OK_e,x1_e,x2_e,y2_e,y1_e,hp_e,lp_e]:[m
[32m+[m[32m        for i in [good_part_e,reworked_e,QC_OK_e,inlt_e,otlt_e,oth_e,vlv_e,hp_e,lp_e]:[m
             i.delete(0, tk.END)[m
[32m+[m[32m        for i,j in zip([inlt_e,otlt_e,oth_e,vlv_e],[inlt_deflt,otlt_deflt,oth_deflt,vlv_deflt]):[m
[32m+[m[32m            i.insert(0,j)[m
         step2_valid=0[m
 [m
     else:[m
         messagebox.showinfo("", "Complete Step1 first")[m
[31m-        for i in [good_part_e, reworked_e, QC_OK_e, x1_e, x2_e, y2_e, y1_e, hp_e, lp_e]:[m
[32m+[m[32m        for i in [good_part_e,reworked_e,QC_OK_e,inlt_e,otlt_e,oth_e,vlv_e,hp_e,lp_e]:[m
             i.delete(0, tk.END)[m
[32m+[m[32m        for i,j in zip([inlt_e,otlt_e,oth_e,vlv_e],[inlt_deflt,otlt_deflt,oth_deflt,vlv_deflt]):[m
[32m+[m[32m            i.insert(0,j)[m
 [m
 # Create the main tkinter window[m
 root = tk.Tk()[m
[36m@@ -169,17 +176,17 @@[m [mreworked_l.grid(row=1, column=0, sticky="w")[m
 reworked_e= tk.Entry(step2,font=stp12_entry_font,width=stp12_e_w_s,validatecommand=vcmd,validate="key")[m
 reworked_e.grid(row=1, column=1, padx=4, pady=5)[m
 [m
[31m-x1_l = tk.Label(step2, text="X1",font=stp12_lable_font,anchor="w",width=stp12_l_wm)[m
[31m-x1_l.grid(row=1, column=2, sticky="w")[m
[31m-x1_e= ttk.Combobox(step2,values=["7--8","8--9","9--10"],font=stp12_entry_font,width=6)[m
[31m-x1_e.grid(row=1, column=3, padx=4, pady=5)[m
[31m-x1_e.set("0")[m
[32m+[m[32minlt_l = tk.Label(step2, text="INLT",font=stp12_lable_font,anchor="w",width=stp12_l_wm)[m
[32m+[m[32minlt_l.grid(row=1, column=2, sticky="w")[m
[32m+[m[32minlt_e= tk.Entry(step2,font=stp12_entry_font,width=6)[m
[32m+[m[32minlt_e.grid(row=1, column=3, padx=4, pady=5)[m
[32m+[m[32minlt_e.insert(0,0)[m
 [m
[31m-x2_l = tk.Label(step2, text="X2",font=stp12_lable_font,anchor="w",width=stp12_l_wm)[m
[31m-x2_l.grid(row=1, column=4, sticky="w")[m
[31m-x2_e= tk.Entry(step2,font=stp12_entry_font,width=stp12_e_w_s,validatecommand=vcmd,validate="key")[m
[31m-x2_e.grid(row=1, column=5, padx=4, pady=5)[m
[31m-x2_e.insert(0,"0")[m
[32m+[m[32motlt_l = tk.Label(step2, text="OTLT",font=stp12_lable_font,anchor="w",width=stp12_l_wm)[m
[32m+[m[32motlt_l.grid(row=1, column=4, sticky="w")[m
[32m+[m[32motlt_e= tk.Entry(step2,font=stp12_entry_font,width=stp12_e_w_s,validatecommand=vcmd,validate="key")[m
[32m+[m[32motlt_e.grid(row=1, column=5, padx=4, pady=5)[m
[32m+[m[32motlt_e.insert(0,"0")[m
 [m
 # Step 2 row 3[m
 QC_OK_l = tk.Label(step2, text="QC_OK",font=stp12_lable_font,anchor="w",width=stp12_l_w)[m
[36m@@ -187,17 +194,17 @@[m [mQC_OK_l.grid(row=2, column=0, sticky="w")[m
 QC_OK_e = tk.Entry(step2,font=stp12_entry_font,width=stp12_e_w_s,validatecommand=vcmd,validate="key")[m
 QC_OK_e.grid(row=2, column=1, padx=4, pady=5)[m
 [m
[31m-y1_l = tk.Label(step2, text="Y1",font=stp12_lable_font,anchor="w",width=stp12_l_wm)[m
[31m-y1_l.grid(row=2, column=2, sticky="w")[m
[31m-y1_e= ttk.Combobox(step2,values=["7--8","8--9","9--10"],font=stp12_entry_font,width=6)[m
[31m-y1_e.grid(row=2, column=3, padx=4, pady=5)[m
[31m-y1_e.set("0")[m
[31m-[m
[31m-y2_l = tk.Label(step2, text="Y2",font=stp12_lable_font,anchor="w",width=stp12_l_wm)[m
[31m-y2_l.grid(row=2, column=4, sticky="w")[m
[31m-y2_e= tk.Entry(step2,font=stp12_entry_font,width=stp12_e_w_s,validatecommand=vcmd,validate="key")[m
[31m-y2_e.grid(row=2, column=5, padx=4, pady=5)[m
[31m-y2_e.insert(0,"0")[m
[32m+[m[32mvlv_l = tk.Label(step2, text="VLV",font=stp12_lable_font,anchor="w",width=stp12_l_wm)[m
[32m+[m[32mvlv_l.grid(row=2, column=2, sticky="w")[m
[32m+[m[32mvlv_e= tk.Entry(step2,font=stp12_entry_font,width=6)[m
[32m+[m[32mvlv_e.grid(row=2, column=3, padx=4, pady=5)[m
[32m+[m[32mvlv_e.insert(0,0)[m
[32m+[m
[32m+[m[32moth_l = tk.Label(step2, text="OTH",font=stp12_lable_font,anchor="w",width=stp12_l_wm)[m
[32m+[m[32moth_l.grid(row=2, column=4, sticky="w")[m
[32m+[m[32moth_e= tk.Entry(step2,font=stp12_entry_font,width=stp12_e_w_s,validatecommand=vcmd,validate="key")[m
[32m+[m[32moth_e.grid(row=2, column=5, padx=4, pady=5)[m
[32m+[m[32moth_e.insert(0,"0")[m
 [m
 [m
 # Row 3: Submit button[m
