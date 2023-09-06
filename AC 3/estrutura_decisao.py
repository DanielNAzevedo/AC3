""" AC3 
Daniel do Nascimento Azevedo
Realizado dia 06/09"""
# Exercicio 1

salario = float(input('Salário do colaborador: '))
if (salario <= 280):
    percentual = 20
elif (salario <= 700):
    percentual = 15
elif (salario <= 1500):
    percentual = 10
else:
    percentual = 5

print('Salario original: R$ ', salario)
print('Percentual: ',percentual,'%')

percentual = percentual/100.0
aumento = percentual * salario
novo_salario = salario + aumento
    
print('Aumento: R$ ',aumento)
print('Novo salário: R$ ', novo_salario)

# Exercicio 2 
num = int(input("Digite um número: "))

if num == 1:
    print("1-Domingo")
elif num == 2:
    print("2-Segunda")
elif num == 3:
    print ("3-Terça")
elif num == 4:
    print ("4-Quarta")
elif num == 5:
    print ("5-Quinta")
elif num == 6:
    print ("6-Sexta")
elif num == 7:
    print ("7-Sábado")
else:
    print ("Entrada inválida")

# Exercicio 3

# Informou 0 como parametro A ->  A = 0: Working

a = float(input("Informe o valor de A: "))

if a == 0:
    print("Informe outro valor sem ser 0")

else:
    b = float(input("Informe o valor de B: "))
    c = float(input("Informe o valor de C: "))

delta = (b ** 2) - (4 * a * c)

# Delta -> Delta é um número negativo -> A = 1 B = 5 C = 7 -> Delta = - 3: Working

if delta < 0: 
    print("A equação náo tem raizes reais.") 

else:
    x1 = (( - b + delta ** 0.5) / (2 * a))
    x2 = (( - b - delta ** 0.5) / (2 * a))

#Delta -> Se tem o resultado 0 em x1 ou x2 -> A =1 B = -6 C = 9 -> x1 e x2 = 0: Working

if delta == 0: 
    print("Essa equação possui somente uma raiz real =", x1 ,".")   

#Delta -> Se o delta for positivo -> A = 1  B = 3 C = -4: Working

else: 
    print("Essa equação possui 2 raizes reais -> x1 =", x1 ,"x2 =", x2 ,".")