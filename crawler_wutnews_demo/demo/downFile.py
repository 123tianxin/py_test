import requests  
  
res = requests.get('http://bmob-cdn-16420.b0.upaiyun.com/2018/01/21/dfe2f2f040f46aa380b9fc3068e5c695.txt')  
  
res.raise_for_status()  
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):  
    playFile.write(chunk)  
playFile.close()