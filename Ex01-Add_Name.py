import time

with open('registro.txt', 'a') as file:
    name = input('Qual seu nome? ')

    file.write('%s/%s \n' % (time.ctime(), name))  