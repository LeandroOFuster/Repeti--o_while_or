# Pesquisa de satisfação - TudoWeb

# Contadores
excelente = 0
ruim = 0

# Loop para 50 entrevistados (para teste, altere para 10)
total_entrevistados = 10  # TROQUE PARA 50 depois

for i in range(total_entrevistados):
    print(f"\nEntrevistado {i + 1}")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Avaliação do atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opção: "))

    # Estrutura de decisão
    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1
    elif opiniao == 2:
        pass  # Não precisa contar o "BOM"
    else:
        print("Opção inválida!")

# Resultado final
print("\n=== RESULTADO DA PESQUISA ===")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")