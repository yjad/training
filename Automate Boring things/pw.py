#! python3
# pw.py - An insecure password locker program.

import sys, pyperclip

usage = '''
Usage: python pw.py [account]                    - copy account password
     : python pw.py [account] --m {new password} - modify account password
'''

no_of_params = len(sys.argv)
if no_of_params < 2:
    print(usage)
    sys.exit()
elif no_of_params == 4 and sys.argv[2] != '-m':
        print(usage)
        sys.exit()

account = sys.argv[1] # first command line arg is the account name
new_password = sys.argv[3]

PASSWORDS={
    'DTSEMAIL':'asd1010@',
    'HOTMAIL': 'yahia123',
    'GMAIL': 'yahia123',
    'TEDATA': 'yahia123',
    'RESERVATION':'Dts@1234',
    'NASRCITYWIFI': 'DTS1234',
}

account = account.upper()
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'Password of {account} copied to clipboard')
else:
    print (f'account {account} does not exist')
    exit()

