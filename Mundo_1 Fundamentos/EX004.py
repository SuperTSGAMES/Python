#Exercicio Operadores Aritmeticos
import os
print('='*44)
print('={:9} Operadores Aritmericos {:9}='.format((''),('')))
print('='*44)
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro Valor: "))
s = n1 - n2
a = n1 + n2
m = n1 * n2
div = n1 / n2
divint = n1 // n2
pot = n1 ** n2
restdiv = n1 % n2

print(f'\nA Soma Entre {n1} e {n2} é: {a}\nA Subtração Entre {n1} e {n2} é: {s}\nA Multiplicaçao Entre {n1} e {n2} é: {m}')
print(f'A Divisao Entre {n1} e {n2} é: {div}\nA Divisao Inteira Entre {n1} e {n2} é: {divint}\nA Potencia Entre {n1} e {n2} é: {pot}\nO resto Da Divisao Entre {n1} e {n2} é: {restdiv}')
os.system('pause')
