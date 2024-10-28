#de celcius para faremhaint
print("de celcius para farenhaints ou ó contrario")
print("C - de celcius para farenhaint")
print("F - de farenhait para celsius ")

opcao= input("sua opção: ")

if opcao == "c" or opcao == "C" :
    C=  float(input("coloque o valor de celsius: "))

    F = float( C * 1.8 + 32 )

    print (F)
elif opcao == "F" or opcao == "f" :
    F = float(input("coloque o valor de farenhait: "))
    C = float ((F-32)/1.8)
    print (C)