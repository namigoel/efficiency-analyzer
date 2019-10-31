#graph plotting
#data
#importing header files
import os

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style

'exec(%matplotlib inline)'

import csv

import numpy as np
style.use('ggplot')
fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')
heading=input("Enter measure")
entries=[]
#month=['january','february','march','april','may','june','july','august','september','october','november','december']
filename=os.path.abspath( os.path.join("data","data1.csv"))
with open(filename,'r') as csvfile:
   fields=csvfile.readline().strip().split(',')
   print(fields)
   test_passed=0
   products=0
   efficiency=[]
   for line in csvfile:
       parts=line.strip().split(',')
       row=dict()
       for i,h in enumerate(fields):
           row[h]=parts[i]
           if(i==3):
               test_passed=float(parts[i])
           elif(i==1):
               products=float(parts[i])
       if (products == 0):
           div = 0
       else:
           div = test_passed / products
       efficiency.append(int(div*100))
       entries.append(row)

print(efficiency)
fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')
ypos=[]
for i in range(len(entries)):
   ypos.append(float(entries[i]['Cost (in billions)']))
xpos_array=[1,2,3,4,5,6,7,8,9,10,11,12]
ypos_array=np.asarray(ypos).astype(int)
zpos_array=np.zeros(12).astype(int)
dx=np.ones(12)
dy=[2,2,2,2,2,2,2,2,2,2,2,2]
dz=[]
my_xticks=['Jan','Feb','Mar','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
for i in efficiency:
    dz.append(int(i))
dz_array=np.asarray(dz).astype(int)
plt.xticks(xpos_array,my_xticks,rotation=90)
for i in range(0,12):
    ax1.text(xpos_array[i]-0.5,ypos_array[i]+3,dz_array[i],'%s'%str(dz[i]),size=10)
plt.title=heading

ax1.bar3d(xpos_array,ypos_array,zpos_array,dx,dy,dz_array,color=['red','blue','green','yellow','orange','black','brown','cyan','magenta','pink','blue','green'])

plt.show()



#for e in entries:
       #print("{0}month , quality tests passed are{1}".format(e['Month'],e['Quality test passed (in millions)']))












