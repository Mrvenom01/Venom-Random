#<\>!python3.11 
 #<\>coded by Mrvenom01
 #----------------Don't Copy This Script--------------# 
 import os, sys, platform 
 try: 
     import requests 
 except: 
     os.system('pip install requests') 
 os.system('xdg-open https://facebook.com/Sujoy.name.of.brand/') 
 import requests 
 try: 
     if sys.argv[1]=='update': 
         os.system('rm -rf xd.so') 
 except: 
     pass 
 os.system('rm -rf xd.so') 
 os.system('git pull') 
  
 bit = platform.architecture()[0] 
 if bit == '64bit': 
     if not os.path.isfile('xd.so'): 
         os.system('curl -L https://github.com/Mrvenom01/Venom-Random/blob/main/Run.cpython-311.so?raw=true -o xd.so')  
         import xd   
     else: 
         import xd 
 elif bit == '32bit': 
     exit('\033[1;31m\n Sorry System or 32bit device not supported ')
