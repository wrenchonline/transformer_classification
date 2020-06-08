import sys
import os

root_dir = '/home/wrench/下载/ML_Tech_Stack/Natural_language_process/'
parent_dir = '/home/wrench/下载/ML_Tech_Stack/Natural_language_process/data_onvif/1/'

HKfilenames =  []
for index in  range(2,122):
    HKfilenames = '172.30.15.' + str(index) + "_result.xml" 
    HKfilenames.append(os.path.join(parent_dir, filename))

for hk in HKfilenames:
        f = open(hk,'a')
        f.write('\t1')
        f.close()