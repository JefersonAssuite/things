
idade = int(input('Digite a sua idade: '))

if idade >= 18 :
    print('Maior de Idade')
    idade=' Maior de idade'
    
elif idade <18:
    print('Menor de idade')
    idade = ' Menor de Idade'
    
sexo = input('Digite o sexo M ou F: ').lower()
if sexo =='m':
    print('Homem')
    
elif sexo =='f':
    print('Mulher')

if sexo =='f':
    sexo='mulher'
    
elif sexo =='m':
    sexo='Homem'

print(sexo+ idade)

