informacoes = []
valid_input = False

##----------Validação Campo Sexo-----------------------
while valid_input == False:
    sexo= input('Informe o seu Sexo (M ou F): ').lower()
    
    if sexo == 'm' or sexo =='f':
        informacoes.append(sexo)
        valid_input=True
    else:
        print('Informação Inválida, digite o sexo (M ou F)')

        
##---------Validação Campo Peso ------------------------        
valid_input = False

while valid_input == False :
    peso = input('Informa qual é o seu peso: ')
    try:
        peso = float(peso)
        if peso <= 0 or peso > 350:
            print('peso inválido')
        else:
            informacoes.append(peso)
            valid_input = True
    except:
        print("Informe o peso válido, separando os decimais por '.', apenas números")
        
##------------ Validação do Campo Altura---------------------
valid_input = False

while valid_input == False:
    altura= input('Informe seu altura: ')
    try:
        altura = float(altura)
        if altura <= 0 or altura > 3:
            print('altura inválida')
        else:
            informacoes.append(altura)
            valid_input = True
    except:
        print("Informe uma altura válida, separando os decimais por '.', com apenas números")
        
##-------------------- Lógica-----------------------------------

def imc(peso,altura):
    valor_imc = peso / (altura*altura)
    return valor_imc
    

def classificacao(sexo,peso,altura):

    imcc = imc(peso,altura)
    imcc2 = str(imcc)
    imcc2 = imcc2[0:4]
    
    if sexo == 'm':
        if imcc <=20.7:
            print('Abaixo do peso IMC', imcc2)
            
        elif imcc ==20.7 or imcc <26.4:
            print('No Peso Normal IMC:', imcc2)

        elif imcc ==26.4 or imcc <=27.8:
            print('Marginalmente acima do peso IMC:', imcc2)

        elif imcc == 27.8 or imcc <=31.1:
            print('Acima do peso Ideal. IMC', imcc2)

        elif imcc >= 31.1 :
            print('Obeso', imcc2)
            
    if sexo =='f':
        if imcc <19.1:
            return"Abaixo do Peso"
        
        elif imcc == 19.1 or imcc < 25.8:
            print('No Peso Normal IMC:', imcc2)

        elif imcc == 25.8 or imcc < 27.3:
            print('Marginalmente acima do peso IMC:', imcc2)

        elif imcc == 27.3 or imcc < 32.3:
            print('Acima do peso Ideal. IMC', imcc2)
            
        elif imcc >= 32.3 :
            print('Obeso', imcc2)
            
classe = classificacao(sexo,peso,altura)

classe

input('')






