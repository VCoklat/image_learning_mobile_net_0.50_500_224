#!/usr/bin/python

import os, sys

from datetime import datetime
start=datetime.now()
for i in range(1,11):
   os.chdir('/home/pi/Desktop/mobile_net_0.50_500_224/tf'+str(i))
   text_file = open("Tabel_"+str(i)+".txt", "a")
   text_file.write("Nama File")
   text_file.write("\t")
   text_file.write("Clean")
   text_file.write("\t")
   text_file.write("Dirty")
   text_file.write("\t")
   text_file.write("Food")
   text_file.write("\t")
   text_file.write("Water")
   text_file.write("\t")
   text_file.write("Time")
   text_file.write("\n")

   text_file.close()
   os.system('python testing.py')

print datetime.now()-start
