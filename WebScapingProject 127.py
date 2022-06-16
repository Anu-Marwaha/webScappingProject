from bs4 import BeautifulSoup
from selenium import webdriver
#import requests
import csv
import time
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("./chromedriver.exe")
browser.get(START_URL)

time.sleep(10)
headers = ["name", "distance", "mass", "radius"]
star_data = []

soup = BeautifulSoup(browser.page_source, "html.parser")
table1=soup.find_all("table", attrs={"class", "wikitable sortable jquery-tablesorter"})
print("table1= ",table1)
tbody=table1[0].find_all("tbody")
print("tbody= ",tbody)
def scrape():
    for tr_tag in tbody[0].find_all("tr"):
        td_tags = tr_tag.find_all("td")
        temp_list = []
        for index, td_tag in enumerate(td_tags):
            print(index,td_tag)
            
            if index == 1:
                if td_tag.find_all("a"):
                    print(index,"=",td_tag.find_all("a")[0].contents[0])
                    temp_list.append(td_tag.find_all("a")[0].contents[0].strip())
                else:
                    print(index,"=",td_tag.contents)
                    temp_list.append(td_tag.contents[0].strip()) 
            elif index== 3:
                print(index,"=",len(td_tag.contents))
                if(len(td_tag.contents)==1):
                    temp_list.append(td_tag.contents[0].strip())
                else:
                    temp_list.append(td_tag.contents[1].strip())
            elif index== 5:
                #print(td_tag.contents)
                temp_list.append(td_tag.contents[0].strip())
            elif index== 6:
                #print(td_tag.contents)
                temp_list.append(td_tag.contents[0].strip())
            else:
                print("other index")
                #temp_list.append("")
            
        print("temp list=",temp_list)
        star_data.append(temp_list)
scrape()
print("done")
#print(star_data)



print(star_data)
time.sleep(10)
with open("scrapper.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)
print("done2")

#remove spaces from scrapper.csv file in diffrent code
"""
data=[]
with open("scrapper.csv","r") as input:
    input_csvRead=csv.reader(input)
    for row in input_csvRead:
        #print("row1=",row[0])
        if any(field for field in row):
            data.append(row)
print("done3")
with open("FinalScrapper.csv","w") as output:
    output_csvWrite=csv.writer(output)
    output_csvWrite.writerows(data)
print("done4")
"""