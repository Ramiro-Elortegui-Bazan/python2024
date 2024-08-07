#Escribe un programa que solicite al usuario ingresar 10 números y luego imprima una lista con los números pares ingresados
numeros=[]
for i in range(10):
        numero = int(input(f"Ingresa el número {i + 1}: "))
        numeros.append(numero)
NumerosPares=[num for num in numeros if num % 2==0] 
print (("los numeros pares son "),NumerosPares)