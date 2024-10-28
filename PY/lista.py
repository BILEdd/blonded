#indice 0 1 2 

lista_denomes = ['queiroz', 'andersson', 'renan']

print(lista_denomes)

print(lista_denomes[0])

lista_denomes[2] = ''

for bah in range(3):
    print('indice', bah)
    print(lista_denomes[bah])


lista = [
    'BAH', #0
    'VAI' , #1
    'NAO' ,#2
    'DR' , #3
    'XIU', # 4
    'coisa', #5
    'outra', # 6
    'paulo', #7
    'yout' , #8
    'positivo' , #9
    'chefe'#10
]

print(lista)

print(len(lista)) #len conta quantos objetos tem na lista

#append () adicionar um elemento no final da lista

lista.append('pode')

print(len(lista))

#index procurar algo dentro da lista

lista.index('coisa')
print(lista)

lista.remove('XIU')
print(lista)
