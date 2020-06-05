#NOME: LEONARDO ANDRADE
#DATA: 23/04/2019
#DESCRIÇAO: 

print('Entre com o valor do salário bruto', end =  ': ')
salBruto = float(input())

print('Entre com o desconto do Imposto de Renda (porcentagem)', end = ': ')
valor_IR = float(input())

print('Entre com o desconto do INSS', end = ': ')
valor__INSS = float(input())

print('Entre com o valor do Auxilio Moradia', end = ': ')
moradiaValue = float(input())

print ('Entre com o valor do Auxílio Alimentação', end = ': ')
alimentValue = float(input())

print()

print ('*********************************************************')

print ('Salario Bruto                           = ',salBruto)

print ('*********************************************************')

print('DESCONTOS')

if salBruto < 2500 :
    desc_IR = 0

elif 6500 > salBruto >= 2500 :
    desc_IR = (18 * salBruto) / 100

elif salBruto >= 6500 :
    desc_IR = (27.5 * salBruto) / 100

print('Imposto de Renda                         = ',desc_IR)

desc_INSS = (11 * salBruto) / 100

if 600 >= desc_INSS :
    print('Previdencia Social                       = ',desc_INSS)

else:
    print('Previdencia Social                       = ', 600)

print()

print('Auxílios')
print('Moradia                                  = ',moradiaValue)
print('Alimetação                               = ',alimentValue)

print('**********************************************************')

if 600 >= desc_INSS : 
    salLiquido = salBruto - desc_IR - desc_INSS + moradiaValue + alimentValue

else :
    salLiquido = salBruto -desc_IR - 600 + moradiaValue + alimentValue

print('Salário Líquido                          = ', salLiquido)
