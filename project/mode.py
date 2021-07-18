import csv
from collections import Counter
with open('HeightWeight.csv',newline='')as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    num=filedata[i][1]
    newdata.append(float(num))
data=Counter(newdata)
print(data)
mode_data_range={
    '60-70':0,
    '70-80':0,
    '80-90':0
}
for height,occurance in data.items():
    if 120<float(height)<150:
        mode_data_range['60-70']+=occurance
    elif 150<float(height)<180:
        mode_data_range['70-80']+=occurance
    elif 180<float(height)<206:
        mode_data_range['80-90']+=occurance
moderange,modeoccurance=0,0
for range,occurance in mode_data_range.items():
    if occurance>modeoccurance:
        moderange,modeoccurance=[int(range.split('-')[0]),int(range.split('-')[1])],occurance
mode=float((moderange[0]+moderange[1])/2)
print (moderange[0],moderange[1])
print(modeoccurance)