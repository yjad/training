import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug('hello')
print(10,20, sep='', end='')
print('xxxxxxxxxxxxxxx', sep='', end='')

for i in range(10):
    print (f'this is a print line: {i}')
    logging.debug(f'debug i : {i}')