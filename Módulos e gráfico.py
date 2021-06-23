import time
import timeit
import matplotlib.pyplot as plt

entradas = []
rep = []
legenda = []
repet = 7

repeticao = 1

print('Este programa marcará o tempo gasto para digitar a palavra PROGRAMAÇÃO. Você terá que digitar',str(repet),'vezes')

input('Aperte enter Para Começar.')

while repeticao <= repet:
    inicio = time.time()
    input('Uma Palavra Qualquer: ')
    fim= time.time()
    tempo = fim-inicio
    tempo = round(tempo,2)
    rep.append(repeticao)
    entradas.append(tempo)
    vezstr = str(repeticao)+'a vez'
    legenda.append(vezstr)
    repeticao = repeticao +1

plt.plot(rep,entradas)

plt.xticks(rep,legenda)
plt.plot(rep,entradas)
plt.show()
    
    

    

