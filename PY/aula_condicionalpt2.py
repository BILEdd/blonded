print ("MENU - CAUCULADORA")
print ('A - somar')
print (' B - Subtrair ')
print("C-multiplicar ")
print("D- dividir ")
opcao=input("escolha uma das letras : ")
print( " a opcao escolhida foi:", opcao )
if opcao == "a" or opcao == "A":
    print ("somar")
elif opcao == "b" or opcao == "B":
    print("subtrair")
elif opcao == "c" or opcao == "C":
    print  ("multiplicar")
elif opcao == "d" or opcao == "D":
    print ("dividir")
else:
    print ( "usa direito por favor")