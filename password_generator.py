import random as rd

chars = 'abcdefghijqlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%*().,/?0123456789'

quant = int(input('Number of passwords: '))

size = int(input('Passwords sizes: '))

print('\nYour passwords are read!\n')

for i in range(quant):
    for j in range(size):
        print(f'{rd.choice(chars)}', end='')
    print('\n')
