import sys

print (" introduce un alfabeto,  separado por espacios: ")
alf = list(map(str, sys.stdin.readline().strip().split(' ')))
print (alf)

print ("ingrese estados (separados por espacios): ")
q = list(map(str,  sys.stdin.readline().strip().split(' ')))
print (q)

print (" introduce el estado inicial: ")
q0= input()


print (" estado final/es separados por espacios: ")
qf = list(map(str,  sys.stdin.readline().strip().split(' ')))
print (qf)

mt={}


for i in range(len(q)):
    for j in range(len(alf)):
        print ("del estado " + q[i] + " con el simbolo '" + alf[j] + "' a que estado llega")
        aux = input()

        if q[i] in mt:
            mt[q[i]][alf[j]] = aux

        else:
            mt[q[i]]= {alf[j]:aux}

while 1:
    print ("\n ingrese cadena a evaluar por el automata")

    stra= input ()

    state = q0
    for i in stra:
        state = mt[state][i]
    if state in qf:
        print (" cadena aceptada, MUY BIEN! ")
    else:
        print (" cadena no aceptada ")

    print("")
    print("desea evaluar otra cadena (y/n)")
    opt = input()
    if opt == "y":
        continue
    else:
        break
