import os

# basics = os.environ.get('PYTHONSTARTUP')
# if basics and os.path.isfile(basics):
#     exec(basics)

print('card'.strip('c') + ' ena')

palabra = "Hola mundo"
print(palabra[2:4])

#Compresion de listas e iteradores
print("\nCompresion de lista e iteradores")
lista = [1,4,-2,8,-1,-3]
lista2 = [num for num in lista if num > 0]
print(lista)
print(lista2)

# Usando iter y next
print("\niter y next")
my_list = [8,3,8,9,1]
my_iter = iter(my_list)
print(next(my_iter ))

# Numeros primos
numero = int(input("¿Que numero quieres saber si es primo?"))
valor = range(2,numero)
contador = 0
for n in valor:
    if numero % n == 0:
        contador += 1
        print("divisor: ", n)
if contador > 0:
    print("El numero no es primo")
else:
    print("El numero es primo")

def primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

primo(2)