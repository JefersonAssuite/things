
idade = int(input('Digite a sua idade: '))

sexo = input('Digite o sexo M ou F: ').lower()

cidade = input('Digite sua cidade: ')

if cidade =='rio' or cidade == 'sao paulo':

    if sexo == 'm':
        if idade < 18:
            print('Homem menor de Idade, de região Sudeste')
        else:
            print('Homem maior de idade, de região Sudeste')

    elif sexo =='f':
        if idade < 18:
            print('Mulher menor de idade, de região Sudeste')
        else:
            print('Mulher maior de idade, de região Sudeste')
    else:
        print('Erro na entrada dados')
else:
    print('teste apenas para a região sudeste')
