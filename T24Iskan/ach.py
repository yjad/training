import datetime
import pathlib
import pandas as pd

ach_out_file = r'C:\Yahia\Home\Yahia-Dev\Python\training\T24Iskan\data\ACHOUT.txt'
d = []
data = pd.DataFrame()
with open(ach_out_file, 'rt') as f:
    while(True):
        line = f.readline()
        if not line:
            break
        fdt_time = line[45:57]
        ftime = line[52:57]
        
        xtime:float = int(ftime[0:2]) + int(ftime[4:6])/60
        size = int(line[34:44])
        d.append([fdt_time, ftime, xtime, size])
        # print (fdt_time, ftime, size)
        print (fdt_time, ftime, xtime, size)
        
data = {'time': times,
        'size':
}