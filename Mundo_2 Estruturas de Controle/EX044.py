"""
EXERCÍCIO 044: Gerenciador de Pagamentos

Elabore um programa que calcule o valor a ser pago de um produto,
considerando o seu preço normal, e condição de pagamento:

- À vista no dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
import os
print('=' * 42)
print('={:9}Pedra, Papel e Tesoura{:9}='.format('', ''))
print('=' * 42)
compra = float(input('Qual Valor do Produto? '))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista no dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual Forma de Pagamento Voçê Deseja? '))
if opcao == 1:
    total = compra - (compra * 10/100)
elif opcao == 2:
    total = compra - (compra * 5/100)
elif opcao == 3:
    total = compra / 2
    print(f'O Valor Das Parcelas do Produto em 2x Sem Juros é: R$ {total:.2f}')
elif opcao == 4:
    juros = compra + (compra * 20 / 100)
    parcela = int(input('Em Quantas Vezes Deseja Parcelar o Produto: '))
    total = juros / parcela
    print(f'Sua compra será parcelada em {parcela}x de R$ {total:.2f} COM JUROS.')
else:
    total = compra
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print(f'Sua compra de R$ {compra:.2f} vai custar R$ {total:.2f} no final.')
#os.system('cls') or None
