import csv

with open("height-and-weight.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

sorted_data=[]
total_weight=0
total_entries=len(file_data)
for weight in file_data:
    total_weight+=float(weight[2])
    sorted_data.append(float(weight[2]))

sorted_data.sort()

def getMean(total_weight,total_entries):
    mean=total_weight/total_entries
    print("Mean/Average is:",mean)

getMean(total_weight,total_entries)