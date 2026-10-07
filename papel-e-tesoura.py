import random

#pedra papel e tesoura
#melhor de 5
#placar de ser mostrado após cada jogada
#empates não contam como rodadas e devem ser contabilizados
# 1 = pedra |2 = papel |3 = tesoura

def placar():
    print(f"""Jogador | [{pontos_jogador[0]}] | [{pontos_jogador[1]}] |[{pontos_jogador[2]}] |
Maquina | [{pontos_maquina[0]}] | [{pontos_maquina[1]}] | [{pontos_maquina[2]}] |""")
   

while True:
    print("""Começo do torneio, meus parabens, você irá enfrentar a maquina
Um oponente que não irá ler seus movimentos nem nada, que você pode usar probabilidade para vencer...
...embora a probabilida costume te trair nesses momentos
                BOA SORTE!!!!!""")
    pontos_jogador = ["O","O","O"]
    pontuacao_j = 0
    pontos_maquina = ["O","O","O"]
    pontuacao_m = 0
    empates = 0
    empate = False
    contador = 0

    while True:
        contador += 1
        print(f"Rodada {contador}")
        
        if empate == True:
            print("Denovo...")
        escolha = input("ESCOLHA\n* 1 - PEDRA\n* 2 - PAPEL\n* 3 - TESOURA\n* Sair = desistir\n:  ").lower()
        escolha_maquina = random.randint(1,3)

        match escolha:
            case "1":
                escolha = "PEDRA"
            case "2":
                escolha = "PAPEL"
            case "3":
                escolha = "TESOURA"
            case "sair" | "s":
                placar()
                break
            case _:
                print("Isso não existe, ESCOLHE DE NOVO")
                continue
        
        match escolha_maquina:
            case 1:
                escolha_maquina = "PEDRA"
            case 2:
                escolha_maquina = "PAPEL"
            case 3:
                escolha_maquina = "TESOURA"


        if escolha == escolha_maquina:
            print("EMPATE!!")
            print(f"Foi {escolha} contra {escolha_maquina}")
            placar()
            empates += 1
            continue
        elif escolha == "PEDRA" and escolha_maquina == "TESOURA":
            print("O JOGADOR GANHOU A RODADA")
            print(f"Foi {escolha} contra {escolha_maquina}")
            pontos_jogador[pontuacao_j] = "X"
            pontuacao_j += 1
        elif escolha == "PEDRA" and escolha_maquina == "PAPEL":
            print("A MAQUINA LEVOU A RODADA")
            print(f"Foi {escolha} contra {escolha_maquina}")
            pontos_maquina[pontuacao_m] = "X"
            pontuacao_m += 1
        elif escolha == "PAPEL" and escolha_maquina == "TESOURA":
            print("A MAQUINA LEVOU A RODADA")
            print(f"Foi {escolha} contra {escolha_maquina}")
            pontos_maquina[pontuacao_m] = "X"
            pontuacao_m += 1
        elif escolha == "PAPEL" and escolha_maquina == "PEDRA":
            print("O JOGADOR GANHOU A RODADA")
            print(f"Foi {escolha} contra {escolha_maquina}")
            pontos_jogador[pontuacao_j] = "X"
            pontuacao_j += 1
        elif escolha == "TESOURA" and escolha_maquina == "PAPEL":
            print("O JOGADOR GANHOU A RODADA")
            print(f"Foi {escolha} contra {escolha_maquina}")
            pontos_jogador[pontuacao_j] = "X"
            pontuacao_j += 1
        else: #A unica opção restante é tesoura e pedra
            print("A MAQUINA LEVOU A RODADA")
            print(f"Foi {escolha} contra {escolha_maquina}")
            pontos_maquina[pontuacao_m] = "X"
            pontuacao_m += 1
        
        placar()
        
        if pontuacao_j == 3:
            print("O JOGADOR VENCEU A PARTIDA!!!")
            print(f"Foram {empates} empates, terminando na rodada{contador}")
            placar()
            continuar = input("Deseja jogar novamente?(S/N)\n").lower()
            if continuar == "n" :
                print("Até a próxima")
            else:
                print("Vamos la")
            break
        elif pontuacao_m == 3:
            print("A MAQUINA VENCEU A PARTIDA!!!")
            print(f"Foram {empates} empates, terminando na rodada{contador}")
            placar()
            continuar = input("Deseja jogar novamente?(S/N)\n").lower()
            if continuar == "n" :
                print("Até a próxima")
            else:
                print("Vamos la")
            break
        
        empate = False
    if continuar == "n":
        break
    if escolha == "sair":
        break