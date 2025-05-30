def sapo_game():

    pedra_atual = 1

    while pedra_atual < 4:

        print(f"O sapo esta na pedra {pedra_atual}")

        prox_pedra = input("Digite o numero da proxima pedra: ")

        if prox_pedra.isdigit():
            proxima_pedra = int(prox_pedra)

        else:
            print("Entrada invalida. Digite numeros inteiros.")
            continue

        if proxima_pedra > pedra_atual + 1:
            print("Voce falhou. O sapo caiu na agua.")
            break

        else:
            print("Pulo correto.")
            pedra_atual = proxima_pedra
    
        if pedra_atual == 4:
            print("Parabens você chegou ao final.")

sapo_game()

        