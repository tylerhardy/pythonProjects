#! python3

# pw.py - An insecure password locker program.


PASSWORDS = {'email':'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog':'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage':'12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

# first command line arg is the account name
account = sys.argv[1]

if account in PASSWORDS.keys():
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to the clipboard.')    
else:
    print('There is no account name ' + account)