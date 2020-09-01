print("This is the trash file.")

#admins
print('Test Admin/s')
print('username: admin | password: admin')

#users
print('Test User/s')
print('username: user1 | password: user1password')

#messages
from django.contrib import messages
message.debug
message.info
message.success
message.warning
message.error

messages.success(request, f'Account created for {username}!')
#note: python 3.7+ because of the f string