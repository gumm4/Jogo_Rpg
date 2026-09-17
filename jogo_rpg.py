import random

def contagem_inimigos(inimigos, pontos_inimigos):
    if inimigos < 10:
        pontos_inimigos += 10
        print(f"Você ganhou 10 pontos!\nSeu total de pontos é: {pontos_inimigos}\n")
    elif 10 <= inimigos <= 29:
        pontos_inimigos += 30
        print(f"Você ganhou 30 pontos!\nSeus pontos atuais são: {pontos_inimigos}\n")
    else:
        pontos_inimigos += 50
        print(f"Você ganhou 50 pontos!\nSeu total de pontos atual é: {pontos_inimigos}\n")

    return pontos_inimigos

def contagem_inimigos_perda_vida(inimigos, pontos_inimigos, vida):
    if inimigos < 10:
        pontos_inimigos += 10
        vida -= 15
        print(f"Você ganhou 10 pontos!\nSeu total de pontos é: {pontos_inimigos} pontos\n\nE perdeu 15 pontos de vida\nSeus pontos de vida atuais são: {vida}%")
    elif 10 <= inimigos <= 29:
        vida -= 20
        pontos_inimigos += 30
        print(f"Você ganhou 30 pontos!\nSeus pontos atuais são: {pontos_inimigos} pontos\n\nE perdeu 20 pontos de vida\nVocê tem {vida}% restantes\n")
    else:
        vida -= 25
        pontos_inimigos += 50
        print(f"Você ganhou 50 pontos!\nSeu total de pontos atual é: {pontos_inimigos} pontos\n\nE perdeu 25 pontos de vida\nVocê tem {vida}% restantes\n")

    return pontos_inimigos, vida

def luta_chefe(vida, vida_chefe, d_20, numeros_objetivos, pontos_inimigos, contagem_mortes):
    d_6_chefe = random.randint(1, 6)
    print(f"O chefe rolou {d_6_chefe} na rolagem")
    
    if d_6_chefe >= 3 or d_20 == 6:
        vida -= 20
        print(f"O chefe te deu um ataque super efetivo!\nVocê perdeu 20 de vida\nVida atual: {vida}\n")
    else:
        vida -= 15
        print(f"O ataque do chefe não foi tão efetivo\nVocê perdeu 15 de vida\nVida atual: {vida}\n")

    if vida <= 0:
        contagem_mortes += 1
        print(f"Você morreu para o chefe!\nContagem de mortes: {contagem_mortes}\n")
        return vida, vida_chefe, numeros_objetivos, contagem_mortes

    rolagem = int(input("Rolar os dados?\n1-Sim\n2-Não\nOpção: "))

    if rolagem == 1:
        d_6 = random.randint(1, 6)
        print(f"Você rolou {d_6} na rolagem de dados\n")

        if d_6 >= 3 or d_20 == 6:
            dano = 50
        else:
            dano = 40

        vida_chefe -= dano
        print(f"Você deu {dano} de dano no chefe\nVida Chefe: {vida_chefe}\n")

        if vida_chefe <= 0:
            numeros_objetivos += 1
            print(f"Você derrotou o chefe!\nObjetivos concluídos: {numeros_objetivos}\n")

            if 1 <= numeros_objetivos <= 2:
                contagem_objetivos = 25
            else:
                contagem_objetivos = 60

            contagem_total = pontos_inimigos + contagem_objetivos
            print(f"Sua pontuação total é {contagem_total}")

            if contagem_total >= 100:
                print("Jogador de Elite!")
            else:
                print("Jogou Bem")
            
            vida = 0  # Finaliza a partida
    else:
        contagem_mortes += 1
        print(f"Você desistiu da luta e morreu!\nContagem de mortes: {contagem_mortes}\n")
        vida = 0

    return vida, vida_chefe, numeros_objetivos, contagem_mortes

# --- INÍCIO DO JOGO ---
vida = 100
pontos_inimigos = 0
contagem_mortes = 0
numeros_objetivos = 0

print("Escolha entre duas armas\n1-Arco\n2-Luvas")
arma = int(input("Opção: "))

while vida > 0:
    inimigos = random.randint(1, 50)
    print(f"\nVocê começa sua jornada. Terá que enfrentar {inimigos} inimigos!\n")

    d_20 = random.randint(1, 20)

    if d_20 >= 11:
        print(f"Você tirou {d_20} na rolagem de dados\nVocê derrotou todos os inimigos sem sofrer dano!\n")
        numeros_objetivos += 1
        pontos_inimigos = contagem_inimigos(inimigos, pontos_inimigos)
    else:
        print(f"Você tirou {d_20} na rolagem de dados\nVocê derrotou os inimigos, mas perdeu vida!\n")
        numeros_objetivos += 1
        pontos_inimigos, vida = contagem_inimigos_perda_vida(inimigos, pontos_inimigos, vida)

    if vida <= 0:
        contagem_mortes += 1
        print(f"Sua vida chegou a zero. Você morreu!\nContagem de mortes: {contagem_mortes}")
        break

    print("Escolha uma das melhorias:\n1-Dano Crítico e ataque mais rápido\n2-Ataque com mais dano e dano em área\n3-Não pegar nenhum")
    melhoria = int(input("Opção: "))

    if melhoria == 1 or melhoria == 2:
        numeros_objetivos += 1
        vida_chefe = 120
        print("\nVocê encontrou um chefe na sua jornada!\n")

        while vida_chefe > 0 and vida > 0:
            vida, vida_chefe, numeros_objetivos, contagem_mortes = luta_chefe(
                vida,
                vida_chefe,
                d_20,
                numeros_objetivos,
                pontos_inimigos,
                contagem_mortes
            )
    else:
        print("\nVocê não pegou nenhuma melhoria. Ganhará mais pontuações se concluir o próximo objetivo!\n")