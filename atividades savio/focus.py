num = int(input("coloque o valor da sua repetição  "))
acu = 0
acu1 = 1
a = 0 
for x in range (1, num + 1):
    acu += acu + acu1
    acu1 += acu
    

    print(acu1)