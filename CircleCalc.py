from cmath import sqrt
from encodings import utf_8
utf_8

print('Circle Calculator\n©Dobastickrn  Date:2023/4/6\n注意：本工具中π的取值为3.14\n')
while True:
  M = input('输入模式\na：正向\nb：反向\n')
  if M=='a' or M=='b':
    go='t'
  else:
    go='f'
  
  if go=='t':
    if M=='a':
      r=input('输入半径\n')
      d=2*float(r)
      C=float(d)*3.14
      S=float(r)**2*3.14
      print('当半径为'+r+'时→')
      print('直径为 '+str(d))
      print('周长为 '+str(C))
      print('面积为 '+str(S))
      print('计算完毕\n')

    else:
      M_=input('面积还是周长？\na: 面积\nb: 周长\n')
      if M_=='a' or M=='b':
        go_='t'
      else:
        go_='f'
      if go_=='t':
        if M_=='a':
          S=input('输入面积\n')
          r=sqrt(float(S)/3.14)
          d=2*float(r)
          S=float(d)*3.14
          print('当面积为'+str(S)+'时→')
          print('直径为 '+str(d))
          print('周长为 '+str(C))
          print('计算完毕\n')
        else:
          C=input('输入周长\n')
          d=float(C)/3.14
          r=float(d)/2
          S=float(r)**2*3.14
          print('当周长为'+str(C)+'时→')
          print('半径为 '+str(r))
          print('直径为 '+str(d))
          print('面积为 '+str(S))
          print('计算完毕\n')
  else:
    print('请正常点 :)')