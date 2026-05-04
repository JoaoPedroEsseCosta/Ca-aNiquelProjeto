from Jogo import *


def sistema_de_winlose():
    resultado, escolhas = iniciar_jogo()
    print()
    print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
    print(escolhas)


    if resultado == True:
        for _ in range(3):
            print("💰✨ VOCÊ VENCEU! ✨💰")
        print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
    else:
        for _ in range(3):
            print("☠️✦ VOCÊ PERDEU ✦☠️")
        print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")