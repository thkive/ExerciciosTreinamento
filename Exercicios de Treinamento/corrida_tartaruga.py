import time
import os

RED = '\033[31m'
YELLOW = '\033[33m'
RESET = '\033[0m'

def animacao_tartaruga():
    pista = ["_"] * 20
    for i in range(len(pista)):
        pista[i] = "🐢"
        print("".join(pista))
        pista[i] = "_"
        time.sleep(0.1)
        os.system("cls" if os.name == "nt" else "clear")

def corrida_tartaruga():

    animacao_tartaruga()

    posicao_atual = 0

    print(RED+"CORRIDA DE TARTARUGA".center(40, '-')+RESET)

    while posicao_atual < 5:

        print(YELLOW+f"A tartaruga percorreu {posicao_atual} metro(s)."+RESET)
        print("------------------------------------------------")

        proxima_posicao = input(YELLOW+"Digite o proximo metro a ser percorrido: "+RESET)

        if not proxima_posicao.isdigit():
            print(RED+"Valor invalido. Digite numeros inteiros."+RESET)
            continue    
            
        prox_posicao = int(proxima_posicao)
       
        if prox_posicao > 5:
            print(RED+"Esse metro não existe. A pista só vai até 5."+RESET)
            break

        if prox_posicao != posicao_atual + 1:
            print(RED + "A tartaruga errou o caminho e se perdeu." + RESET)
            print("--------------------------------------------")
            break        

        posicao_atual = prox_posicao 
    
        if posicao_atual == 5:
            print(YELLOW + f"A tartaruga percorreu {posicao_atual} metros." + RESET)
            print(RED + "*" * 46)
            print("Parabéns! Você guiou a tartaruga até o fim!")
            print("*" * 46 + RESET)

corrida_tartaruga()

