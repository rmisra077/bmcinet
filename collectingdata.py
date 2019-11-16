from epoc_plus_example import EEG
from SerialDataEMG import get_emg
import csv
import time
#cyHeadset = EEG()
# restcount = 0
# clenchcount = 0
# currentstate = "open"
# while(1):
#     emg = get_emg()
#     if(int(emg) > 150 and clenchcount >= 30):
#         #print("hello")
#         clenchcount = 0
#         if(currentstate == "open"):
#             currentstate = "closed"
#         elif(currentstate == "closed"):
#             currentstate = "open"
#     elif (int(emg) > 150 and clenchcount < 30):
#         #print("hi")
#         clenchcount += 1
#     print(currentstate)
while 1:
    emg = get_emg()
    if(int(emg) > 150):
        #totaleegemglist.append("1")
        print("clench")
    else:
        #totaleegemglist.append("0")
        print("rest")
# with open('eeg-emg-combined-final6-data.csv',  mode='w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     print("Opened CSV file")
#     while 1:
#         #count+=1
#         #print(type(get_emg()))
#         totaleegemglist = cyHeadset.get_data().split(", ")
        
#         emg = get_emg()
#         totaleegemglist.append(emg)
#         if(int(emg) > 150):
#             totaleegemglist.append("1")
#             print("clench")
#         else:
#             totaleegemglist.append("0")
#             print("rest")
#         #csv_writer.writerow(totaleegemglist)
#         #print(totaleegemglist)
#         #if(emg > )
#         # if(count % 103 == 0):
#         #     #print("CLENCHING")
#         #     time.sleep(0.25)
#         #     t_end = time.time()+0.68
#         #     while time.time() < t_end :
#         #         #print("clench")
#         #         totaleegemglist = cyHeadset.get_data().split(", ")
#         #         #totaleegemglist = []
#         #         totaleegemglist.append(get_emg())
#         #         totaleegemglist.append("1")
#         #         #print(totaleegemglist)
#         #         #csv_writer.writerow(totaleegemglist)
#         # else:
#         #     #print("rest")
#         #     totaleegemglist = cyHeadset.get_data().split(", ")
#         #     #totaleegemglist = []
#         #     totaleegemglist.append(get_emg())
#         #     totaleegemglist.append("0")
#         #     #print(totaleegemglist)
#         #     #csv_writer.writerow(totaleegemglist)
        
        