import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

BLUE = '\033[34m'
RED = '\033[31m'
YELLOW = '\033[33m'
RESET = '\033[0m'

def tabuada():
    limpar_tela()

    c = 0

    print(BLUE+"Bem vindo ao Menu".center(40,'*'))
    print(" Escolha uma opção ".center(40,'-'))
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("------------------------"+RESET)

    opcao = input(RED+"Deseja ver a tabuada de qual operador: "+RESET)
    n = int(input(RED+"Digite qual numero deseja ver a tabuada: "+RESET))
    print(BLUE+"------------------------"+RESET)

    if opcao == "1":
        for c in range(0, 11):
            resultado = n + c
            print(f"{c} + {n} = {resultado}")
                    
    elif opcao == "2":
        for c in range(0, n+1):
            resultado = n - c
            print(f"{c} - {n} = {resultado}")
    elif opcao == "3":
        for c in range(1, 11):
            resultado = n * c
            print(f"{n} x {c} = {resultado}")
    elif opcao == "4":
        for c in range(1, 11):
            resultado = n / c
            print(f"{n} / {c} = {resultado:.2f}")
    else:
        print(YELLOW+"Dados Invalidos, tente novamente!"+RESET)
    print(BLUE+"----------------------------"+RESET)
while True:
    tabuada()
    continuar = input(RED+"Deseja ver outra tabuada? (s/n): "+RESET).strip().lower()

    if continuar == 'n':
        print(YELLOW+"Programa encerrado, volte sempre!"+RESET)
        break
