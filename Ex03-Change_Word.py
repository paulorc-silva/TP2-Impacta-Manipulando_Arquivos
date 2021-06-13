input_file_name = input('Arquivo entrada? ')
output_file_name = input('Arquivo saída? ')
original_word = input('Palavra original? ')
changed_word = input('Palavra alterada? ')

try:
    with open(input_file_name, 'r') as input_file:
       with open(output_file_name, 'w') as output_file:
            while(True):
                read = input_file.readline().strip().split('/')

                if(read[0] == ''):
                    break
                    
                if(original_word not in read):
                    output_file.write('%s \n' % (read[0] + '/' + read[1]))

                else:
                    for word in read:
                        if(original_word == word):
                            read.pop()    
                            read.append(changed_word) 
                            output_file.write('%s \n' % (read[0] + '/' + read[1]))
                
except(FileNotFoundError):
    print(25 * '--')
    print('O arquivo de entrada não existe.')
    print('Verifique o nome digitado e tente novamente!')
    print(25 * '--')