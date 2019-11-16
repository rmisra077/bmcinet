import time, threading, csv
from serial import Serial

s = "0"
PORT = 'COM5'
BAUD = 9600

#emg_data = open('emg_data.csv', mode='w')
#emg_writer = csv.writer(emg_data, delimiter=',', quoting=csv.QUOTE_MINIMAL)


def input_thread(L):
    d = input()
    L.append(d)

ser = Serial(PORT, BAUD, timeout=0.25)
# to write data to the serial port
#ser.write("hello")

#Reading line by line data from serial port
def get_emg():
    #L = []
    #threading.Thread(target=input_thread, args=(L,)).start()
    #time.sleep(.25)
    line = ser.readline()
    s = "".join(chr(i) for i in line)
    s = s.strip()
    return s
    # if not(s == "" or s == " " or s== "\n"):
    #     file.write(s + "\n")
    #     emg_writer.writerow([s])
    #if L: break
    #print("Done")