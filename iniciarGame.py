from Jogo import IniciarJogo


def iniciarCn():
    case = int(input("Gostaria de iniciar o CAÇA NIQUEL?  \n1: Sair\n2: Jogar\nEscolha uma opção: "))
    acao = None

    match case:
        case 1:
            acao = "sair"
        case 2:
            acao = "jogar"

    if acao == "sair":
        print("SAINDO...")
        return
    elif acao == "jogar":
        print("ENTRANDO...")
        IniciarJogo("CEREJA")
    else:
        print("OPÇÃO INVÁLIDA")


