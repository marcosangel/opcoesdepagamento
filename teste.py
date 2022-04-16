print('='*31)
print('OPÇÕES DE PAGAMENTO')
print('='*31)
preço = float(input('Valor total das compras:R$'))
if preço > 0:
    print('''FORMAS DE PAGAMENTO
    [ 1 ] À vista dinheiro/cheque, 10% desconto
    [ 2 ] À vista no cartão, 5% desconto
    [ 3 ] 2x no cartão, preço normal
    [ 4 ] 3x ou mais no cartão, 20% juros''')
    opção = int(input('Digite a opção que deseja: '))
    if opção == 1:
        total = preço - (preço * 10 / 100)
    elif opção == 2:
        total = preço - (preço * 5 / 100)
    elif opção == 3:
        total = preço
        parcela = total / 2
        print('Sua compra será parcelada em 2x de R${:.2f}, sem juros!'.format(parcela))
    elif opção == 4:
        total = preço + (preço * 20 / 100)
        parc = int(input('Quantas parcelas?: '))
        parcela = total / parc
        print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(parc,parcela))
    else:
        print('Opção INVALIDA! Tenta novamente')
    print('Voce pagará o valor total de R${:.2f}'.format(total))
else:
    print('Valor da compra deve ser maior que 0,00')


