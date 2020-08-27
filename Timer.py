from time import *
import pyaudio

print("Welcome to the python timer !")
sleep(1)
type = input("Type 'min' for minutes and 'sec' for seconds: ")
if type.lower() == 'min':
    pass
elif type.lower() == 'sec':
    pass
else:
    print("Could not recognize command . Quitting...")
    sleep(1)
    quit()
total = input("How many ? ")
print('Starting in...')
sleep(0.5)
for i in range(3, 0, -1):
    print(i)
    sleep(1)

if type.lower() == 'min':
    print('Started...')
    sleep(0.5)
    for i in range(int(total), -1, -1):
        print(i)
        sleep(120)
elif type.lower() == 'sec':
    print('Started...')
    sleep(0.5)
    for i in range(int(total), -1, -1):
        print(i)
        sleep(1)

