#!/bin/bash

echo "Digite a operação desejada: (+, -, *, /): "
read operacao

echo "Digite o primeiro número: "
read num1

echo "Digite o segundo número: "
read num2

resultado=$(echo "$num1 $operacao $num2" | bc)

echo "Resultado: $resultado"
