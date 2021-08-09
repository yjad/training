import os
import pathlib
import datetime
import csv


correct = 0
corrupted = 0


for f in os.listdir(".\\data\CUSTOMER"):
    # print (f)
    # fname = pathlib.Path(os.path.join(".\\data", f))
    fname = pathlib.Path(os.path.join(".\\data\\CUSTOMER", f))
    ctime = datetime.datetime.fromtimestamp(fname.stat().st_ctime)
    mtime = datetime.datetime.fromtimestamp(fname.stat().st_mtime)
    try:
        with open(fname, 'r', encoding = "UTF8") as fp:
            txt = fp.readline()
            if "???" in txt:
                # print  (f, ": XXXXXXXXXXXXXXXXXXXXXXX", mtime)
                print  (f, ",", mtime)
                corrupted +=1
            else:
                # print  (f, ": correct file: ", mtime)
                correct +=1
    except:
        print  (f, ",", mtime, "***")
        corrupted +=1
        
print (50*'-','\n', "correct :", correct, "corrupted: ", corrupted) 