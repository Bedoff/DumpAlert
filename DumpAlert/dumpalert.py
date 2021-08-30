import time
from datetime import datetime
from binance.client import Client
from binance.enums import *
import os
import webbrowser

class style():          
    RED = '\033[31m'
    GREEN = '\033[32m'        
    RESET = '\033[0m'

api_key = ''
api_secret = ''
client = Client(api_key, api_secret)
os.system("cls")    
print("Enter pair1 param: (EXAM: BTC)")
trdPair1=input()
print("Enter pair2 param: (EXAM: USDT)")
trdPair2=input()

print("if "+trdPair1+" drops below _______ "+trdPair2)
alarm=input()
os.system("cls")



while 1==1:
    tradePair = trdPair1 + trdPair2    
    price = client.get_ticker(symbol=tradePair)
    lastprice = price['askPrice']
    symbol = price['symbol']
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    

    if lastprice < alarm:
        print(style.RED+"Time: ",current_time+" "+lastprice+" "+symbol+" ALARM ACTİVATED")
        print(style.RESET+"------------------------------------------------------")
        break
    else:
        print(style.GREEN+"Time: ",current_time+" "+lastprice+" "+symbol+" NO PROBLEM")
        print(style.RESET+"-------------------------------------------------")

    time.sleep(5)

print(style.RED+"Time: ",current_time+" "+lastprice+" "+symbol+" ALARM ACTİVATED")
print(style.RESET+"------------------------------------------------------")

print(style.RED+"Time: ",current_time+" "+lastprice+" "+symbol+" ALARM ACTİVATED")
print(style.RESET+"------------------------------------------------------")

print(style.RED+"Time: ",current_time+" "+lastprice+" "+symbol+" ALARM ACTİVATED")
print(style.RESET+"------------------------------------------------------")

print(style.RED+"Time: ",current_time+" "+lastprice+" "+symbol+" ALARM ACTİVATED")
print(style.RESET+"------------------------------------------------------")

edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
firefox_path="C://Program Files//Mozilla Firefox//firefox.exe"

webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

webbrowser.get('edge').open('https://www.youtube.com/watch?v=3wG-krTvbqM')
time.sleep(2)
webbrowser.get('edge').open('file:///C:/Users/0/go/src/github.com/bedoff/golang/BinanceAlarm/webalarm.html')
webbrowser.get('firefox').open('https://www.youtube.com/watch?v=v8gh3UUaaYY')

time.sleep(15)
webbrowser.get('firefox').open('https://coin360.com/?dependsOn=volume&period=1h')

while 1==1:
    print(style.RED+"WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP")
    print(style.RESET+"WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP WAKE UP")



