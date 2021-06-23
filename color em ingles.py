cores = {'verde':'green','vermelho':'red'}

cor = input('Digite uma cor em português: ').lower()

traducao = cores.get(cor,'Esta cor não consta')

print(traducao)



