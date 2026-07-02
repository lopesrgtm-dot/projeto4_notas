def nota_eh_valida(nota):
    if nota < 0 or nota > 10:
        return False
    return True

def calcular_media(lista_de_notas):
    if len(lista_de_notas) == 0:
        return 0.0

    media = sum(lista_de_notas) / len(lista_de_notas)
    return media


def fluxo_gestor_notas():
        
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

            if not nota_eh_valida(nota):
                    print("Nota inválida! Digite entre 0 e 10.")
            else:
                    boletim.append(nota)
                    print("Nota cadastrada.")
            
        elif opcao == 2:
            media = calcular_media(boletim)
            print("Calculando média...")

        if len(boletim) == 0:
            print("Nenhuma nota cadastrada ainda")
                
        else:
            media = sum(boletim) / len(boletim)
            if media >= 7:
                print(f"Média: {media:.2f} - Situação: Aprovado!")
            else:
                print(f"Média: {media:.2f} - Situação: Reprovado!")

if __name__ == "__main__":
    fluxo_gestor_notas()

          
