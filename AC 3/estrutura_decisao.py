""" AC3 
Daniel do Nascimento Azevedo
Realizado dia 06/09"""
# Exercico 1 
def sal():
    salario = float(input("informe o salário do colaborador: "))
    if(salario <= 280):
        percentual = 20
    elif(salario <= 700):
        percentual = 15
    elif(salario <= 1500):
        percentual = 10
    else:
        percentual = 5

    print("Salário sem aumento: R$ ", salario ,".")
    print("Percentual de aumento:", percentual,"%")

    percentual = percentual / 100.00
    aumento = percentual * salario 
    nova_salario = salario + aumento 

    print("Aumento: R$" ,aumento)
    print("Novo salário: R$:", nova_salario)
sal()


# Exercicio 2
def função():
        num = int(input("Digite um número: "))

        if num == 1:
            print("Domingo")
        elif num == 2:
            print("Segunda")
        elif num == 3:
            print ("Terça")
        elif num == 4:
            print ("Quarta")
        elif num == 5:
            print ("Quinta")
        elif num == 6:
            print ("Sexta")
        elif num == 7:
            print ("Sábado")
        else:
            print ("Entrada inválida")
função()

def baskara():
        a = float(input("Informe o valor de A: "))

        if a == 0:
            print("Informe outro valor sem ser 0")

        else:
            b = float(input("Informe o valor de B: "))
            c = float(input("Informe o valor de C: "))

        delta = (b ** 2) - (4 * a * c)

    
        if delta < 0: 
            print("A equação náo tem raizes reais.") 

        else:
            x1 = (( - b + delta ** 0.5) / (2 * a))
            x2 = (( - b - delta ** 0.5) / (2 * a))

    

        if delta == 0: 
            print("Essa equação possui somente uma raiz real =", x1 ,".")   



        else: 
            print("Essa equação possui 2 raizes reais x1 =", x1 ,"x2 =", x2 ,".")
baskara()