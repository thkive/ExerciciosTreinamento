total = 0
soma = 0
mais_populosa_valor = 0
mais_populosa_nome = ''

while True:

    cidade = input("Digite o nome da cidade: ")

    populacao_quant = input("Digite a população estimada: ")

    try:
        populacao = float(populacao_quant)
    except ValueError:
        print("Entrada invalida. Digite somente numeros.")
        continue

    total = total + 1
    soma = soma + populacao

    if populacao > mais_populosa_valor:
        mais_populosa_valor = populacao
        mais_populosa_nome = cidade

    continuar = input("Deseja continuar: ").strip().lower()

    if continuar != 's':
        print("Programa encerrado")
        break

print("\n Resultado final: ")
print(f"Total de cidades cadastradas: {total}")
print(f"A media da população: {soma/total:.3f} habitantes")
print(f"A cidade mais populosa é {mais_populosa_nome} com {mais_populosa_valor} habitantes")

