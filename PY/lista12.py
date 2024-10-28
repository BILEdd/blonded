lista =  [1,23,4,5,6,7,8,9,]


acumuladora = 0

for x  in range (len(lista)):

    valor = lista[x]
    # função de loop, onde a acumuladora vai pegando o valor e somando ate o limite
    acumuladora += valor


print ("a soma da lista", acumuladora)
    
 
