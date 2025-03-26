#Ejercicio 1
print("Hola Mundo")

#Ejercicio 2
nombre = input("Ingrese su nombre: ")

print(f"Hola {nombre}")

#Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugarDeResidencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años de edad y vivo en {lugarDeResidencia}")

#Ejercicio 4
import math

radio = float(input("Ingrese el radio de un círculo: "))
pi = math.pi
perimetro = round((2 * pi * radio),2)
area = round((pi * radio ** 2),2)

print(f"El perímetro del círculo es: {perimetro} y su área es: {area}")

#Ejercicio 5
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

print(f"Horas: {horas}, Minutos: {minutos}, Segundos: {segundos}")

#Ejericio 6
numero = int(input("Ingrese un número: "))

for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")

#Ejercicio 7
numero1 = int(input("Ingrese un número distinto de 0: "))
numero2 = int(input("Ingrese otro número distinto de 0: "))

if numero1 == 0 or numero2 == 0:
    print("Los números deben ser distintos de 0")
else:
  print(f"{numero1} + {numero2} = {numero1 + numero2}")
  print(f"{numero1} - {numero2} = {numero1 - numero2}")
  print(f"{numero1} x {numero2} = {numero1 * numero2}")
  print(f"{numero1} / {numero2} = {round((numero1 / numero2),2)}")

#Ejercicio 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilos: "))
imc = round((peso / altura ** 2),2)

print(f"Su índice de masa corporal es: {imc}")

#Ejercicio 9
temperaturaEnCelsius = float(input("Ingrese una temperatura en grados Celsius: "))
temperaturaEnFahrenheit = round((temperaturaEnCelsius * 9/5 + 32),2)

print(f"La temperatura en grados Fahrenheit es: {temperaturaEnFahrenheit}")

#Ejercicio 10
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))
numero3 = int(input("Ingrese otro número: "))
promedio = round(((numero1 + numero2 + numero3) / 3),2)

print(f"El promedio de los números ingresados es: {promedio}")
