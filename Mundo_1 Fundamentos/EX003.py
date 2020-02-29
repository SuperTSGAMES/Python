"""
EXERCÍCIO 003: Dissecando uma Variável

Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""
import os
print('='*43)
print('={:12} Tipos de DADOS! {:12}='.format((''),('')))
print('='*43)

txt = input("Digite algo: ")
print("\nTipo primitivo desse valor é: ", type(txt))
print("\nSó Tem Espaço? ", txt.isspace())
print("\nÉ um Numero? ", txt.isnumeric())
print("\nÉ AlfaNumerico? ", txt.isalnum())
print("\nÉ Alfabetico? ", txt.isalpha())
print("\nEstá em Maiuscula? ", txt.isupper())
print("\nEstá em Minuscula? ", txt.islower())
print("\nEstá Capitalizada? ", txt.istitle())
os.system('pause')
