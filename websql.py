from googlesearch import search
import time
import random
import os
os.system('clear')
y = "\u001b[32;1m"
n = '\u001b[31;1m'
r = '\u001b[0m'
print(
 n+   '''
                  bb                             lll 
ww      ww   eee  bb       sss      sss    qqqqq lll 
ww      ww ee   e bbbbbb  s        s     qq   qq lll 
 ww ww ww  eeeee  bb   bb  sss      sss   qqqqqq lll 
  ww  ww    eeeee bbbbbb      s        s      qq lll 
                           sss      sss       qq     
    '''+r
)
print('links con posibilidades de ataque sql')
print("")
print('Escoja una opcion\n')
print('iniciar(y)')
print('salir(x)\n')
c = input('--->  ')
if c == 'y':
        os.system('clear')
        lis = ['shop.','paypal.','inurl ','buy.']

        a = random.randint(0,3)
        b = random.randint(1,9)

        index = lis[a]

        sear = 'php?id='
        sear = index+sear+str(b)

        for i in search(sear, num_results=200, lang='es'):
                  if 'https' in i:
                       print(n,i,r)
                       print('----------------------------------')
                  else:
                       print(y,i,r)
                       print('----------------------------------')
        print(r,"")
        print('presione x para salir\n')
        x = input('---> ')
        if x == 'x':
              os.system('clear')
