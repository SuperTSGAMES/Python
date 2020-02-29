"""
EXERCÍCIO 010: Conversor de Moedas

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.

"""
import os
print('='*43)
print('={:10} CONVERSOR DE MOEDAS {:10}='.format((''),('')))
print('='*43)
n1 = float(input('\nQuanto Dinheiro tem Na Carteira? R$ '))
usd = n1 / 4.39 #converte REAL para DOLAR
eur = n1 / 4.76 #converte REAL para EURO
jpy = n1 / 0.04 #Converte REAL pra IENE JAPAO
gbp = n1 / 5.69 #Converte REAL pra Libra Esterlina
aud = n1 / 2.91 #Converte REAL pra Dolar Australiano
cad = n1 / 3.32 #Converte REAL pra Dolar Canadense
chf = n1 / 4.49 #Converte REAL pra Franco Suiço
cny = n1 / 0.62 #Converte REAL pra Yaun Chines
print(f'\nVoce tem R$ {n1:.2f} e consegue compra USD: {usd:.2f} Dólar Americano')
print(f'Voce tem R$ {n1:.2f} e consegue compra EUR: {eur:.2f} Euro')
print(f'Voce tem R$ {n1:.2f} e consegue compra JPY: {jpy:.2f} Iene Japonês')
print(f'Voce tem R$ {n1:.2f} e consegue compra GBP: {gbp:.2f} Libra Esterlina')
print(f'Voce tem R$ {n1:.2f} e consegue compra AUD: {aud:.2f} Dólar Australiano')
print(f'Voce tem R$ {n1:.2f} e consegue compra CAD: {cad:.2f} Dólar Canadense')
print(f'Voce tem R$ {n1:.2f} e consegue compra CHF: {chf:.2f} Franco Suiço')
print(f'Voce tem R$ {n1:.2f} e consegue compra CNY: {cny:.2f} Yuan Chinês')
os.system('pause')
