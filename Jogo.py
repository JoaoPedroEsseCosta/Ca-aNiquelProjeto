import random
import time


def IniciarJogo(resultadoCN):
    listajogo = ["🍒", "7️⃣", "🎲", "🔔", "♠️", "🐎", "🍋", ]

    escolhas = random.choices(listajogo, k=3)
    print("┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅")
    print("RESULTADO: ", escolhas)
    print("┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅")


    if escolhas[0] == escolhas[1] == escolhas[2]:
        print("✦✦✦ ✨ VOCÊ GANHOU! ✨ ✦✦✦")
        print("✦✦✦ ✨ VOCÊ GANHOU! ✨ ✦✦✦")
        print("✦✦✦ ✨ VOCÊ GANHOU! ✨ ✦✦✦")
    else:
        print("✦✦✦ ❌ VOCÊ PERDEU! ❌ ✦✦✦")
        print("✦✦✦ ❌ VOCÊ PERDEU! ❌ ✦✦✦")
        print("✦✦✦ ❌ VOCÊ PERDEU! ❌ ✦✦✦")


    acao = int(input("DESEJA CONTINUAR? \n1: SAIR \n2: CONTINUAR "))

    match acao:
        case 1:
            acao = "sair"
        case 2:
            acao = "jogar"

    if acao == "sair":
        print("FECHANDO CAÇA NÍQUEL")
    elif acao == "jogar":
        print("REJOGANDO")
        IniciarJogo("CEREJA")
    else:
        print("OPÇÃO INVÁLIDADA")











