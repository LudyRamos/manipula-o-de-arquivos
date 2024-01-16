def cadastrar_evento():
    agenda = open('agenda.txt','a')
    evento = input('informe o evento: \n')
    evento += '\n'
    agenda.write(evento)
    agenda.close()

def apagar_agenda():
    agenda = open('agenda.txt','w')
    agenda.write('')
    agenda.close()

def visualizar_agenda():
    agenda = open('agenda.txt','r')
    for evento in agenda.readlines():
        print(evento)
    agenda.close()

while True:
    mensagem = 'o que deseja fazer?\n[c]adastrar evento\n[a]pagar agenda\n[v]visualizar agenda\n[s]air\n'
    opcao = input(mensagem)
    if opcao == 'c':
        cadastrar_evento()
    elif opcao == 'a':
        apagar_agenda()
    elif opcao == 'v':
        visualizar_agenda()
    elif opcao =='s':
        break
    else:
        print('opção invalida')