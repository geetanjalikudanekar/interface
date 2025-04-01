
step2_valid=0


#files
csv_data_file= "c:/Promat/data1.csv"
cvs_descrptn_file="c:/Promat/Part_Description.csv"
export_csv="c:/Promat/"


# variables for entry in Description frame
variable_dict = {}
desctn_e_w_s=6
desctn_e_w_m=10
desctn_e_w_b=33
desctn_lable_font=("arial",12)
desctn_entry_font=("arial",12)
desctn_label_full=[ "Date","Start","PO No", "PO QTY","Description", "End","Good",
           "Rewrkd", "QC_OK","HP","LP","INLT","OTLT","VLV","OTH","PPH"]
desctn_label_frst=[ "Date","Start","PO No", "PO QTY","Description"]
desctn_label_secnd=[ "End","Good","Rewrkd", "QC_OK","HP","LP","INLT","OTLT","VLV","OTH"]
def entry_normal():
    for i,text in enumerate(desctn_label_full):
        for j in range(1,no_dash_b_ent+1):
            variable_dict[f"{text}_{j}{i}"].config(state="normal")
def entry_disable():
    for i,text in enumerate(desctn_label_full):
        for j in range(1,no_dash_b_ent+1):
            variable_dict[f"{text}_{j}{i}"].config(state="disable")


#Rows decoration varicable
# stick_ew="ew"
# stick_

#Number of columns in dashboard entry
no_dash_b_ent=7


#step 1 and 2 Variables
stp12_e_w_s=8
stp12_e_w_b=33

stp12_l_w=9
stp12_l_w1=6
stp12_l_wm=3
stp12_lable_font=("Arial",12)
stp12_entry_font=("Arial",12)

#step 1 Variables
stp1_e_w_s=10
stp2_l_w_s=15

stp12_head_font=("Monotype Corsiva", 14, "bold")

#defalt value varible
shift_deflt="first"
inlt_deflt=0
otlt_deflt=0
vlv_deflt=0
oth_deflt=0