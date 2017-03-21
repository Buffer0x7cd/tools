import requests
from bs4 import BeautifulSoup

print("input roll number and sem")
rollno = input()
sem = input()
url = "http://mis.itmuniversity.ac.in/itmzone/std/main/Regcopy2.php?temp1={0}&temp2={1}".format(rollno,sem)

res = requests.get(url)

#print(res.status_code)

if res.status_code == 200:
    print('INFORMATION FOUND\n')

soup = BeautifulSoup(res.text,'lxml')

list_info = soup.find_all('span')

for data in range(4):
    if data == 1:
        pass
    else:
        print(list_info[data].text)
