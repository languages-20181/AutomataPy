import sys


alf = list(map(str, sys.stdin.readline().strip().split(' ')))
print (alf)
q = list(map(str,  sys.stdin.readline().strip().split(' ')))

q0= input(" introduce el estado inicial ")
qf = list(map(str,  sys.stdin.readline().strip().split(' ')))

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
# stat= mt.key()
# valu = mt.values()

for i in (stra):
    print(i)
