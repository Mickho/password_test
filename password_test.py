i = 0
while True:
	
	password = input('please input password:')
	if password == 'a123456':
		print('login_successful')
		break
	elif password != 'a123456':
		
		while i < 3:
			print('login fail please try again', i) 
		i = i + 1
		
