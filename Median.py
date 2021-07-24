import csv

with open("height-and-weight.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

sorted_data=[]
total_weight=0
n=len(file_data)
for weight in file_data:
    total_weight+=float(weight[2])
    sorted_data.append(float(weight[2]))

sorted_data.sort()

if n%2==0:
    median1=float(sorted_data[n//2])
    median2=float(sorted_data[n//2-1])
    median=(median1+median2)/2

else:
    median=float(sorted_data[n//2])
    print(n)

print("Median is:"+str(median))