import socket, os, sys
from time import time as timer	
from multiprocessing.dummy import Pool
from colorama import Fore								
from colorama import Style
####### Colors	 ######	
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT
										
#######################

def banners():
    try:
        os.mkdir('logs')
        os.mkdir('result')
    except:
        pass
        
    banner = """{}

                   ...          
                 ;::::;           ::
               ;::::; :;        :::::: 
              ;::::;  :;   Dir/File Scanner
             ;:::::'   :;     By RaiC0d3r
            ;:::::;     ;.
           ,:::::'       ;           OOO\
           ::::::;       ;          OOOOO\{}
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO  {}
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#                                                                                            

		\n""".format(fg, fr, fg, sn)
		
    print(banner)


def getoption():
    print("{}[1]{} Single Site".format(fg, fw))
    print("{}[2]{} Multiple Site".format(fg, fw))
    choiceoption=input('Put Number => ')
    if choiceoption=='1':
        url = input("\n\033[92m[!]\033[91m ENTER WEBSITE/IP : ")
        singleiprange(url)
        
    elif choiceoption=='2':
        start_raw = input("\n\033[92m[!]\033[91m ENTER LIST OF WEBSITES/IP : ")
        try:
            with open(start_raw, 'r') as f:
                url = f.read().splitlines()
        except IOError:
            pass
        start = timer()
        ThreadPool = Pool(100)
        Threads = ThreadPool.map(multiiprange, url)
        print('PrivateBot Finished in : ' + str(timer() - start) + ' seconds')

def singleiprange(url):
    try:
        ip = socket.gethostbyname(url)
        parts = ip.split('.')
        part_0 = parts[0]
        part_1 = parts[1]
        part_2 = parts[2]
        part_3 = parts[3]
        sep = '.'
        for x in range(1, 256):
            result = (part_0 + sep + part_1 + sep + part_2 + sep + str(x))
            print(result)     
            open('logs/iprangee.txt', 'a').write(result+'\n')
        lines_seen = set() # holds lines already seen
        outfile = open("result/iprange.txt", "w")
        for line in open('logs/iprangee.txt', "r"):
            if line not in lines_seen: # not a duplicate
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()         
    except:
        pass
##################end reverse############

def multiiprange(url):
    try:
        ip = socket.gethostbyname(url)
        parts = ip.split('.')
        part_0 = parts[0]
        part_1 = parts[1]
        part_2 = parts[2]
        part_3 = parts[3]
        sep = '.'
        for x in range(1, 256):
            result = (part_0 + sep + part_1 + sep + part_2 + sep + str(x))
            print(result)     
            open('logs/iprangee.txt', 'a').write(result+'\n')
        lines_seen = set() # holds lines already seen
        outfile = open("result/iprange.txt", "w")
        for line in open('logs/iprangee.txt', "r"):
            if line not in lines_seen: # not a duplicate
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()         
    except:
        pass
##################end reverse############
banners()
getoption()


