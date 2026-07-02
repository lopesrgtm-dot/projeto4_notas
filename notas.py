def nota_eh_valida(nota):
    if nota < 0 or nota > 10:
        return False
    return True


boletim = []

while True:
    print("1 Adicionar Nota")
    print("2 Ver Média")
    print("3 Sair")
    
    opcao = int(input(" Digite uma opção: "))
    

    
    if opcao == 3 :
        print("Saindo...")
        break       
    
    elif opcao == 1:
        nota = float(input("Digite a nota: "))

        if nota < 0 or nota > 10:
            print("Nota inválida!")
        else:
            boletim.append(nota)
        
    elif opcao == 2:
        print("Calculando média...")

    if len(boletim) == 0:
        print("Nenhuma nota cadastrada ainda")
            
    else:
        media = sum(boletim) / len(boletim)
        if media >= 7:
            print(f"Média: {media:.2f} - Situação: Aprovado!")
        else:
            print(f"Média: {media:.2f} - Situação: Reprovado!")
          
