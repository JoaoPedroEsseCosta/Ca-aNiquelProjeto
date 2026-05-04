import random


def iniciar_jogo():
    listajogo = ["🍒", "7️⃣", "🎲", "🔔", "♠️", "🐎", "🍋", ]
    pesos = [30, 1, 5, 8, 12, 10, 20]

    escolhas = random.choices(listajogo,weights=pesos, k=3)

    if escolhas[0] == escolhas[1] == escolhas[2]:
       return True , escolhas
    else:
       return False, escolhas












