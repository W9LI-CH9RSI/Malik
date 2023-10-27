from urllib import response
import mechanize
import os
from time import sleep
import datetime
import sys
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0')]
browser.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'


def openlink(msg4):

    r = browser.open(msg4)

def aclass():

    browser.open(url)

    browser.select_form(nr = 0)

    browser.form['email'] = emailx

    browser.form['pass'] = pwx

    r = browser.submit()

    browser.select_form(nr = 0)

    browser.form['name_action_selected'] = ['save_device']

    r = browser.submit()
      
      
      
    r = browser.open(url)
    x = browser.title()
    if x == "Review recent login":
        print("\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.")
        exit(1)
    if x == "Login approval needed":
        print("\nYour account is stuck on verification\nPlease do it and then re run the program.")
        exit(1)
    if x == "Epsilon":
        print("\nYour account got locked, recover it kindly and re run the script.")
        exit(1)

  
    





def poct(comment):

    browser.select_form(nr = 0)
    print("\033[1;37;40m")
    	
    browser.form['comment_text'] = comment
        
    r = browser.submit()
    
    print("\033[1;37;40m")
    e = datetime.datetime.now()
    print (e.strftime("»» %d/%m/%Y   %I:%M:%S %p"))
logo = ("""\033[97;1m
   
   
 \33[1;36m$$$$$$\ $$\     $$\ $$\   $$\  $$$$$$\  $$\   $$\ 
 \33[1;36m$$  __$$\\$$\   $$  |$$ |  $$ |$$  __$$\ $$ |  $$ |
\33[1;36m$$ /  $$ |\$$\ $$  / $$ |  $$ |$$ /  \__|$$ |  $$ |
\33[1;36m$$$$$$$$ | \$$$$  /  $$ |  $$ |\$$$$$$\  $$$$$$$$ |
\33[1;36m$$  __$$ |  \$$  /   $$ |  $$ | \____$$\ $$  __$$ |
\33[1;36m$$ |  $$ |   $$ |    $$ |  $$ |$$\   $$ |$$ |  $$ |
\33[1;36m$$ |  $$ |   $$ |    \$$$$$$  |\$$$$$$  |$$ |  $$ |
\33[1;36m\__|  \__|   \__|     \______/  \______/ \__|  \__|
                                                   
                                                                                              
\33[1;32m -----------------------------------------------------------------------------------------                                 
X====TH3 UNSTOPP9BL3 W9LI CH9RSI ====X

\33[1;32m[[ AUTHOR NAME ]]      (( XM9RTY AYUSH K1NG )) 

\33[1;32m[[ TOOL CREATED BY ]]  (( XM9RTY AYUSH K1NG )) 
\33[1;32m -----------------------------------------------------------------------------------------
                                                         

    
    
    
    
\33[1;32m""")
os.system('clear')
print(logo)
 
print ("[-[ TH3 T00L CREATE BY  XM9RTY AYUSH K1NG]-]")

emailx=str(input("➣ >>> EMAIL DAALO  : "))

pwx =str(input("➣ >>> PASSWORD DAALO : "))

aclass()

msg4=str(input("➣ >>>ENTER POST LINK : "))

msg5=str(input("➣ >>> ENTER NOTPAD  : "))

f=open(msg5, 'r')

lines = f.readlines()

f.close()

msg6= int(input("➣ENTER TIME : "))

os.system('clear')

sys.stdout.flush()

print("\033[1;37;40m")
e = datetime.datetime.now()
print(e.strftime("Start Time = %d/%m/%Y   %I:%M:%S %p"))
print()
count = 0
while True:
    for line in lines:
        if len(line) > 0:
            if count != 0:
            	sleep(msg6)
            openlink(msg4)
            poct(line)
            print("\033[1;33;96m", end = "")
            print('>> XM9RTY AYUSH K1NG >> ', line)
            print("\033[91;1m")
            count += 1
            if count % 50 == 0:
            	sleep(1)
                
                
                
                
                
            
            
                
                
