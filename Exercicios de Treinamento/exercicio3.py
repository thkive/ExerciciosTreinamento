# Aqui foi aberto um função que calcula o imc de um pessoa
def menu():

    while True:
        print("Calculadora de IMC".center(40,'-'))
        print("1 - Calcular IMC")
        print("2 - Ver tabela de classificação")
        print("3 - Sair")
        print("-----------------------------------")
# esse while vai rodar o try que é para se uma pessoa digitar um valor incorreto na opçao 
# ele pede para digitar novamente se nao ele usa o break e continua o codigo
        while True:
            try:
                opcao = int(input("Digite uma opção: "))
                print("-----------------------------------")
                return opcao
            except ValueError:
                print("Entrada invalida. Digite um numero inteiro valido.")

def calcular_imc():
        
# Esse while tem a mesma função do segundo isso serve para caso o usuario digite uma letra por exemplo
    while True:
        try:
            peso = float(input("Digite se peso(kg): "))
            altura = float(input("Digite sua altura(m): "))
            imc =  peso / (altura * altura)
            print("------------------------------------")
            print(f"O valor do sei IMC é de: {imc:.2f}")
            classificar_imc(imc)
            break
        except ValueError:
            print("Digite numeros validos")
            
def classificar_imc(imc):
    if imc < 18.5:
        print("Você esta abaixo do peso")
        print("------------------------------------")
            
    elif imc >= 18.5 and imc <= 24.9:
        print("Seu peso esta normal")
        print("------------------------------------")
            
    elif imc >= 25 and imc <= 29.9:
        print("Voce esta com sobrepeso")
        print("------------------------------------")

    elif imc >= 30 and imc <= 34.9:
        print("Voce esta com obesidade grau I")
        print("------------------------------------")

    elif imc >= 35 and imc <= 39.9:
        print("Voce esta com obesidade grau II")
        print("------------------------------------")
            
    elif imc >= 40:
        print("Voce esta com obesidade grau III")
        print("------------------------------------")

def mostrar_tabela():
        
    print("Tabela de Classificação IMC")
    print("------------------------------------")
    print("Abaixo de 18.5    -> Abaixo do peso")
    print("Entre 18.5 a 24.9 -> Peso normal")
    print("Entre 25 a 29.9   -> Sobrepeso")
    print("Entre 30 a 34.9   -> Obesidade Grau I")
    print("Entre 35 a 39.9   -> Obesidade Grau II")
    print("Acima de 40       -> Obesidade III")

def sistema():
    while True:
        opcao=menu()

        if opcao == 1:
            calcular_imc()
        elif opcao == 2:
            mostrar_tabela()
        elif opcao == 3:
            print("Saindo do sistema. Volte sempre.")
            break
        else:
            print("Opção invalida. Tente novamente.")

sistema()