ooooooooooooooo#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To mhi

#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[+] \033[1;97mToken \033[1;97m:")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()

def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		menu()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		menu()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		menu()

def phone():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')

#Dev:Mhi
##### LOGO #####
logo = """
 /$$   /$$                     /$$          
 | $$$ | $$                    |__/         
| $$$$| $$  /$$$$$$  /$$$$$$$$ /$$  /$$$$$$
| $$ $$ $$ |____  $$|____ /$$/| $$ /$$__  $$
| $$  $$$$  /$$$$$$$   /$$$$/ | $$| $$  \__/
| $$\  $$$ /$$__  $$  /$$__/  | $$| $$
| $$ \  $$|  $$$$$$$ /$$$$$$$$| $$| $$
|__/  \__/ \_______/|________/|__/|__/
\033[1;96m           [\033[1;97mOwner Brand: MHI \033[1;97m]    
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(0.1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;95m❖⚏⚏⚏L💙U⚏⚏⚏❖❖⚏⚏⚏L💙U⚏⚏⚏❖
\033[1;95m[Owner   Mantal]
\033[1;95m[whatsap   aa      ]
\033[1;91m[Facebook  Mantal   ]
\033[1;91mNote: \033[1;97mWellcomeeeeeeeeee to
\033[1;97mVIP Tools with My user and pass
\033[1;91m❖⚏⚏⚏L💙U⚏⚏⚏❖❖⚏⚏⚏L💙U⚏⚏⚏❖
 """
CorrectUsername = "Mhi"
CorrectPassword = "Mhi"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m \x1b[1;91mTool Username \x1b[1;91m: \x1b[1;92m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m \x1b[1;91mTool Password \x1b[1;91m: \x1b[1;92m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Mhi
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;93mWrong Password"
            os.system('xdg-open https://chat.whatsapp.com/GWTPaJVAy1gDHIDgHEw0Ht')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://chat.whatsapp.com/GWTPaJVAy1gDHIDgHEw0Ht')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	print "\033[1;97m[1]\x1b[1;96mLogin With Facebook Account  "
        time.sleep(0.05)
        print "\033[1;97m[2]\x1b[1;96mLogin  With Token"
        time.sleep(0.05)
        print "\033[1;97m[3]\x1b[1;96mGet Free Token to Basit Ali"
        time.sleep(0.05)
	print "\033[1;97m[0]\033[1;96mExit             "
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;96mChoose an Option: \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
        elif peak =="3":
	        os.system('xdg-open https://www.facebook.com/SsRoCky420')
	        login()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		jalan(' \033[1;91
