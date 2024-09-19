# Recebe a data do usuário
data = input("Digite a data no formato DD-MM-AAAA: ")

# Verifica se a data está no formato correto (DD-MM-AAAA)
if len(data) == 10 and data[2] == '-' and data[5] == '-':
    # Extrai dia, mês e ano da string de data
    dia = int(data[0:2])  # Pega os primeiros 2 caracteres e converte para inteiro
    mes = int(data[3:5])  # Pega os caracteres do meio (3 e 4) e converte para inteiro
    ano = int(data[6:10])  # Pega os últimos 4 caracteres e converte para inteiro

    # Verifica se o mês é válido (entre 1 e 12)
    if 1 <= mes <= 12:
        # Verifica se o dia é válido para meses com 31 dias
        if mes in [1, 3, 5, 7, 8, 10, 12] and 1 <= dia <= 31:
            print("A data é válida ")
        # Verifica se o dia é válido para meses com 30 dias
        elif mes in [4, 6, 9, 11] and 1 <= dia <= 30:
            print("A data é válida ")
        # Verifica se o dia é válido para fevereiro
        elif mes == 2:
            # Verifica se o ano é bissexto
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                # Ano bissexto: fevereiro tem 29 dias
                if 1 <= dia <= 29:
                    print("A data é válida ")
                else:
                    print("A data não é válida ")
            else:
                # Ano não bissexto: fevereiro tem 28 dias
                if 1 <= dia <= 28:
                    print("A data é válida: ")
                else:
                    print("A data não é válida ")
        else:
            # Se o mês não for válido
            print("A data não é válida ")
    else:
        # Se o mês não estiver entre 1 e 12
        print("A data não é válida ")
else:
    # Se a data não estiver no formato correto
    print("A data não é válida ")
