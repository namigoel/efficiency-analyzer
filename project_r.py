import os

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style

'exec(%matplotlib inline)'


import csv

import numpy as np
style.use('ggplot')
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
heading=input("Enter measure")
target=input("enter target")
monthly_target=int(int(target)/12)
entries=[]
# month=['january','february','march','april','may','june','july','august','september','october','november','december']
filename=os.path.abspath( os.path.join("data", "data1.csv"))
with open(filename, 'r') as csvfile:
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
min_cost=np.min(ypos_array)
for i in range(0,12):
    if(ypos_array[i]==min_cost):
        cost_index=i
        month_index=i
        z_index=i
        break
zpos_array=np.zeros(12).astype(int)
dz=[]
my_xticks=['Jan','Feb','Mar','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
for i in efficiency:
    dz.append(int(i))
dz_array=np.asarray(dz).astype(int)
max_eff=np.max(dz_array)
for i in range(0,12):
    if(dz_array[i]==max_eff):
        eff_index=i
        month_eff=i
        break
print(min_cost,max_eff)
plt.xticks(xpos_array,my_xticks,rotation=90)
for i in range(0,12):
    ax1.text(xpos_array[i],ypos_array[i]+3,dz_array[i],'%s'%str(dz[i]),size=10)
for i in range(0,12):
    ax1.text(xpos_array[i]+0.5,ypos_array[i]+3,dz_array[i],'%s'%str(ypos_array[i]),size=9)
plt.title(heading)
ax1.set(xlabel='',ylabel='cost',zlabel='efficiency')
dz_array_less=[]
dz_array_more=[]
for i in range(len(dz_array)):
    if(dz_array[i]<monthly_target):
        dz_array_less.append(i)
    else:
        dz_array_more.append(i)
x_less=[]
x_more=[]
y_less=[]
y_more=[]
z_less=[]
dx_less=[]
dx_more=[]
dy_more=[]
dy_less=[]
z_more=[]
dz_more=[]
dz_less=[]
for i in dz_array_less:
    x_less.append(xpos_array[i])
    y_less.append(ypos_array[i])
    z_less.append(zpos_array[i])
    dz_less.append(dz_array[i])
for i in dz_array_more:
    x_more.append(xpos_array[i])
    y_more.append(ypos_array[i])
    z_more.append(zpos_array[i])
    dz_more.append(dz_array[i])
print(x_less)
print(y_less)
print(z_less)
print(dz_array_less)
for i in range(0,len(x_less)):
    dx_less.append(int('1'))
    dy_less.append(int('1'))
for i in range(0,len(x_more)):
    dx_more.append(int('1'))
    dy_more.append(int('1'))
print(dx_less)
print(dy_less)
#ax1.annotate('Min cost',xyz=(month_index,cost_index,z_index),xyzcoords='data',xyztext='-30,0,0',textcoords='offset points',bbox=dict(boxstyle="round4,pad=.5", fc="0.9"),
# arrowprops=dict(arrowstyle="->")


ax1.bar3d(np.asarray(x_less),np.asarray(y_less),np.asarray(z_less),np.asarray(dx_less),np.asarray(dy_less),np.asarray(dz_less),color='red',edgecolor='black')
ax1.bar3d(np.asarray(x_more),np.asarray(y_more),np.asarray(z_more),np.asarray(dx_more),np.asarray(dy_more),np.asarray(dz_more),color='green',edgecolor='black')
#ax1.bar3d(xpos_array[xpos_array_max],ypos_array[ypos_array_max],zpos_array,dx,dy,dz_array[dz_array_more],color='green')

plt.show()



#for e in entries:
       #print("{0}month , quality tests passed are{1}".format(e['Month'],e['Quality test passed (in millions)']))












