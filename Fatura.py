repetir = 's'
fatura= []
total = 0
valid_preco = False

while repetir == 's':
        produto = input('Digite o nome do Produto: ')
        
        while valid_preco == False:
                preco = (input('Digite o preco do Produto: '))
                try:
                        preco = float(preco)
                        
                        if preco <= 0:
                                print('O preço precisa ser maior que zero')
                        else:
                                valid_preco = True
                        
                except:
                        print("Formato de preço inválido. Use apenas números e separe os centavos com'.'.")

        fatura.append([produto,preco])
        total += preco
        valid_preco = False
        repetir = input('Deseja comprar mais algusn produtos? (S ou N) ').lower()

for i in fatura:
        print(i[0],'-', i[1])

print('O total da sua fatura é:', total)
