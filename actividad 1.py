#Ejercicio 1
numeros=[6,2,3,4,5,8,9]

cuadrados=[numero ** 2 for numero in numeros]

print("Lista de numeros elevados al cuadrado", cuadrados)

#Ejercicio 2 string

nombre="pepe"
edad=29

mensaje=f"Hola, mi nombre es {nombre} y tengo {edad} años"

print(mensaje)


#Ejercicio 3 booleanos

edad=71
 
if edad >=18:
    print("Eres mayor de edad :)")
else:
    print("Eres menor de edad :()")

#Ejercicio 4 while y float

saldo=200.0
while saldo >10:
    retiro=14.0
    saldo -=retiro #saldo menos retiro
    print(f" se ha retirado {retiro}, saldo actual: {saldo}")

# Ejercicio 5 Uso de diccionarios y cadenas

persona={"nombre":"Anubis",
         "edad": 17,
         "ciudad": "Madrid"
}

for clave, valor in persona.items():
    print(f"{clave.capitalize()}:{valor}")
