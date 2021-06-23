print('Calculo de Média Ponderada')

peso1 = float(input('Digite o valor do peso da prova1: '))
nota1= float(input('Digite a nota do aluno na prova1: '))
    
peso2 = float(input('Digite o valor do peso da prova2: '))
nota2= float(input('Digite a nota do aluno na prova2: '))

resultadonota1 = nota1*peso1

resultadonota2 =nota2*peso2

numerador= resultadonota1+resultadonota2

pesos = peso1+peso2

dividir = numerador/pesos

print('A média é',dividir)




    


