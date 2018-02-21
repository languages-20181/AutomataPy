import sys

print (" introduce un alfabeto,  separado por espacios: ")
alf = list(map(str, sys.stdin.readline().strip().split(' ')))
print (alf)

print ("estados (separados por espacios): ")
q = list(map(str,  sys.stdin.readline().strip().split(' ')))
print (q)

q0= input(" introduce el estado inicial: ")
print (q0)

print (" estado final/es separados por espacios: ")
qf = list(map(str,  sys.stdin.readline().strip().split(' ')))
print (qf)

mt={}


for i in range(len(q)):
    for j in range(len(alf)):
        print ("del estado " + q[i] + " con el simbolo " + alf[j] + " a que estado llega")
        aux = input()

        if q[i] in mt:
            mt[q[i]][alf[j]] = aux

        else:
            mt[q[i]]= {alf[j]:aux}
print ("ingrese cadena a evaluar ")

stra= input ()

state = q0
for i in stra:
    state = mt[state][i]
if state in qf:
    print (" cadena aceptada, FELICIDADES! ")
else:
    print (" cadena no aceptada ")
