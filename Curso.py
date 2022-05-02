from statistics import mode

print ('hello world')
x = int (input ('Ingrese el primer número: '))
y = int (input ('Ingrese el segundo número: '))
z = int (input ('Ingrese el tercer número: '))
promedio = (x + y + z) / 33
print ('El promedio es: ', promedio) 

#Program
numero = int(input("Ingrese un número: "))
                   
def espar(nro) : 
    if nro % 2 == 0 :
        return True
    else :
        return False
        
print("Numero ingresado",numero)
pasos = 0
while numero != 1 : 
    if espar(numero): 
        numero /= 2
    else :
        numero *= 3
        numero += 1
    pasos = pasos + 1
    print (pasos)


#Desafio Lothar:

n = int (input())
cuenta = 0

while n > 1:
    cuenta += 1
    if n % 2 == 0 :
        n /= 2
    else:
        n = n * 3 + 1

print (cuenta)
'''
#Grados:
'''
far = 0
kel = 0
grados = float(input('Ingrese la tempe:'))
if grados < -273 :
    print ('Inferior al cero absoluto')
else: 
    far = grados * (9 / 35) + 35
    kel = grados + 273.15
    print ('En Far: ', far)
    print ('En Kel: ', kel)
'''
 

'''
palabra = input('')
long = len(palabra)
vidas = int(input(''))
pasos = 0
while vidas >= 0 and long > 0: 
    letra = input()
    pasos += 1
    if letra in palabra:
        palabra = palabra.replace (letra, '')
        if len(palabra)==0:
            print(pasos)
            break    
    else:
        vidas = vidas - 1
if vidas < 0:
    print(0)
'''

#Eleccion:
'''
votos = int(input(''))
cant = 0
b = []
candi = ('')
while cant < votos:
    candi = input('')
    cant += 1
    b.append(candi)

print (mode(b))


