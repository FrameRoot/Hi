import time
import os
user = os.getlogin()
print(''' _______                            
|    ___|.----.---.-.--------.-----.
|    ___||   _|  _  |        |  -__|
|___|    |__| |___._|__|__|__|_____|
                                    ''')
time.sleep(1)
print(''' _______                    
|     __|.---.-.--.--.-----.
|__     ||  _  |  |  |__ --|
|_______||___._|___  |_____|
               |_____|      ''')
time.sleep(1)
print(''' _______ _______ 
|   |   |_     _|
|       |_|   |_ 
|___|___|_______|''')

time.sleep(1)


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    
    if iteration == total: 
        print()
hi = input('want to say hi to frame? (y/n)')

if hi == 'y':
    items = list(range(0, 57))
    l = len(items)
    printProgressBar(0, l, prefix = 'Hi Frame:', suffix = 'Sending', length = 50)
    for i, item in enumerate(items):
        time.sleep(0.1)
        printProgressBar(i + 1, l, prefix = 'Hi Frame:', suffix = 'Sended', length = 50)
    print()
    print(user,': Hi Frame')
    print('Frame: Hi , thanks for visiting my profile :)')
    input()
if hi == 'n':
    print('Frame is sad :(')
    input()


