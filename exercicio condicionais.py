nome =  input('Digite o nome do aluno: ')

validacao = False

##------------------ Validação Campo Faltas -----------------

validacaofalta = False

while validacaofalta == False:
    faltas = input('Digite o total de faltas do aluno: ')
    try:
        faltas = int(faltas)
        if faltas < 0 or faltas > 20 :
            print('Numero de faltas inválido, valor deve ser entre 0 e 20 ')
        else:
            validacaofalta = True
    except:
        print('Faltas só serão marcadas por números inteiros')
    

##------------------Validacao 1 Campo -----------------------

while validacao == False :
    
    nota1 = input('Digite o valor da nota 1: ')
    
    
    try:
        nota1= float(nota1)
        
        if nota1 <0 or nota1 >10 :
            print('Erro digite um valor entre zero e dez')
        
        else:
            validacao=True
            
    except:
                print('Use apenas números e separe os decimais com ponto.(Ex 9.5)!')
                
##-----------------Validação 2 campo--------------------

validacao2 = False

while validacao2 == False:
    
    nota2 = input('Digite o valor da nota 2: ')
    try:
        nota2= float(nota2)
        if nota2 < 0 or nota2 > 10:
            print('Erro! Digite um valor entre zero e dez')
        else:
            validacao2= True
                    
    except:
        print('Use apenas números e separe os decimais com ponto.(Ex 9.5)!')
        
##-----------------Lógica---------------------------------        
print('Tudo Validado')

presente= 20-faltas

presenca=(presente/20)*100

media= (nota1+nota2)/2

if presenca > 70.0 and media > 6 :
    resultado = 'Aluno Aprovado'
    
elif presenca >= 70.0 and media <6:
    resultado =' Reprovador por média'
    
elif presenca< 70.0 and media > 6:
    resultado = 'Reprovado por faltas'
    
elif presenca < 70.0 and media < 6:
    resultado =  'Aluno reporvador por média e presenças'
    
else:
    print('Erro de dados, Favor refazer os lançamentos')

print('')
print('Nome:', nome)
print('Média:', media)
print('Assiduidade:',presenca,'%')
print('Resultado:', resultado)


