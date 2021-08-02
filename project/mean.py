import csv
with open('HeightWeight.csv',newline='')as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    num=filedata[i][2]
    newdata.append(float(num))
total=0
for x in newdata:
    total+=x
    mean=total/len(newdata)
print("Mean",mean)
