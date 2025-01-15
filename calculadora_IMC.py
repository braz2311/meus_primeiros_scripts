#!/bin/bash
#Calculadora_IMC

Alturacm = float(input("Por favor digite a sua altura em cm: "))
Peso = float(input(" Por favor, digite o seu peso em kg: "))
Altura = Alturacm /100
IMC = Peso / (Altura ** 2) 
print("seu IMC é: ", IMC)
if IMC < 18.5:
  print("Abaixo do peso")
elif 18.5 <= IMC < 25:
  print("Voce está com o peso normal")
else:
  print(" Voce está acima do peso")
