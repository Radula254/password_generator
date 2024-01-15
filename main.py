import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?.,#&'

length = input('Password length: ')
length = int(length)

times = input('Amount of passwords: ')
times = int(times)

for p in range(times):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)

