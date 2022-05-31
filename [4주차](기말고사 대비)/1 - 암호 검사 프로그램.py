# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def gainRootRight():
  PASSWORD = 'hufs2020'
  MAX_TRIAL = 3
	
  loop = True
  c = 0
	
  while loop:
    if c < MAX_TRIAL:
	    a = input('암호: ')
	    if a == PASSWORD:
		    print('반갑습니다!')
		    return True
		    loop = False
	    elif a != PASSWORD:
		    if c == MAX_TRIAL -1:
		      print('더 이상 암호 입력이 불가능합니다')
		      return False
		      break
		    print('암호가 틀렸습니다.')
		    c += 1
				
#		    if c < 3:
#		      print('암호가 틀렸습니다.')
#		      c += 1
#		    elif c >= MAX_TRIAL:
#		      print('더 이상 암호 입력이 불가능합니다')
#		      return False
#		      loop = False
				
if gainRootRight():
  print('관리자 권한을 획득하였습니다.')
else:
  print('당신은 권한이 없습니다.')
