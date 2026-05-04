from iniciarGame import iniciar_cn
from SistemaDeWinLose import sistema_de_winlose

iniciar_cn()
sistema_de_winlose()
while True:
    rerun = str(input("Re-jogar? \n1: Sair\n2: Jogar\nEscolha uma opção: "))
    if rerun == "2":
        sistema_de_winlose()
    else:
        break










