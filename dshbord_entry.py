from variables import variable_dict,cvs_descrptn_file,\
    desctn_label_secnd,csv_data_file,no_dash_b_ent,desctn_label_full,\
    entry_disable,entry_normal
from datetime import datetime
from save_to_csv_step2 import insert_csv_step2
import pandas as pd


def dshbord_enty_1(currnt_date,currnt_time,part,po_no,po_qty):
    part_descrptn = cvs_descrptn_file
    df = pd.read_csv(part_descrptn)
    entry_normal()

    for i in range (1,no_dash_b_ent+1):  # finding out empty row for entry
        value= variable_dict[f"Date_{i}0"].get()
        if value=="":
            counter=i
            break;
        else:
            continue

    currnt_time = datetime.now().strftime("%H:%M:%S")
    label=["Date","Start","PO No", "PO QTY"] # data entry in description frame
    values=[currnt_date,currnt_time,po_no,po_qty]
    for i ,(text,value) in enumerate(zip(label,values)):
        variable_dict[f"{text}_{counter}{i}"].insert(0,value)

    if part in df["Part"].values:
        value=df.loc[df["Part"]==part,"Description"].values[0]  # feching description from csv file according to part
        variable_dict[f"Description_{counter}4"].insert(0, value)
    else:
        variable_dict[f"Description_{counter}4"].insert(0, "None")
    entry_disable()


def dshbord_enty_2(currnt_time,good_part,reworked,QC_OK,hp,lp,inlt,otlt,oth,vlv):
    counter = 1
    entry_normal()
    for i in range(1,no_dash_b_ent+1 ):  # finding out empty row for entry
        value2 = variable_dict[f"Good_{i}6"].get()
        if value2 == "":
            counter=i
            label = desctn_label_secnd # data entry in description frame
            values = [currnt_time,good_part,reworked,QC_OK,hp,lp,inlt,otlt,oth,vlv]
            for index, (text, value) in enumerate(zip(label, values)):
                variable_dict[f"{text}_{counter}{index+5}"].insert(0, value)
            start = (variable_dict[f"Start_{counter}1"].get())
            end = variable_dict[f"End_{counter}5"].get()
            time_hm_s = datetime.strptime(start, "%H:%M:%S").strftime("%H:%M")
            time_hm_e = datetime.strptime(end, "%H:%M:%S").strftime("%H:%M")
            Start_time = datetime.strptime(time_hm_s, "%H:%M")
            End_time = datetime.strptime(time_hm_e, "%H:%M")
            time_difference = End_time - Start_time
            total_min = time_difference.total_seconds() / 60
            if total_min > 0:  # To prevent division by zero
                value=int(variable_dict[f"QC_OK_{counter}8"].get())
                PPH_value = (value/ total_min)*60
                variable_dict[f"PPH_{counter}15"].insert(0, PPH_value)
            else:
                PPH_value = 0
                variable_dict[f"PPH_{counter}15"].insert(0, PPH_value)
            insert_csv_step2(currnt_time,good_part,reworked,QC_OK,hp,lp,inlt,otlt,vlv,oth,PPH_value)
            break
        else:continue
    entry_disable()
