# Solicita a avaliação do usuário
avaliacao = int(input("Insira a avaliação do filme (1 a 5): "))

# Imprime a mensagem correspondente à avaliação
if avaliacao == 5:
    print("Excelente!")
elif avaliacao == 4:
    print("Muito Bom!")
elif avaliacao == 3:
    print("Bom!")
elif avaliacao == 2:
    print("Regular.")
elif avaliacao == 1:
    print("Ruim.")
else:
    print("Avaliação inválida. Por favor, insira um valor entre 1 e 5.")
