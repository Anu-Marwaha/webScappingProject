import csv

#Remove spaces in data set
"""
with open("storeNasaData.csv","r") as input, open("final_NasaData.csv","w",newline='') as output:
    input_csvRead=csv.reader(input)
    output_csvWrite=csv.writer(output)

    for row in input_csvRead:
        #print("row1=",row[0])
        if any(field for field in row):
            output_csvWrite.writerow(row)
            print("row=",row[2])
"""
#Merge two files
file1Read=[]
file2Read=[]

with open("final_achieve.csv","r") as file1,open("E:\whitehat\python\data files\PRO-129-Datasets-main\PRO-129-Datasets-main/final.csv","r") as file2:
    f1Read=csv.reader(file1)
    for row in f1Read:
        file1Read.append(row)

    f2Read=csv.reader(file2)
    for row in f2Read:
        file2Read.append(row)


header1=file1Read[0]
file1Data=file1Read[1:]   
header2=file2Read[0]
file2Data=file2Read[1:]
finalHeader=header2+header1
finalData=[]
for index, data in enumerate(file1Data):
    d=file2Data[index]+file1Data[index]
    finalData.append(d)

with open("completeData.csv","w") as f:
    fileWrite=csv.writer(f)
    fileWrite.writerow(finalHeader)
    fileWrite.writerows(finalData)
     
print("Merging completed")

#Remove spaces in data set
#"""
data=[]
with open("scrapper.csv","r") as input:
    input_csvRead=csv.reader(input)
    

    for row in input_csvRead:
        #print("row1=",row[0])
        if any(field for field in row):
            data.append(row)

with open("finalScrapper.csv","w",newline='') as output:
    output_csvWrite=csv.writer(output)
    output_csvWrite.writerows(data)
print("done")
#"""





