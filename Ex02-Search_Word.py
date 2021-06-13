file_name = input('Nome do arquivo? ')
word = input('Palavra? ')
line = 1

try:
    with open(file_name, 'r') as file:
        while(True):
            read = file.readline()
            if(read == ''):
                break

            if(word in read):
                print('Linha %d:' % line)
                print(read)
 
            line += 1

except(FileNotFoundError):
    print(25 * '--')
    print('Esse arquivo não existe.')
    print('Verifique o nome digitado e tente novamente!')
    print(25 * '--')