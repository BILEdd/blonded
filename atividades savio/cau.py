print (" vamos para sua cauculadora ")
print(" coloque A para +, B para - , C para *, D para / ")
print (" agora coloque seus numeros") 
numero1 = float (input ("numero um : "))
numero2 = float(input("numero dois : "))
o = str(input("oque vocé quer :  "))
if o == "a" or o == "A" :
    soma = numero1 + numero2
    print (soma) 
elif o == "b" or o == "B" :
    soma = numero1 - numero2
    print (soma) 
elif o == "c" or o == "C" :
    soma = numero1 * numero2
    print (soma) 
elif o == "d" or o == "D" :
    soma = numero1 / numero2
    print (soma) 
else :
    print ("brinca direito")