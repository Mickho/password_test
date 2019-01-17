i = 3
pwd = 'a123456'
while True:
	password = input('please input password:')
	if password == 'pwd':
		print('login_successful')
		break
	elif password != 'pwd':
			i = i - 1
			print('login fail please try again', i, 'times') 
			if i == 0:
				print('login fial')
				break	