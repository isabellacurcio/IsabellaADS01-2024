#O programa
#deve, dado um salário retornar o valor do desconto proporcional ao mesmo. O cálculo de desconto
#segue a regra: o desconto deve 11% do valor do salário. Entretanto, o valor máximo de desconto é
#318,20. Sendo assim, ou o método retorna 11% sobre o salário ou 318,20.
salario= float(input('Digite o valor correspondente ao seu salário:'))
desconto=salario-(salario* 0.11)


if desconto > 318.20:
    descontofinal=salario - 318.20
    print('Seu salário com o desconto previdenciário ficou:''R$',descontofinal)

else:
    
    print('Seu sálario com desconto previdenciário ficou de ''R$',desconto)