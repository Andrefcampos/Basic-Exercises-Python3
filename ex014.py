#Calculadora de aumento de salário com 15% de aumento

sal = float(input('Informe o salário do funcionário: R$'))

print('O salário do funcionário é R${:.2f} \nCom um aumento de 15% o novo salário passa a ser de R${:.2f}'.format(sal, sal+(sal*0.15)))