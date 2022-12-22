#import required library
from tkinter import *
import re
from bs4 import BeautifulSoup
import requests
import datetime

main_screen = Tk()
main_screen.title("Crypto price show")
main_screen.geometry('300x250')
main_screen.resizable(width = False , height = False)

#time = datetime.datetime.now().strftime("%H:%M:%S")



Label(main_screen , text = "Crypto prices" , bg = 'Blue' , font = ('calibri' , 15)).pack()
time_label =Label(main_screen)
time_label.pack()
Label(main_screen , text="").pack()
btc_price = Label(main_screen , text = '' , bg ='orange' , font = ('calibri' , 12))
btc_price.pack(anchor=W , padx=5)
eth_price = Label(main_screen ,  text = '' , bg ='silver' , font = ('calibri' , 12))
eth_price.pack(anchor=W , padx= 5 , pady= 5)

def crypto():
    url = "https://coinmarketcap.com/currencies/bitcoin/"
    furl = requests.get(url)
    soup = BeautifulSoup(furl.content, 'html.parser')
    btc = str(soup.find('div', class_='priceValue'))
    btc_larger = re.findall(r'\$\d.+\d', btc)
    btc_larger1 = btc_larger[0]
    btc_price.config(text = f'BTC: {btc_larger1}')

    url = "https://coinmarketcap.com/currencies/ethereum/"
    furl = requests.get(url)
    soup = BeautifulSoup(furl.content , 'html.parser')
    eth = str(soup.find('div' , class_='priceValue'))
    eth_larger = re.findall(r'\$\d.+\d' , eth)
    eth_larger1 = eth_larger[0]
    eth_price.config(text=f'ETH: {eth_larger1}')

    time = datetime.datetime.now().strftime("%H:%M:%S")
    time_label.config(text=time)
    main_screen.after(1000 , crypto)

crypto()
main_screen.mainloop()
