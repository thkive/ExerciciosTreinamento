lista = []

def menu():

    print("Calculadora de Notas".center(40,'-'))
    print("1 - Calcular media de um aluno ")
    print("2 - Ver tabela de classificação")
    print("3 - Ver historico de alunos")
    print("4 - Sair")
    print("-------------------------------------")

    while True:
        try:
            opcao = int(input("Digite uma opção: "))
            print("---------------------------")
            return opcao
        except ValueError:
            print("Valor invalido. Digite novamente.")

def calcular_media():

    contador = 0
    while contador < 5:
        try:
            print("------------------------------------")
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))
            nota3 = float(input("Digite a terceira nota: "))
            print("-----------------------------------")
            media = (nota1 + nota2 + nota3) / 3
            situacao = classificar_media(media)
            print (f"Aluno: {nome}, Idade: {idade}")
            print(f"Media de notas: {media:.2f}")
            print(f"Situação: {situacao}")
           
            aluno = {"nome": nome,"idade": idade, "media": media, "situacao": situacao}
            lista.append(aluno)

            contador = contador + 1
            
        except ValueError:
            print("Valores invalidos. Digite novamente.")

def classificar_media(media):

    if media < 5.0:
        return "Reprovado"
    elif media >= 5 and media < 7:
        return "Recuperação"
    elif media >= 7:
        return "Aprovado"

def mostrar_tabela():
    
    print("Tabela de Notas".center(40,'-'))
    print("Abaixo de 5   -> Reprovado")
    print("Entre 5 e 7   -> Recuperação")
    print("Acima de 7    -> Aprovado")

def mostrar_historico(lista):
    print("Historico de Alunos".center(40, '-'))

    if not lista:
        print("Nenhum aluno registrado ainda.")
    else:
        for aluno in lista():
            print(f"Nome: {aluno['nome']} |Idade: {aluno['idade']} | Media: {aluno['media:.2f']} | Situação: {aluno['situacao']}")
    print('-'*40)

def sistema():
    
    while True:
        opcao = menu()

        if opcao == 1:
            calcular_media()
        elif opcao == 2:
            mostrar_tabela()
        elif opcao == 3:
            mostrar_historico(lista)
        elif opcao == 4:
            print("Saindo do sistema. Volte sempre.")
            break
        else:
            print("Opção invalida. Tente novamente.")

sistema()